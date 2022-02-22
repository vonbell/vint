from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vinyl

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyls_index(request):
    # vinyls = Vinyl.objects.filter(user=request.user)
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/index.html', { 'vinyls': vinyls })

def vinyls_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    return render(request, 'vinyls/detail.html', { 'vinyl': vinyl })

class VinylCreate(CreateView):
    model = Vinyl
    fields = ('artist', 'album', 'release_date', 'genre', 'description')