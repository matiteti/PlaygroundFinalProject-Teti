from django import forms
from .models import Ingreso,Fruta,Carniceria,Panaderia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class Ingresoform(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = '__all__'

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

