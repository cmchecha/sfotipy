from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import renderers

urlpatterns = [
    url(r'^$', views.artists_view, name='artists_view'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.artists_edit, name='artists_edit'),
    url(r'^new/$', views.artists_new, name='artists_new'),
    url(r'^(?P<pk>[0-9]+)/$', views.artist_view, name='artist_view'),

    #	HYPERLINKEDMODELSERIALIZER
    url(r'^serializer/$', views.artist_list),
    url(r'^serializer/(?P<pk>[0-9]+)/$', views.artist_detail),

    #	MODEL SERIALIZER
    url(r'^list_api/$', views.artist_list_api),
    url(r'^list_api/(?P<pk>[0-9]+)/$', views.artist_detail_api),

    #	CLASS BASED VIEWS
    url(r'^cbv_api/$', views.ArtistView.as_view()),
    url(r'^cbv_api/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view()),

    #	MIXINS
    url(r'^mixin_api/$', views.ArtistViewMixin.as_view()),
    url(r'^mixin_api/(?P<pk>[0-9]+)/$', views.ArtistDetailMixin.as_view()),

    #	GENERIC CLASS BASED VIEWS
    url(r'^generic_cbv/$', views.ArtistViewGeneric.as_view()),
    url(r'^generic_cbv/(?P<pk>[0-9]+)/$', views.ArtistDetailGeneric.as_view(), name='artist-detail'),

    #	USERS 
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),


    #	API ROOT AND HYPERLINKING OUR API 
    url(r'^api_root/$', views.api_root),
    url(r'^(?P<pk>[0-9]+)/first_name/$', views.ArtistFirstName.as_view(), name='artist-first-name'),

    #	CORE API

]

#	VIEWSET BASED API


urlpatterns = format_suffix_patterns(urlpatterns)