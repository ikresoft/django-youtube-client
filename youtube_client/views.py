from django.shortcuts import render
from apiclient.discovery import build
from django.conf import settings


def playlists(request):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    playlists = youtube.playlists().list(part="snippet", channelId=settings.YOUTUBE_CHANNEL_ID, maxResults=50).execute()
    return render(request, "youtube_client/channel_playlists.html", {'playlists': playlists["items"]})


def videos(request, playlist):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    videos = youtube.playlistItems().list(part='snippet', playlistId=playlist, maxResults=50).execute()
    return render(request, "youtube_client/playlist_videos.html", {'videos': videos["items"]})

