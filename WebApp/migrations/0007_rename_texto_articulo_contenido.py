# Generated by Django 4.2.5 on 2023-10-25 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_rename_contenido_articulo_texto_articulo_subtitulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='texto',
            new_name='contenido',
        ),
    ]
