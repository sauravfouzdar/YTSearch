from django.urls import path
from .views import TestAppAPIView, GetYTVideos,VideoListView

urlpatterns = [
    path('test/', TestAppAPIView.as_view(), name='video-app'),
    path('search-video', GetYTVideos.as_view(), name='video-app'),
    path('video', VideoListView.as_view(), name='video-search')
]

