from django import forms
from .models import Ingreso,Fruta,Carniceria,Panaderia

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
    id = forms.CharField(required=False)
