from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Perfil(models.Model):
	user = models.OneToOneField(User, related_name='perfil_user')
	telefono = models.CharField(max_length=12)
	celular = models.CharField(max_length=12)
	seleccion_cargo= (('Doctor','Doctor'), ('Enfermera','Enfermera'), ('Interno','Interno'))
	cargo = models.CharField(max_length=12, choices=seleccion_cargo)
	nota = models.CharField(max_length=40)

	def crear_perfil(sender, instance, created, **kwargs):
		if created:
			Perfil.objects.create(user=instance)

	def guardar_perfil(sender, instance, **kwargs):
		instance.perfil.save()
