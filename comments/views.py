from rest_framework import generics, permissions
from .models import Comments
from .serializers import CommentsSerializer
from cinemary_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
