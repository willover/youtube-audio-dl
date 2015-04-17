from django.contrib import admin
from django.utils.text import Truncator

from youtubeadl.apps.downloader import models


@admin.register(models.ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = (
        'video',
        'client_ip',
        'action',
        'created',
    )
    list_filter = ('action', 'client_ip')

    def video_title(self, obj):
        return Truncator(obj.video.title).chars(50)
    video_title.admin_order_field = 'video__title'


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'youtube_id',
        'audio_filename',
        'duration',
        'download_count',
        'last_download_date'
    )
