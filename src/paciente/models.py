from django.db import models 
from django.conf import settings
from datetime import datetime


class Paciente(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    edad = models.IntegerField()
    seleccion_sexo= (('M', 'Masculino'), ('F', 'Femenino'))
    sexo = models.CharField(max_length=1, choices=seleccion_sexo)
    peso = models.FloatField(max_length=5)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    celular = models.CharField(max_length=12)
    fecha_ingreso = models.DateField(auto_now_add=True, blank=False)

    def __str__(self):
    	return self.nombre

    def get_url(self):
    	return '/paciente/{0}/{0}'.format(self.id)


class Signos_Vitales(models.Model):
	fecha = models.DateField(auto_now_add=True)
	hora = models.TimeField(auto_now_add=True)
	tension_arterial = models.CharField(max_length=20)
	frecuencia_cardiaca = models.CharField(max_length=20)
	frecuencia_respiratoria = models.CharField(max_length=20)
	temperatura = models.CharField(max_length=20)
	notas = models.CharField(max_length=100)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)



class Medicamento(models.Model):

	nombre = models.CharField(max_length=30)
	tipo = models.CharField(max_length=20)
	dosis = models.CharField(max_length=40)
	frecuencia = models.CharField(max_length=30)
	via = models.CharField(max_length=20)
	nota = models.CharField(max_length=40)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Otras_Ordenes_Terapeuticas(models.Model):
	fecha = models.DateField(auto_now_add=True)
	hora = models.TimeField(auto_now_add=True)
	dieta = models.CharField(max_length=60)
	actividad_fisica = models.CharField(max_length=30)
	curas = models.CharField(max_length=30)
	oxigeno = models.CharField(max_length=20)
	fisioterapia_respiratoria = models.CharField(max_length=20)
	sondas_drenajes = models.CharField(max_length=20)
	estudios_lab_diagnostico = models.CharField(max_length=60)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


# class Evolucion(models.Model):
# 	fecha = models.DateField(auto_now_add=True)
# 	hora = models.TimeField(auto_now_add=True)
# 	notas = models.CharField(max_length=200)
# 	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)





# class Seguro(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	numero_afiliado = models.CharField(max_length=20)


