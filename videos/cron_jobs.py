
from .models import Video
from django.conf import settings
import requests


import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# YT API endpoints
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

def fetch_youtube_video():
    #logic
    #fetch video from YT
    #save it to db

    print('cron job starts executing') 

    query = 'cricket'

    search_parameters = {
        'key': settings.YOUTUBE_API_KEY,
        'part': 'snippet',
        'q': query,
        'type':'video',
        'videoEmbeddable': True,
        'maxResults':10, #10 result as given in assignment
    }
    response = requests.get(SEARCH_URL, params=search_parameters).json()['items']

# Iterate through the results and store them in list and bulk upload 
    youtube_video_response = []
    for item in response['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        description = item['snippet']['description']
        published_at = item['snippet']['publishedAt']
        thumbnail_url = item['snippet']['thumbnails']['url']
        
        youtube_video_response.append(video_id=video_id,title=title,description=description,published_at=published_at,thumbnail_url=thumbnail_url)

        # Create or update the Video model with the fetched data

        # video, created = Video.objects.update_or_create(
        #     video_id=video_id,
        #     defaults={
        #         'title': title,
        #         'description': description,
        #         'published_at': published_at,
        #         'thumbnail_url': thumbnail_url,
        #     }
        # )

    Video.objects.bulk_create(youtube_video_response)