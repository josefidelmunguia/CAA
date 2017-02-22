# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=10)),
                ('leyenda', models.CharField(max_length=50)),
                ('texto_alternatico', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_publicacion', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuarios')),
            ],
        ),
    ]
