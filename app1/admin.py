from django.contrib import admin
from .models import  Fruta, Carniceria, Panaderia, User, Avatar

admin.site.register(Fruta)
admin.site.register(Carniceria)
admin.site.register(Panaderia)
admin.site.register(User)
admin.site.register(Avatar)

# Register your models here.