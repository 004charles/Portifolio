# Generated by Django 5.1.4 on 2024-12-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
