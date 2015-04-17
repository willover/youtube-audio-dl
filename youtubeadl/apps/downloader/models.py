from django.db import models

from django_extensions.db.models import TimeStampedModel


class Video(TimeStampedModel):
    youtube_id = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=255)
    title = models.TextField()
    duration = models.IntegerField(null=True)
    audio_filename = models.CharField(max_length=255, null=True, blank=True)
    audio_filesize = models.IntegerField(null=True)
    download_count = models.IntegerField(null=True, default=0)
    last_download_date = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.youtube_id


class ActivityLog(TimeStampedModel):
    """
    Store user activity.
    """
    CONVERT = 'convert'
    DOWNLOAD = 'download'
    ACTION_CHOICES = (
        (CONVERT, 'Convert'),
        (DOWNLOAD, 'Download'),
    )

    video = models.ForeignKey(Video)
    client_ip = models.GenericIPAddressField(null=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)