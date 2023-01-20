from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.urls import reverse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .forms import *
from AppBlog.models import *
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
               return redirect('AppBlog:inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })


class editar_perfil (UpdateView):
    model = Perfil
    template_name='editar_perfil.html'
    fields=['alias','email','bio','avatar']
    succes_message='Perfil editado correctamente'
    success_url=reverse_lazy('AppBlog:redireccionar')



class borrar_perfil(SuccessMessageMixin,DeleteView):
    model = User
    fields="__all__"
    template_name='perfil_confirm_delete.html'
    

    def get_success_url(self):
        succeess_message='Usuario Eliminado Correctamente'
        messages.success(self.request, (succeess_message))
        return reverse_lazy('AppBlog:inicio') 

def miperfil (request, username):
    perfil=Perfil.objects.get(username=username)
    posteos=Posteo.objects.filter(username=username)
    return render(request, 'miperfil.html', {"perfil":perfil, "posteos":posteos})
    

