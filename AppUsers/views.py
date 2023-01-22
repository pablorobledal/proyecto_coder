from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.core.exceptions import PermissionDenied
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
             canaldeusuario=CanaldeUsuario(usuario=user)
             canaldeusuario.save()
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


def DMs (request, username, *args, **kwargs):

    if not request.user.is_authenticated:
        return redirect('AppUsers:login')

    else:
     mi_username=request.user.username

     canal, created=Canal.objects.obtener_canal_dm(mi_username,username)
     if created:
        print("Si se creo mamon")

    Usuarios_Canal=canal.canaldeusuario_set.all().values("usuario__username")
    print(Usuarios_Canal)
    mensaje_canal=canal.canaldemensaje_set.all()
    print(mensaje_canal.values("texto"))
    print(canal.id)
    return reverse_lazy('AppUsers:DetalleDMs', kwargs={"username":username})
    #return render(request, 'mensajes.html', {'canal':canal})

class Buzon(View):
    def get(self, request):

        buzon=Canal.objects.filter(canaldeusuario__usuario__in=[request.user.id])

        context={"buzon":buzon}

        return render(request, 'buzon.html', context)

class CanalFormMixin(FormMixin):
    form_class = FormDeMensajes
    

    def get_success_url(self):
        return self.request.path


    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        if not request.user.is_authenticated:
            raise PermissionDenied

        form = self.get_form()
        if form.is_valid():
            canal=self.get_object()
            usuario=self.request.user
            mensaje=form.cleaned_data.get("mensaje")
            canal_obj=CanaldeMensaje.objects.create(canal=canal, usuario=usuario, texto=mensaje)


            if is_ajax:
                return JsonResponse({'mensaje': canal_obj.texto,
                'username':canal_obj.usuario.username}, status=201)
            return super().form_valid(form)
            
        else:
            if is_ajax:
                return JsonResponse({"Error":form.errors}, status=400)

            return super().form_invalid(form)

class DetalleCanal(DetailView, LoginRequiredMixin, CanalFormMixin):
    template_name="mensajes.html"
    queryset=Canal.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        obj = context['object']
        print(obj)

        if self.request.user not in obj.usuarios.all():
            raise PermissionDenied

        context['si_canal_miembro'] = self.request.user in obj.usuarios.all()
        return context




class DetalleDMs(DetailView, LoginRequiredMixin,CanalFormMixin):
      template_name="mensajes.html"
      def get_object(self, *args, **kwargs):

        username=self.kwargs.get("username")
        
        mi_username=self.request.user.username
        canal, _=Canal.objects.obtener_canal_dm(mi_username,username)

        if username == mi_username:
            mi_canal,_ =Canal.objects.obtener_canal_usuario_actual(self.request.user)
            print(mi_canal)
            return mi_canal

        
        if canal == None:
            return reverse_lazy('AppBlog:inicio')

        return canal

