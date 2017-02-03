from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.albums_view, name='albums_view'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.albums_edit, name='albums_edit'),
    url(r'^new/$', views.albums_new, name='albums_new'),
    url(r'^(?P<pk>[0-9]+)/$', views.album_view, name='album_view'),
]