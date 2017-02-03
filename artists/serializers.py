from rest_framework import serializers
from .models import Artist
from django.contrib.auth.models import User

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #first_name = serializers.HyperlinkedIdentityField(view_name='artist-first-name', format='html')
    owner = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name', 'image', 'biography', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #artists = serializers.PrimaryKeyRelatedField(many=True, queryset=Artist.objects.all())
    artists = serializers.HyperlinkedRelatedField(many=True, view_name='artist-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'artists')