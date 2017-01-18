from django.contrib import admin
from models import Perfil

class PerfilAdmin(admin.ModelAdmin):
	list_display = ("user","cargo", "telefono")
admin.site.register(Perfil,PerfilAdmin)
		
