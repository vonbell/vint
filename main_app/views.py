from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vinyl, Photo
from .forms import VinylForm
import boto3
import uuid

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'vint'


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

def add_photo(request, vinyl_id):
    photo_file = request.FILES.get('photo-file', None)

    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, vinyl_id=vinyl_id)
            photo.save()
        except Exception as error:
            print('*************************')
            print('An error occurred uploading file to S3:')
            print(error)
            print('*************************')
    return redirect('detail', vinyl_id=vinyl_id)


class VinylCreate(CreateView):
    model = Vinyl
    fields = ('artist', 'album', 'release_date', 'genre', 'description')

class VinylUpdate(UpdateView):
    model = Vinyl
    fields = ('release_date', 'genre', 'description')

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls/'