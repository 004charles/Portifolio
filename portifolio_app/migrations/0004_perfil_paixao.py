# Generated by Django 5.1.4 on 2024-12-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio_app', '0003_remove_perfil_paixao_remove_perfil_um'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='paixao',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
