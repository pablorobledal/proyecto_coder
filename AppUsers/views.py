from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
# Create your views here.

def registro(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             login(request, user)
             return redirect('AppBlog:inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', { 'form': form })

def cerrar_sesion(request):
    if request.method == 'POST':
            logout(request)
            return redirect('AppBlog:inicio')

def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return render(request, 'index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })


class editar_usuario (UpdateView):
    model = User
    form=UserCreationForm
    template_name='editar_perfil.html'
    fields="__all__"
    succes_message='Usuario editado correctamente'

    def get_succes_url(self):
        return reverse_lazy('perfil.html')

class borrar_usuario(SuccessMessageMixin,DeleteView):
    model = User
    form=UserCreationForm
    fields="__all__"
    

    def get_success_url(self):
        succeess_message='Usuario Eliminado Correctamente'
        messages.success(self.request, (succeess_message))
        return reverse_lazy('AppBlog:index.html') 

def miperfil(request, username):
    perfil=Perfil.objects.get(username=username)
    return render(request, 'miperfil.html')
    

