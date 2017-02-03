from django import forms
from django.contrib.auth.models import User
from .models import Track
from django.forms import ModelForm

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('title', 'track_file', 'album',)
