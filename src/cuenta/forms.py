from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from .models import Perfil 

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Clave')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
       
      
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Este usuario no existe")
            if not user.check_password(password):
                raise forms.ValidationError("Clave incorrecta")
            if not user.is_active:
                raise forms.ValidationError("Este usuario no esta activo.")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Correo Electronico')
    email2 = forms.EmailField(label='Reingresar Correo Electronico')
    password = forms.CharField(widget=forms.PasswordInput, label='Clave')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name',
            'email',
            'email2',
            'password'
        ]
        


    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Ambos correos deben coincidir")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Este correo ya ha sido registrado")
        return email

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefono', 'celular', 'cargo', 'nota']


