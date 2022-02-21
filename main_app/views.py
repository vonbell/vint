from django.shortcuts import render
from .models import Vinyl

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyls_index(request):
    # vinyls = Vinyl.objects.filter(user=request.user)
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/index.html', { 'vinyls': vinyls })