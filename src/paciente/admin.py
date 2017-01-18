from django.contrib import admin

# Register your models here.
from models import Paciente, Signos_Vitales, Medicamento, Otras_Ordenes_Terapeuticas

class PacienteAdmin(admin.ModelAdmin):
	list_display = ("nombre","telefono")
admin.site.register(Paciente,PacienteAdmin)
		
class SignosVitalesAdmin(admin.ModelAdmin):
	list_display = ("paciente", "notas")

admin.site.register(Signos_Vitales, SignosVitalesAdmin)

class MedicamentoAdmin(admin.ModelAdmin):
	list_display = ("paciente", "nombre")

admin.site.register(Medicamento, MedicamentoAdmin)

class OtrasOrdenesAdmin(admin.ModelAdmin):
	list_display = ("paciente", "fecha", "hora")

admin.site.register(Otras_Ordenes_Terapeuticas, OtrasOrdenesAdmin)