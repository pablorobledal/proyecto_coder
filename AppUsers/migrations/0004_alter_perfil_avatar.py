# Generated by Django 4.1.4 on 2023-01-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsers', '0003_alter_perfil_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, default='avatares/default.jpg', upload_to='avatares'),
        ),
    ]
