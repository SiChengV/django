from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    movie = models.MovieInfo.objects.get(id=1)   #从数据库获取数据
    return render(request, 'index.html', {'movie':movie})