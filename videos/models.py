from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Video(models.Model):
    video_id = models.CharField(max_length=255,unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    key = models.CharField(max_length=64)
    requests = models.IntegerField(default=100) #user can make 100 API request at max using one api key










