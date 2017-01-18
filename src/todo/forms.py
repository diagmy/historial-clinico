from django import forms
from .models import  Item
from django.utils.translation import ugettext_lazy as _

class ToDoForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('titulo', 'fecha_vencimiento', 'prioridad', 'nota' )
   


