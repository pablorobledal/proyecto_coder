from django.urls import path, re_path
from AppUsers.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'AppUsers'
UUID_CANAL_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'

urlpatterns = [
    path('registro', registro, name='registro'),
    path('login', logear, name='iniciar_sesion'),
    path('logout', cerrar_sesion, name="cerrar_sesion"),
    path('editar_perfil/<pk>', editar_perfil.as_view(), name='editar_usuario'),
    path('borrar_usuario/<pk>', borrar_perfil.as_view(), name='borrar_usuario'),
    path('perfil/<username>', miperfil, name='mi_perfil'),
    path('editar_contraseña/<pk>', editar_contraseña.as_view(), name='editar_contraseña'),
    path('mensajes/<username>', DMs, name='DMs'),
    path('detalledms/<username>', DetalleDMs.as_view(), name="detalledms"),
    re_path(UUID_CANAL_REGEX,DetalleCanal.as_view(), name="detallecanal"),
    path('buzon', Buzon.as_view(),name="buzon"),
    path('usuarios',obtener_usuarios,name="obtenerusuarios"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

