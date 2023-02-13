from rest_framework import generics, permissions
from .models import Likes
from .serializers import LikesSerializer
from cinemary_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self.serializer):
        serializer.save(owner=self.request.user)
