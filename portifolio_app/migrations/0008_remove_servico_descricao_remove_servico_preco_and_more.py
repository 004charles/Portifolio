# Generated by Django 5.1.4 on 2024-12-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio_app', '0007_remove_areaespecializacao_descricao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='preco',
        ),
        migrations.AddField(
            model_name='servico',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
