from django.urls import path
from AppBlog.views import *


app_name = 'AppBlog'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('reglas/', reglas, name='reglas'),
    path('lotr', lotr, name='lotr'),
    path('mistborn/', mistborn, name='mistborn'),
    path('Narnia/', narnia, name='narnia'),
    path('got', got, name='got'),
    path('mensajes', mensajes, name='mensajes'),
    path('posts/', posts, name='posts'),
    path('crear_posteo', crear_posteo, name='crear_posteo'),
    path('editar_posteo/<pk>', editar_posteo.as_view(), name='editar_posteo'),
    path('borrar_posteo/<pk>', borrar_posteo.as_view(), name='borrar_posteo'),
    path('visitar_perfil/<username>',visitar_perfil, name='visitar_perfil'),
    path('visitar_posteo/<titulo>',visitar_posteo, name='visitar_posteo'),
    path('redireccionar',redireccionar, name='redireccionar'),
    path('resultado_busqueda', buscar, name='resultado_busqueda'),
    path('<universo>',visitar_universo, name='visitar_universo'),

]