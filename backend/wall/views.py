from rest_framework.viewsets import ModelViewSet
from rest_framework import  viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)
