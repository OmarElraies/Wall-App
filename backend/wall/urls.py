from wall.views import PostViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

posts_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
posts_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('posts/', posts_list, name='posts-list'),
    path('posts/<int:pk>/', posts_detail, name='posts-detail'),
])