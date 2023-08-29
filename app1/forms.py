from django import forms
from .models import Fruta,Carniceria,Panaderia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class Frutaform(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = '__all__'

class Carniceriaform(forms.ModelForm):
    class Meta:
        model = Carniceria
        fields = '__all__'

class Panaderiaform(forms.ModelForm):
    class Meta:
        model = Panaderia
        fields = '__all__'

class BusquedaForm(forms.Form):
    nombre = forms.CharField(required=False)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields 

class CustomLoginForm(AuthenticationForm):
    pass

class CustomUserRegistrationForm(forms.Form):
    usuario = forms.EmailField()
    clave = forms.CharField(widget=forms.PasswordInput)
