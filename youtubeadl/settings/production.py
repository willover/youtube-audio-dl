from base import *


DEBUG = False

ALLOWED_HOSTS = ['.youtubeadl.com']


MEDIA_ROOT = '/webapps/youtubeadl/media/'


# Use the cached template loader so template is compiled once and read from
# memory instead of reading from disk on each load.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
