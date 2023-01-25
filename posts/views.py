from rest_framework import generics, permissions, filters
from .models import Posts
from .serializers import PostSerializer
from cinemary_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
