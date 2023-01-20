# Generated by Django 4.1.3 on 2023-01-20 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUsers', '0007_rename_mensaje_canal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canal',
            name='texto',
        ),
        migrations.RemoveField(
            model_name='canal',
            name='usuario',
        ),
        migrations.CreateModel(
            name='CanaldeUsuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
                ('canal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppUsers.canal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanaldeMensaje',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
                ('texto', models.TextField()),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsers.canal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='canal',
            name='usuarios',
            field=models.ManyToManyField(blank=True, through='AppUsers.CanaldeUsuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
