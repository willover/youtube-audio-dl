from youtubeadl.apps.core.utils import slugify

import youtube_dl


def create_filename(value):
    """
    Generate a valid filename.

    Non-ASCII characters will be deleted from the value and replace spaces with
    underscores. Slashes and percent signs are also stripped.
    """
    return '{}.mp3'.format(slugify(value, u'_'))


def get_video_info(url):
    """
    Retrieve the YouTube videos' information without downloading it.

    Source: http://stackoverflow.com/questions/18054500/how-to-use-youtube-dl-\
            from-a-python-programm/18947879#18947879
    """
    ydl = youtube_dl.YoutubeDL()
    ydl.add_default_info_extractors()

    try:
        return ydl.extract_info(url, download=False)
    except youtube_dl.DownloadError:
        return None