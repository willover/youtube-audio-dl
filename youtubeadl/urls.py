from django.conf.urls import include, url
from django.contrib import admin

from youtubeadl.apps.downloader.views import DownloadFormView

urlpatterns = [
    url(r'^$', DownloadFormView.as_view(), name='home'),
    url(r'^downloader/', include('youtubeadl.apps.downloader.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
