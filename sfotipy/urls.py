from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
from djangorf import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'tracks', views.TrackViewSet)

urlpatterns = [
	
    url(r'^schema/$', schema_view),
    url(r'^admin/', admin.site.urls),

    url(r'', include('tracks.urls')),
    url(r'^albums/', include('albums.urls')),
    url(r'^artists/', include('artists.urls')),

    url(r'^api-rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^snippets/', include('snippets.urls')),

    #url(r'^vs/', include('artists.urls_rest')),

    #url(r'^tracks/(?P<title>[\w-\]+)/$', views.track_view, name='track_view'),
    #url(r'^productos/eliminar/(?P<pk>[0-9]+)/$', views.producto_eliminar, name='producto_eliminar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #   DESPLIEGUE DE ARCHIVOS MEDIA