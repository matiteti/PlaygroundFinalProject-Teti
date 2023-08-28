from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('index/', views.index, name='index'),
    path('fruta/', views.fruta, name='fruta'),
    path('panaderia/', views.panaderia, name='panaderia'),
    path('carniceria/', views.carniceria, name='carniceria'),
    path('menu/', views.menu, name='menu'),
    path('intro/', views.intro, name='intro'),
    path('buscar-por-fruta/', views.buscar_fruta_por_id, name='buscar_fruta_por_id'),
    path('buscar-por-carne/', views.buscar_carne_por_id, name='buscar_carne_por_id'),
    path('buscar-por-pan/', views.buscar_pan_por_id, name='buscar_pan_por_id'),
    path('leer_fruta/', views.leer_fruta, name='leer_fruta'),
    path('eliminar_fruta/<fruta_id>/', views.eliminar_fruta, name='eliminar_fruta'),
    path('editar_fruta/<fruta_id>/', views.editar_fruta, name='editar_fruta'),
    path('leer_carne/', views.leer_carne, name='leer_carne'),
    path('eliminar_carne/<carne_id>/', views.eliminar_carne, name='eliminar_carne'),
    path('editar_carne/<carne_id>/', views.editar_carne, name='editar_carne'),
    path('leer_panaderia/', views.leer_panaderia, name='leer_panaderia'),
    path('eliminar_pan/<pan_id>/', views.eliminar_pan, name='eliminar_pan'),
    path('editar_pan/<pan_id>/', views.editar_pan, name='editar_pan'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    
]