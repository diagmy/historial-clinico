# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 16:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('fecha_creada', models.DateTimeField(default=datetime.datetime.now)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('fecha_completada', models.DateField(blank=True, null=True)),
                ('prioridad', models.IntegerField(choices=[(1, 'Baja'), (2, 'Normal'), (3, 'Alta')], default=2)),
                ('completado', models.BooleanField(default=False)),
                ('nota', models.TextField(blank=True, null=True)),
                ('asignado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_asignado_por', to=settings.AUTH_USER_MODEL)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_creado_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-prioridad', 'titulo'],
            },
        ),
    ]
