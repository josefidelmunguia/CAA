# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0006_auto_20170206_0850'),
        ('entradas', '0004_auto_20170206_0850'),
        ('paginas', '0002_auto_20170131_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=35)),
                ('enlace_personalizado', models.CharField(max_length=35)),
                ('categoria_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entradas.Categoria_Entrada')),
                ('categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Categoria_Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='enlace',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enlaces.Menu'),
        ),
        migrations.AddField(
            model_name='enlace',
            name='pagina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.Pagina'),
        ),
    ]
