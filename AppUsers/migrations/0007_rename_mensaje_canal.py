# Generated by Django 4.1.3 on 2023-01-19 23:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUsers', '0006_mensaje'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mensaje',
            new_name='Canal',
        ),
    ]
