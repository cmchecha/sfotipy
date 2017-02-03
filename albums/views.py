from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Album
from django.contrib.auth.decorators import login_required
from .forms import AlbumForm

@login_required(login_url='/login/')
def albums_view(request):
    albums = Album.objects.order_by('title')
    context = {'albums':albums}
    return render(request, 'albums/albums.html', context)

@login_required(login_url='/login/')
def albums_new(request):
    if request.user.is_superuser:
        if request.POST:
            form = AlbumForm(request.POST, request.FILES)
            if form.is_valid():
                album = form.save(commit=False)
                album.save()
            return HttpResponseRedirect("/albums")
        else:
            form = AlbumForm()
        return render(request, 'albums/album_edit.html', {'form':form})
    else:
        return HttpResponseRedirect("/")

@login_required(login_url='/login/')
def albums_edit(request, pk):
    if request.user.is_superuser:
        album = get_object_or_404(Album, pk=pk)
        if request.POST:
            form = AlbumForm(request.POST, request.FILES, instance=album)
            if form.is_valid():
                album = form.save(commit=False)
                album.save()
            return HttpResponseRedirect("/albums")
        else:
            form = AlbumForm(instance=album)
        return render(request, 'albums/album_edit.html', {'form':form, 'album':': ' + album.title})
    else:
        return HttpResponseRedirect("/")


@login_required(login_url='/login/')
def album_view(request, pk):    
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_view.html', {'album':album})
    