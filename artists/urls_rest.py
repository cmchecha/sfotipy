from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import ArtistViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'users', views.UserViewSet)



urlpatterns = [

    url(r'^', include(router.urls)),

]


urlpatterns = format_suffix_patterns(urlpatterns)