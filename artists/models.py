from __future__ import unicode_literals
from django.db import models

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

class Artist(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	image = models.ImageField(upload_to='images/artists/', blank=True, default='images/artists/default.jpg')
	biography = models.TextField(blank=True)

	#owner = models.ForeignKey('auth.User', related_name='artists', on_delete=models.CASCADE, blank=True)
	owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='artists')
	#highlighted = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.first_name + '  ' + self.last_name
