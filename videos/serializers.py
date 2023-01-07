from rest_framework import serializers
from .models import Video

class SearchQuerySerializer(serializers.Serializer):
    searchQuery = serializers.CharField()

    def validate(self, attrs):
        
        if attrs['searchQuery'] == '':
            raise serializers.ValidationError({"searchQuery":"Please input query to search"})

        return attrs


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video_id','title', 'description', 'published_at', 'thumbnail_url']    