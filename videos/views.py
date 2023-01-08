from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
import requests
from rest_framework.permissions import AllowAny

# Serializers
from .serializers import SearchQuerySerializer, VideoSerializer

# Models
from .models import Video

# pagination
from rest_framework.generics import ListAPIView
from rest_framework import pagination

#utils 
from .utils import CustomPagination, VideoFilter
from django_filters.rest_framework import DjangoFilterBackend

# YT API endpoints
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'


class TestAppAPIView(APIView):
    def get(self, request, format=None):
        try:
            result = 'testing get api'
            print(result)
            return Response({'status': True,
                             'Response': "Successfully Tested"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class GetYTVideos(APIView):
    permission_classes = (AllowAny,)
    #logic
    #first serialize request parameter
    #make request to YT api endpoint with input parameter
    #format/modify returned JSON response in chrological order(as is asked in assignment)
    #return top 10 request 
    #and we are done :)
    def post(self,request):
        print(request.data)
        serializer = SearchQuerySerializer(data=request.data)

        if serializer.is_valid():
            #fetch video from YT
            #format/modify
            #return result
            print('almost done')
            #YT video accept following parameter to return result
            print('query: ',serializer.data)
            search_parameters = {
                'key': settings.YOUTUBE_API_KEY,
                'part': 'snippet',
                'q':serializer.data['searchQuery'],
                'type':'video',
                'videoEmbeddable': True,
                'maxResults':10, #10 result as given in assignment
            }
            fetched_data = requests.get(SEARCH_URL, params=search_parameters).json()['items']

            print(fetched_data)
            return Response({
                'msg':'videos fetched successfully',
                'videos': fetched_data,
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class VideoListView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = VideoFilter
    ordering_fields = ['published_at']
    ordering = ['-published_at']

    def get_queryset(self):
        return Video.objects.filter().order_by('-published_at')


            
         



