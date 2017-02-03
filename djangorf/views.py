from django.contrib.auth.models import User, Group
from artists.models import Artist
from albums.models import Album
from tracks.models import Track
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, ArtistSerializer, AlbumSerializer, TrackSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Artist.objects.all().order_by('first_name')
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer