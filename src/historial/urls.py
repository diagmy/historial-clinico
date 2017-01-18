"""historial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url, handler404, handler400
from django.contrib import admin

from cuenta.views import (login_view, register_view, logout_view, perfil_view)
from paciente.views import(paciente, nuevo_paciente,mostrar_pacientes,buscar_paciente, signos_vitales, otras_ordenes, medicamento,  handler400)
from inicio.views import index
from todo.views import reporte_estado, nuevo_item, borrar_tarea

handler400 = 'handler400'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^registro/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view,  name='logout'),
    url(r'^perfil/$', perfil_view, name='perfil'),
   # url(r'^editar_usuario/$', editar_usuario, name='editar_usuario'),
    url(r'^paciente/(?P<id>[0-9])/(?P<tab>[\w]+)/$', paciente, name='paciente'), #como poner el nuevo parametro aqui para identificar cada tab.. 
    url(r'^pacientelist/$', mostrar_pacientes, name='pacientelist'),
    url(r'^nuevo/$', nuevo_paciente, name='nuevo_paciente'),
    url(r'^buscar/$', buscar_paciente, name='buscar_paciente'),
    url(r'^signos-vitales/(?P<id>[0-9])/$', signos_vitales, name ='signos_vitales'),
    url(r'^medicamento/(?P<id>[0-9])/$', medicamento, name ='medicamento'),
    url(r'^otras/(?P<id>[0-9])/$', otras_ordenes, name ='otras_ordenes'),
    url(r'^reporte/$', reporte_estado, name= 'reporte_estado'),
    url(r'^item/$', nuevo_item, name= 'nuevo_item'),
    url(r'^borrar/(?P<id>\d+)/$',borrar_tarea, name ='borrar_tarea'),
]
 