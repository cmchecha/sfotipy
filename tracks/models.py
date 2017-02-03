from __future__ import unicode_literals
from django.db import models
from albums.models import Album

# Create your models here.

class Track(models.Model):
	title = models.CharField(max_length=255)
	track_file = models.FileField(upload_to='tracks')
	album = models.ForeignKey(Album)

	def __unicode__(self):
		return self.title