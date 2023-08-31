from django import forms
from .models import Fruta,Carniceria,Panaderia, User, Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm




class Frutaform(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = ['fruta', 'cantidad', 'peso']

class Carniceriaform(forms.ModelForm):
    class Meta:
        model = Carniceria
        fields = ['carne', 'cantidad', 'peso']

class Panaderiaform(forms.ModelForm):
    class Meta:
        model = Panaderia
        fields = ['pan', 'cantidad', 'peso']

class BusquedaForm(forms.Form):
    nombre = forms.CharField(required=False)


class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'name', 'password1', 'password2')


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))


class UserEditForm(forms.ModelForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    name = forms.CharField(label="Nombre")
    imagen = forms.ImageField(label="Avatar", required=False)
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'imagen']  # Campos para editar
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    def save(self, commit=True):
        user = super().save(commit=False)
    
        avatar, _ = Avatar.objects.get_or_create(user=user)  # Usamos _ para ignorar el valor de created
        
        imagen = self.cleaned_data['imagen']
        
        if imagen:
            avatar.image = imagen
            avatar.save()
        
        if commit:
            user.save()
            
        return user





