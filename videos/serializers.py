from rest_framework import serializers

class SearchQuerySerializer(serializers.Serializer):
    searchQuery = serializers.CharField()

    def validate(self, attrs):
        
        if attrs['searchQuery'] == '':
            raise serializers.ValidationError({"searchQuery":"Please input query to search"})

        return attrs
