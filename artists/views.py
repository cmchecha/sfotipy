from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, mixins, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from .forms import ArtistForm
from .models import Artist
from .serializers import ArtistSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly



########################################################################

@login_required(login_url='/login/')
def artists_view(request):
    artists = Artist.objects.order_by('first_name')
    context = {'artists':artists}
    return render(request, 'artists/artists.html', context)

@login_required(login_url='/login/')
def artists_new(request):
    if request.user.is_superuser:
        if request.POST:
            form = ArtistForm(request.POST, request.FILES)
            if form.is_valid():
                artist = form.save(commit=False)
                artist.save()
            return HttpResponseRedirect("/artists")
        else:
            form = ArtistForm()
        return render(request, 'artists/artist_edit.html', {'form':form})
    else:
        return HttpResponseRedirect("/")

@login_required(login_url='/login/')
def artists_edit(request, pk):
    if request.user.is_superuser:
        artist = get_object_or_404(Artist, pk=pk)
        if request.POST:
            form = ArtistForm(request.POST, request.FILES, instance=artist)
            if form.is_valid():
                artist = form.save(commit=False)
                artist.save()
            return HttpResponseRedirect("/artists")
        else:
            form = ArtistForm(instance=artist)
        return render(request, 'artists/artist_edit.html', {'form':form, 'artist':': ' + str(artist)})
    else:
        return HttpResponseRedirect("/")
    
@login_required(login_url='/login/')
def artist_view(request, pk):    
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artists/artist_view.html', {'artist':artist})


######################BASADO EN EL MODEL SERIALIZER######################################

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def artist_list(request):
    """
    List all artists, or create a new artist.
    """
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True, context={'request': request})
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def artist_detail(request, pk):
    """
    Retrieve, update or delete a artist.
    """
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist, context={'request': request})
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(artist, data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        artist.delete()
        return HttpResponse(status=204)


##################REQUEST AND RESPONSES######################################################


@api_view(['GET', 'POST', 'FILES'])
def artist_list_api(request, format=None):
    """
    List all artists, or create a new artist.
    """
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail_api(request, pk, format=None):
    """
    Retrieve, update or delete a artist instance.
    """
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#################### CLASS BASED VIEWS ###################################################

class ArtistView(APIView):
    """
    List all artists, or create a new artist.
    """
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistDetail(APIView):
    """
    Retrieve, update or delete a artist instance.
    """
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        artist = self.get_object(pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#####################   MIXINS  ########################################################


class ArtistViewMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ArtistDetailMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


###################   GENERIC CLASS BASED VIEWS     ####################################


class ArtistViewGeneric(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


###################   GENERIC CLASS BASED VIEWS     ####################################


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


###################    RELATIONSHIPS AND HIPERLINKED API'S  ###############################


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'artists': reverse('artist-list', request=request, format=format)
        #'snippets': reverse('snippet-list', request=request, format=format)
    })


class ArtistFirstName(generics.GenericAPIView):
    queryset = Artist.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        artist = self.get_object()
        return Response(artist.first_name)


###################    RELATIONSHIPS AND HIPERLINKED API'S  ###############################


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def first_name(self, request, *args, **kwargs):
        artist = self.get_object()
        return Response(artist.first_name)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


