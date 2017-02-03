from django import forms
from django.contrib.auth.models import User
from .models import Album
from django.forms import ModelForm

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'cover', 'artist',)
