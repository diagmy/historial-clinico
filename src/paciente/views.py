from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import *
from .forms import PacienteForm, SignosVitalesForm, MedicamentoForm, OtrasOrdenesForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext 
 

# Create your views here.
@ensure_csrf_cookie
@login_required(login_url='/login/')
def nuevo_paciente(request):
	
	form = PacienteForm()
	if request.method == "POST":
		form = PacienteForm(request.POST)
		if form.is_valid():
		
			messages.success(request, "Nuevo paciente agregado.")
			form.save()
	return render(request,"form.html", {"form": form, 'title_1': "Ingresar", 'title': "Agregar paciente"})

@login_required(login_url='/login/')
def index(request):
  	patient_list = Paciente.objects.order_by("nombre")
  	context = {"patient_list": patient_list}
  	return render(request, "index.html", context)

@login_required(login_url='/login/')
def paciente(request, id, tab):
	form_list = [(SignosVitalesForm, "signos_vitales"),
				 (MedicamentoForm, "medicamento"),
				 (OtrasOrdenesForm, "otras_ordenes")]
	paciente = get_object_or_404(Paciente, pk=id)
	signos_vitales = Signos_Vitales.objects.filter(paciente=id)
	medicamentos = Medicamento.objects.filter(paciente=id)
	otras_ordenes = Otras_Ordenes_Terapeuticas.objects.filter(paciente=id)
	return render(request, "paciente/paciente.html", {"paciente": paciente, 
													  "signos_vitales": signos_vitales,
													  "medicamentos": medicamentos,
													  "otras_ordenes": otras_ordenes,
													  "active_tab":tab,
													  "form_list": form_list})
													   #aqui quiero poner el nombre de tab 
	#return render(request,"paciente/paciente.html", {'paciente': paciente, 'id': id})

@login_required(login_url='/login/')
def mostrar_pacientes(request):
	return render(request,"paciente/pacienteslist.html",{'pacientes': Paciente.objects.all(), 'title': "Pacientes"} )

@login_required(login_url='/login/')
def buscar_paciente(request):
	q=request.GET.get("q")
	pacientes = Paciente.objects.filter(nombre__contains = q)

	if q:
		return render(request,"paciente/buscar_paciente.html",{'q': q, 'pacientes': pacientes})

@login_required(login_url='/login/')
def signos_vitales(request, id):
	paciente_obj = Paciente.objects.get(id=id)
	form = SignosVitalesForm()
	if request.method == "POST":
		form = SignosVitalesForm(request.POST)
		if form.is_valid():
			signo_nuevo = form.save(commit=False)
			signo_nuevo.paciente = paciente_obj
			signo_nuevo.save()
			return redirect('paciente', id= id, tab="signos_vitales_tab")
        	
			# messages.success(request, "Signos vitales agregados.")
	# return render(request,"form.html", {"form": form, 'title_1': "Agregar", 'title': "Signos Vitales" })

@login_required(login_url='/login/')
def medicamento(request, id):
	paciente_obj = Paciente.objects.get(id=id)
	import logging
	logging.error(paciente_obj)
	form = MedicamentoForm()
	if request.method == "POST":
		form = MedicamentoForm(request.POST)
		if form.is_valid():
			medicamento_nuevo = form.save(commit=False)
			medicamento_nuevo.paciente = paciente_obj
			medicamento_nuevo.save()
			return redirect('paciente', id= id, tab='medicamentos_tab')
			# messages.success(request, "Medicamento agregado.")
	# return render(request,"form.html", {"form": form, 'title_1': "Agregar", 'title': "Medicamentos"})
@login_required(login_url='/login/')
def otras_ordenes(request, id):
	paciente_obj = Paciente.objects.get(id=id)
	import logging
	logging.error(paciente_obj)

	form = OtrasOrdenesForm()
	if request.method == "POST":
		form = OtrasOrdenesForm(request.POST)
		if form.is_valid():
			otras_ordenes_nuevo = form.save(commit=False)
			otras_ordenes_nuevo.paciente = paciente_obj
			otras_ordenes_nuevo.save()
			return redirect('paciente', id= id, tab="otras_ordenes_tab")
			# messages.success(request, "Datos agregados.")
	# return render(request,"form.html", {"form": form, 'title_1': "Agregar", 'title': "Otras Ordenes Terapeuticas"})




def handler400(request):
	response = render_to_response('404.html', {}, context_instance = RequestContext(request))
	response.status_code = 404
	return response


	
