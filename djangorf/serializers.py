from django.contrib.auth.models import User, Group
from artists.models import Artist
from albums.models import Album
from tracks.models import Track
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artist
		fields = ('first_name', 'last_name', 'image','biography')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Album
		fields = ('title', 'cover', 'artist')

class TrackSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Track
		fields = ('title', 'track_file', 'album')