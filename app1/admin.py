from django.contrib import admin
from .models import  Fruta,Carniceria,Panaderia,Usuario

admin.site.register(Usuario)
admin.site.register(Fruta)
admin.site.register(Carniceria)
admin.site.register(Panaderia)

# Register your models here.