from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^$', views.mainpage, name='mainpage'),
    url(r'^tracks/(?P<pk>[0-9]+)/$', views.tracks_view, name='tracks_view'),
    url(r'^tracks/$', views.tracks, name='tracks'),
    url(r'^tracks/new/$', views.tracks_new, name='tracks_new'),
    url(r'^tracks/edit/(?P<pk>[0-9]+)/$', views.tracks_edit, name='tracks_edit'),
]