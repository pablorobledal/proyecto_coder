from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from AppBlog.urls import *
from .forms import *
from .models import Posteo
from AppUsers.models import Perfil
from . import forms
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.models import User
from django.db.models import Q

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



def inicio(request):
    posteos=""
    posteos=Posteo.objects.all()
    context = {}
    lista = ""
    if request.GET:
        lista = request.GET['n']
        context['lista']=str(lista)
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


def posts(request):
    return render (request,'AppBlog/templates/listado-post.html')

@login_required(login_url='AppUsers:iniciar_sesion')
def crear_posteo(request):
    if request.method == 'POST':
        form = forms.CrearPosteo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user.username
            instance.autor=Perfil.objects.get(username=request.user).alias
            instance.save()
            return redirect('AppBlog:inicio')
    else:
        form = forms.CrearPosteo()
    return render(request, 'crear_posteo.html', { 'form': form })

def redireccionar(request):
   user = request.user
   username=user.username
   perfil=Perfil.objects.get(username=username)
   posteos=Posteo.objects.filter(username=username)
   return render(request,'AppUsers/templates/miperfil.html', {'posteos':posteos, 'perfil':perfil})


class editar_posteo (LoginRequiredMixin, UpdateView):
    model = Posteo
    template_name='editar_perfil.html'
    fields=['titulo','universo','cuerpo','imagen']
    succes_message='Posteo editado correctamente'
    success_url=reverse_lazy('AppBlog:redireccionar')
    login_url=reverse_lazy('AppUsers:iniciar_sesion')

class borrar_posteo(LoginRequiredMixin, SuccessMessageMixin,DeleteView):
    model = Posteo
    fields="__all__"
    template_name='posteo_confirm_delete.html'
    login_url=reverse_lazy('AppUsers:iniciar_sesion')
    
    
    def get_success_url(self):
        succeess_message='Usuario Eliminado Correctamente'
        messages.success(self.request, (succeess_message))
        return reverse_lazy('AppBlog:redireccionar') 

def visitar_perfil(request, username):
    posteos=Posteo.objects.filter(username=username)
    perfil=Perfil.objects.get(username=username)
    return render(request, 'AppUsers/templates/visitar_perfil.html', {'perfil':perfil, 'posteos':posteos})


def visitar_posteo(request, titulo):
    posteo=Posteo.objects.get(titulo=titulo)
    return render(request, 'visitar_posteo.html',{'posteo':posteo})


def buscar(request):
    busqueda_completa= request.GET["n"]
    busqueda_separada=busqueda_completa.split()
    lista_busqueda= []
    #busqueda=lista
    if busqueda_separada!=[]:
        for busqueda in busqueda_separada:
            posteos = Posteo.objects.filter(
                Q(titulo__icontains=busqueda) |
                Q(autor__icontains=busqueda) |
                Q(cuerpo__icontains=busqueda) |
                Q(universo__icontains=busqueda)     
            ).distinct()

            for posteo in posteos:
                lista_busqueda.append(posteo)
        lista_busqueda = list(set(lista_busqueda))
        return render(request, "AppBlog/templates/resultado_busqueda.html", {"lista_busqueda": lista_busqueda, "busqueda_completa":busqueda_completa})
        
    else:
        return redirect('AppBlog:inicio')



def visitar_universo(request, universo):
    return render(request, f"{universo}.html", {'universo':universo})


