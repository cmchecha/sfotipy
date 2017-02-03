from django import forms
from django.contrib.auth.models import User
from .models import Artist
from django.forms import ModelForm

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'image', 'biography', 'owner')
