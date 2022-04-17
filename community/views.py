from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


# Create your views here.

def write(request):
    Article.name = 'inzae'
    return render(request, 'write.html', Article.name)
