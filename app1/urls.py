from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('menu_inicio/', views.menu_inicio, name='menu_inicio'),
    path('lista_fruta/', views.lista_fruta, name='lista_fruta'),
    path('lista_carniceria/', views.lista_carniceria, name='lista_carniceria'),
    path('lista_panaderia/', views.lista_panaderia, name='lista_panaderia'),
    path('fruta/', views.fruta, name='fruta'),
    path('panaderia/', views.panaderia, name='panaderia'),
    path('carniceria/', views.carniceria, name='carniceria'),
    path('menu/', views.menu, name='menu'),
    path('intro/', views.intro, name='intro'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('buscar_cursos_por_id-por-id/', views.buscar_cursos_por_id, name='buscar_cursos_por_id'),
]