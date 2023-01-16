# Generated by Django 4.1.4 on 2023-01-14 19:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatares/'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='perfil',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
