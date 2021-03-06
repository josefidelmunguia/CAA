# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0003_auto_20170131_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='img/sliders')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sliders.Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
    ]
