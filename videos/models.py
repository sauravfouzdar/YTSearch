from django.db import models

# Create your models here.


class Video(models.Model):
    video_id = models.CharField(max_length=255,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()











