from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
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
    paginaweb=models.URLField(max_length=200, null=False,blank=True)

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
        return self.annotate(numero_usuarios=Count("usuarios").filter(numero_usuarios=1))

    def solo_dos_u(self):
        return self.annotate(numero_usuarios=Count("usuarios").filter(numero_usuarios=2))


class CanalManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return CanalQuerySet(self.model, using=self._db)


class Canal(ModeloBase):
    usuarios=models.ManyToManyField(User, blank=True, through=CanaldeUsuario)
    objects=CanalManager()




