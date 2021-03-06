from django import template
from django.conf import settings

from apiclient.discovery import build
import random

register = template.Library()


@register.inclusion_tag("youtube_client/templatetags/channel_playlists.html")
def channel_playlists(limit=3):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    playlists = youtube.playlists().list(part="snippet", channelId=settings.YOUTUBE_CHANNEL_ID, maxResults=50).execute()
    return {
        'playlists': random.sample(playlists['items'], limit)
    }


@register.inclusion_tag("youtube_client/templatetags/random_videos.html")
def random_videos(limit=3):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    videos = youtube.search().list(part='snippet', channelId=settings.YOUTUBE_CHANNEL_ID, order='date', maxResults=50).execute()
    return {
        'videos': random.sample(videos["items"], limit)
    }
