from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Track
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import TrackForm
# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
        #return HttpResponse('<script>alert("Holi")</script>')
    else:
        username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/login")
        return render(request, "sfotipy/login.html", {})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        first_name = last_name = username = password = email = ''
        if request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if(first_name != '' and last_name != '' and username != '' and email != '' and password != ''):
                user = User.objects.create_user(first_name =first_name, last_name = last_name, username=username, email=email, password=password)
                user.save()
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/signup")
        return render(request, "sfotipy/signup.html", {})

@login_required(login_url='/login/')
def mainpage(request):
	context = {}
	return render(request, 'sfotipy/mainpage.html', context)

@login_required(login_url='/login/')
def tracks(request):
    tracks = Track.objects.order_by('title')
    context = {'tracks':tracks}
    return render(request, 'tracks/tracks.html', context)

@login_required(login_url='/login/')
def tracks_view(request, pk):
    track = get_object_or_404(Track, pk=pk)
    dct = {'track':track}
    return render(request, 'tracks/track_view.html', dct)
    
@login_required(login_url='/login/')
def tracks_new(request):
    if request.user.is_superuser:
        if request.POST:
            form = TrackForm(request.POST, request.FILES)
            if form.is_valid():
                track = form.save(commit=False)
                track.save()
            return HttpResponseRedirect("/tracks")
        else:
            form = TrackForm()
        return render(request, 'tracks/track_edit.html', {'form':form})
    else:
        return HttpResponseRedirect("/")

@login_required(login_url='/login/')
def tracks_edit(request, pk):
    if request.user.is_superuser:
        track = get_object_or_404(Track, pk=pk)
        if request.POST:
            form = TrackForm(request.POST, request.FILES, instance=track)
            if form.is_valid():
                track = form.save(commit=False)
                track.save()
            return HttpResponseRedirect("/tracks")
        else:
            form = TrackForm(instance=track)
        return render(request, 'tracks/track_edit.html', {'form':form, 'track':': ' + track.title})
    else:
        return HttpResponseRedirect("/")
