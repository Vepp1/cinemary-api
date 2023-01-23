from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
