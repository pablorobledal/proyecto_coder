from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    username=models.CharField(max_length=50, null=False,blank=True)
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




