# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20170131_1459'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Categoria_Producto',
        ),
        migrations.RenameModel(
            old_name='Etiqueta',
            new_name='Etiqueta_Producto',
        ),
    ]
