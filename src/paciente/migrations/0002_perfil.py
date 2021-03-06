# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-29 19:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=12)),
                ('celular', models.CharField(max_length=12)),
                ('cargo', models.CharField(choices=[(b'Doctor', b'Doctor'), (b'Enfermera', b'Enfermera'), (b'Interno', b'Interno')], max_length=12)),
                ('nota', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
