from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

# Create your models here.
class Posteo(models.Model):
    username=models.CharField(max_length=40, blank=True, null=True)
    #Datos del autor del POST
    autor = models.CharField(max_length=40, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, null=True, blank=True)
    #Informacion del posteo
    titulo = models.CharField(primary_key=True, max_length=40)
    universo = models.CharField(max_length=40, blank=True, null=True, choices=[('LotR','Lord of the Rings'),('Narnia' ,'Narnia'),('Mistborn', 'Mistborn'),('GoT', 'Game of Thrones'),('Otros','Otros')])
    cuerpo = models.TextField(max_length=10**10, null=True, blank=True)
    imagen = models.ImageField(upload_to='posts', null=False, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    
    def __str__(self) -> str:
        return f'{self.titulo} | {self.autor} | {self.username}'

class Comment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comment_author')
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.CharField(max_length=100)
 
    def __str__(self) -> str:
        return f'{self.usuario} | {self.post}'