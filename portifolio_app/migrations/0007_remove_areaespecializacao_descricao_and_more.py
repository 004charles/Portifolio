# Generated by Django 5.1.4 on 2024-12-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio_app', '0006_experienciaprofissional_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areaespecializacao',
            name='descricao',
        ),
        migrations.AddField(
            model_name='areaespecializacao',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
