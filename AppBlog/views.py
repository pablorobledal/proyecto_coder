from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppBlog.urls import *
# Create your views here.


def inicio(request):
    return render(request, 'AppBlog/templates/index.html')

def nosotros(request):
    return render(request, 'AppBlog/templates/nosotros.html')

def reglas(request):
    return render(request, 'AppBlog/templates/reglas.html')

def lotr(request):
    return render(request, 'AppBlog/templates/lotr.html')

def mistborn(request):
    return render(request, 'AppBlog/templates/mistborn.html')

def narnia(request):
    return render(request, 'AppBlog/templates/narnia.html')

def got(request):
    return render(request, 'AppBlog/templates/got.html')

def mensajes(request):
    return render(request, 'AppBlog/templates/mensajes.html')

def posts(request):
    return render (request,'AppBlog/templates/listado-post.html')