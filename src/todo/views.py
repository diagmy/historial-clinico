from django.shortcuts import render, render_to_response, redirect, get_object_or_404, HttpResponse
from .models import Item
from .forms import ToDoForm

from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy


 

# Create your views here.
@login_required(login_url='/login/')
def nuevo_item(request): #cambiar luego por nueva_tarea

	form = ToDoForm()
	if request.method == "POST":
		form = ToDoForm(request.POST)
		if form.is_valid():
			item_nuevo = form.save(commit=False)
			item_nuevo.save()
			return redirect('/')
			form.save()
	return render(request,"form.html", {"form": form, 'title_1': "Ingresar", 'title': "Agregar Tarea"})

def reporte_estado(request):
	
	return render(request,"index.html",{'items': Item.objects.all(), 'title': "Panel"} )

def borrar_tarea(request, id):
	item = get_object_or_404(Item,pk=id)
	item.delete()
	return redirect('/')
	# return HttpResponse("Deleted!")


