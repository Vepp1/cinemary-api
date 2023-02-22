from rest_framework import generics, permissions, filters
from .models import Posts
from .serializers import PostSerializer
from cinemary_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Posts.objects.annotate(likes_count=Count(
        'likes', distinct=True), comments_count=Count('comments', distinct=True),).order_by('-created_at')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    search_fields = [
        'owner__username',
        'title',
        'genrer',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Posts.objects.annotate(likes_count=Count(
        'likes', distinct=True), comments_count=Count('comments', distinct=True),).order_by('-created_at')
