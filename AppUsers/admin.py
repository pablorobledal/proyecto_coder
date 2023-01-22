from django.contrib import admin
from .models import *

class CanalMensajeInLine(admin.TabularInline):
    model = CanaldeMensaje
    extra = 1

class CanalUsuarioInLine(admin.TabularInline):
    model = CanaldeUsuario
    extra = 1

class CanalAdmin(admin.ModelAdmin):
    inlines = [CanalMensajeInLine, CanalUsuarioInLine]

    class Meta:
        model = Canal

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Canal, CanalAdmin)
admin.site.register(CanaldeMensaje)
admin.site.register(CanaldeUsuario)