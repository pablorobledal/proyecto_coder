from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.apps import apps
import uuid
from django.db.models import Count

User=settings.AUTH_USER_MODEL

# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    username=models.CharField(max_length=50, null=False,blank=True)
    alias=models.CharField(max_length=50, null=False,blank=True)
    email=models.EmailField(max_length=100, null=False,blank=True)
    fecha_registro=models.DateTimeField(auto_now_add=True,auto_now=False, null=False,blank=True)
    bio=models.TextField(null=False,blank=True)
    avatar=models.ImageField(upload_to='avatares',default='avatares/default.jpg', null=False, blank=True)
    

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class ModeloBase(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    tiempo=models.DateTimeField(auto_now_add=True)
    actualizar=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CanaldeMensaje(ModeloBase):
    canal=models.ForeignKey("Canal", on_delete=models.CASCADE)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    texto=models.TextField()

class CanaldeUsuario(ModeloBase):
    canal=models.ForeignKey("Canal", null=True , on_delete=models.SET_NULL)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)


class CanalQuerySet(models.QuerySet):
    def solo_uno(self):
        return self.annotate(numero_usuarios=Count("usuarios")).filter(numero_usuarios=1)

    def solo_dos(self):
        return self.annotate(numero_usuarios=Count("usuarios")).filter(numero_usuarios=2)
    
    def filtrado_por_usuario(self, username):
        return self.filter(canaldeusuario__usuario__username=username)

 

class CanalManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return CanalQuerySet(self.model, using=self._db)
    
    def filtrar_por_privado(self, username_1, username_2):
        return self.get_queryset().solo_dos().filtrado_por_usuario(username_1).filtrado_por_usuario(username_2)

    def obtener_canal_usuario_actual(self, user):
        qs=self.get_queryset().solo_uno().filtrado_por_usuario(user.username)
        if qs.exists():
            return qs.order_by("tiempo").first, False
        
        canal_obj = Canal.objects.create()
        CanaldeUsuario.objects.create(usuario=user, canal=canal_obj)
        return canal_obj, True

    def obtener_canal_dm(self, username_1,username_2):
        qs=self.filtrar_por_privado(username_1,username_2)
        if qs.exists():

            return qs.order_by("tiempo").first(), False

        canal_obj = Canal.objects.create()
        Usuario=apps.get_model("auth", model_name='User')
        Canal_usuario_1=CanaldeUsuario(usuario=Usuario.objects.get(username=username_1), canal=canal_obj)
        Canal_usuario_2=CanaldeUsuario(usuario=Usuario.objects.get(username=username_2), canal=canal_obj)
        CanaldeUsuario.objects.bulk_create([Canal_usuario_1,Canal_usuario_2])
        return canal_obj, True
        
class Canal(ModeloBase):
    usuarios=models.ManyToManyField(User, blank=True, through=CanaldeUsuario)
    objects=CanalManager()




