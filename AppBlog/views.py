from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from AppBlog.urls import *
from .forms import *
from .models import Posteo
from . import forms
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.



def inicio(request):
    posteos=Posteo.objects.all()

    return render(request, 'AppBlog/templates/index.html', {'posteos':posteos})

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

def crear_posteo(request):
    if request.method == 'POST':
        form = forms.CrearPosteo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autor = request.user.username
            instance.save()
            return redirect('AppBlog:inicio')
    else:
        form = forms.CrearPosteo()
    return render(request, 'crear_posteo.html', { 'form': form })

class BorrarPosteo(SuccessMessageMixin,DeleteView):
    model = Posteo
    fields="__all__"
    template_name='posteo_confirm_delete.html'
    

    def get_success_url(self):
        succeess_message='Usuario Eliminado Correctamente'
        messages.success(self.request, (succeess_message))
        return reverse_lazy('AppBlog:inicio') 

 