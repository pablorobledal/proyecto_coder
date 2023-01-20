from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Perfil

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user=User.objects.get(username=instance.username)

        Perfil.objects.create(user=instance, username= user.username, email=user.email, alias=user.username,  bio='Completa tu biografia')


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.perfil.save()
