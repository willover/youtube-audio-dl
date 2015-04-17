import datetime
import os
import urllib
from urlparse import urlparse, parse_qs, urlsplit, urlunsplit

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.encoding import smart_str
from django.views.generic import TemplateView, View

from braces.views import JSONResponseMixin, AjaxResponseMixin, CsrfExemptMixin
from celery.result import AsyncResult

from youtubeadl.apps.core.utils import get_client_ip

from youtubeadl.apps.downloader import tasks
from youtubeadl.apps.downloader.models import ActivityLog, Video


class DownloadFormView(TemplateView):
    template_name = 'home.html'


class ConvertAjaxView(CsrfExemptMixin, JSONResponseMixin, AjaxResponseMixin, View):
    """
    Ajax view to start the video conversion.
    """

    # TODO: change to post_ajax and remove csrf exemption
    def post(self, request, *args, **kwargs):
        url = self.parse_url(request.POST.get('url', '').strip())

        if url:
            # Call celery task.
            task = tasks.convert.delay(url, get_client_ip(request))
            result = AsyncResult(task.id)
            result.wait()

            if result.successful():
                data = {
                    'message': 'Conversion successful!',
                    'task_id': task.id
                }

                if result.result:
                    youtube_id = result.result['youtube_id']
                    filename = result.result['filename']
                    download_link = reverse(
                        'download_view',
                        kwargs={'youtube_id': youtube_id, 'filename': filename}
                    )

                    data['video_id'] = youtube_id
                    data['filename'] = filename
                    data['download_link'] = download_link

                    return self.render_json_response(data, status=200)

            return self.render_json_response(
                {'message': 'Something went wrong.'}, status=500)

        return self.render_json_response({'message': 'Please provide a URL.'},
                                         status=400)

    def parse_url(self, url):
        """
        Remove the list parameter from the URL as we currently don't support
        conversion of an entire playlist.
        """
        qs = parse_qs(urlparse(url).query)
        if qs.get('list', None):
            del(qs['list'])
            parts = urlsplit(url)
            return urlunsplit([
                parts.scheme,
                parts.netloc,
                parts.path,
                urllib.urlencode(qs, True),
                parts.fragment
            ])

        return url


def download(request, youtube_id, filename):
    """
    Serves the audio file.
    """
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    file_exists = os.path.exists(filepath)

    video = None
    try:
        # We need to filter by both the youtube_id and audio_filename as the
        # record might exists but the video is still being converted.
        video = Video.objects.get(youtube_id=youtube_id, audio_filename=filename)
    except Video.DoesNotExist:
        pass

    if video and file_exists:
        ActivityLog.objects.create(
            video=video,
            action=ActivityLog.DOWNLOAD,
            client_ip=get_client_ip(request),
        )

        video.download_count += 1
        video.last_download_date = datetime.datetime.now()
        video.save()

        if settings.DEBUG:
            with open(filepath, 'rb') as file_data:
                response = HttpResponse(file_data.read(),
                                        content_type='audio/mpeg')

            response['Content-Disposition'] = 'attachment; filename={}'.format(
                smart_str(filename))
            response['Content-Length'] = os.path.getsize(filepath)

            return response
        else:
            # Have Nginx serve the file in production.
            response = HttpResponse(mimetype='application/force-download')
            response['Content-Length'] = os.path.getsize(filepath)
            response['X-Accel-Redirect'] = os.path.join(settings.MEDIA_URL,
                                                        smart_str(filename))

            return response

    return HttpResponseRedirect(reverse('home'))