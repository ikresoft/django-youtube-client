from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('',
    url(r'playlists/$', playlists, name="youtube-playlists"),
    url(r'videos/(?P<playlist>.*)/$', videos, name="youtube-videos"),
)