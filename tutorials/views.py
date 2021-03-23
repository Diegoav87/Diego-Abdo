from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.


def tutorials(request):
    channel_url = 'https://www.googleapis.com/youtube/v3/channels'
    playlist_url = 'https://www.googleapis.com/youtube/v3/playlistItems'

    channel_params = {
        'part': 'contentDetails',
        'id': 'UCWvinsn7iTIha1WqhgxstBQ',
        'key': settings.YOUTUBE_DATA_API_KEY
    }

    r = requests.get(channel_url, params=channel_params)
    playlist_id = r.json()[
        'items'][0]['contentDetails']['relatedPlaylists']['uploads']

    playlist_params = {
        'part': 'snippet',
        'maxResults': 9,
        'playlistId': playlist_id,
        'key': settings.YOUTUBE_DATA_API_KEY
    }

    r = requests.get(playlist_url, params=playlist_params)
    videos = r.json()['items']

    video_list = []

    for video in videos:
        video_data = {
            'title': video['snippet']['title'],
            'id': video['snippet']['resourceId']['videoId'],
            'url': f"https://www.youtube.com/watch?v={video['snippet']['resourceId']['videoId']}",
            'thumbnail': video['snippet']['thumbnails']['high']['url']
        }
        video_list.append(video_data)

    return render(request, 'tutorials/tutorials.html', {'videos': video_list})
