
from django import forms
from .models import Paciente, Signos_Vitales, Medicamento, Otras_Ordenes_Terapeuticas


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'edad', 'sexo', 'peso', 'direccion', 'telefono', 'celular' )


class SignosVitalesForm(forms.ModelForm):
    class Meta:
        model = Signos_Vitales
        fields = ('tension_arterial', 'temperatura', 'frecuencia_cardiaca', 'frecuencia_respiratoria', 'notas' )


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ('nombre', 'tipo', 'dosis', 'frecuencia', 'via', 'nota')
       
      
class OtrasOrdenesForm(forms.ModelForm):
    class Meta:
        model = Otras_Ordenes_Terapeuticas
        fields = ('dieta', 'actividad_fisica', 'curas', 'oxigeno', 'fisioterapia_respiratoria', 'sondas_drenajes', 'estudios_lab_diagnostico' )


 


# from django import forms
# from django.forms import ModelForm
# from django.contrib.auth.forms import User
# from .models import Patient, UserInfo, MedicalInfo, ProfileInfo, Prescription, MedTest, Appointment


# class LoginForm(forms.Form):
#     username = forms.CharField(label="Username", max_length=50)
#     password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)


# class BaseUserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')


# class AppointmentForm(forms.Form):
#     doctor = forms.CharField(max_length=50)
#     date = forms.CharField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     time = forms.CharField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
#     description = forms.CharField(max_length=200)

#     class Meta:
#         model = Appointment
#         fields = (
#             'doctor',
#             'userName',
#             'date',
#             'time',
#             'description'
#         )

#     def __init__ (self, *args, **kwargs):
#         super(AppointmentForm, self).__init__(*args, **kwargs)
#         self.fields['date'].widget.attrs['value'] = '2015-03-14'


# class UserForm(ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = (
#             'policyNumber',
#             'provider',
#             'groupNumber',
#         )


# class ProfileForm(ModelForm):
#     class Meta:
#         model = ProfileInfo
#         fields = (
#             'firstName',
#             'middleName',
#             'lastName',
#             'address',
#             'city',
#             'state',
#             'dateOfBirth',
#             'zipcode',
#             'phoneNumber',
#             'email',
#             'eName',
#             'ePhoneNumber',
#         )


# class MedicalForm(ModelForm):
#     class Meta:
#         model = MedicalInfo

#         # TODO - add cancer/diabetes
#         fields = (
#             'allergies',
#             'anemia',
#             'arthritis',
#             'chickenpox',
#             'coxsackie',
#             'diphtheria',
#             'epilepsy',
#             'frequentColds',
#             'germanMeasles',
#             'highBloodPressure',
#             'influenza',
#             'kidneyDisease',
#             'measles',
#             'migraines',
#             'mumps',
#             'obesity',
#             'pneumonia',
#             'polio',
#             'rheumaticFever',
#             'scarlatina',
#             'scarletFever',
#             'strokes',
#             'syphilis',
#             'tonsillitis',
#             'tuberculosis',
#             'whoopingCough',
#         )


# class MedTestForm(ModelForm):
#     class Meta:
#         model = MedTest
#         fields = (
#             'name',
#             'doctor',
#             'released',
#             'dateIssued',
#             'result',
#         )



# """