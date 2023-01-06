from django.urls import path
from .views import TestAppAPIView, GetYTVideos

urlpatterns = [
    path('test/', TestAppAPIView.as_view(), name='video-app'),
    path('search-video', GetYTVideos.as_view(), name='video-app')
]