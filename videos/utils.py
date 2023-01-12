from rest_framework import pagination
#import django_filters
from .models import Video

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page_number'



# class VideoFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     description = django_filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = Video
#         fields = ['title', 'description']