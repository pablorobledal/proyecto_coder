from django.urls import path
from AppUsers.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'AppUsers'

urlpatterns = [
    path('registro', registro, name='registro'),
    path('login', logear, name='iniciar_sesion'),
    path('logout', cerrar_sesion, name="cerrar_sesion"),
    path('editar_perfil/<pk>', editar_perfil.as_view(), name='editar_usuario'),
    path('borrar_usuario/<pk>', borrar_perfil.as_view(), name='borrar_usuario'),
    path('perfil/<username>', miperfil, name='mi_perfil'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

