from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime 

# Create your models here.


 

SELECCION_PRIORIDAD = ( 

  (1, 'Baja'), 

  (2, 'Normal'), 

  (3, 'Alta'), 

) 

 

class Item(models.Model): 

  titulo = models.CharField(max_length=250) 
  fecha_creada = models.DateTimeField(default=datetime.datetime.now) 
  fecha_vencimiento = models.DateField(blank=True, null=True, )
  fecha_completada = models.DateField(blank=True, null=True)
  prioridad = models.IntegerField(choices=SELECCION_PRIORIDAD, default=2) 
  completado = models.BooleanField(default=False) 

  creado_por = models.ForeignKey(User, related_name='todo_creado_por', blank= True, null= True)
  asignado_por = models.ForeignKey(User, blank=True, null=True, related_name='todo_asignado_por')
  nota = models.TextField(blank=True, null=True)

  def __str__(self): 

    return self.titulo 

  class Meta: 

    ordering = ['-prioridad', 'titulo'] 

  class Admin: 

    pass