from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('menu_inicio/', views.menu_inicio, name='menu_inicio'),
    path('leer_fruta/', views.leer_fruta, name='leer_fruta'),
    path('lista_carniceria/', views.lista_carniceria, name='lista_carniceria'),
    path('lista_panaderia/', views.lista_panaderia, name='lista_panaderia'),
    path('fruta/', views.fruta, name='fruta'),
    path('panaderia/', views.panaderia, name='panaderia'),
    path('carniceria/', views.carniceria, name='carniceria'),
    path('menu/', views.menu, name='menu'),
    path('intro/', views.intro, name='intro'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('buscar-por-fruta/', views.buscar_fruta_por_id, name='buscar_fruta_por_id'),
    path('buscar-por-carne/', views.buscar_carne_por_id, name='buscar_carne_por_id'),
    path('buscar-por-pan/', views.buscar_pan_por_id, name='buscar_pan_por_id'),
    path('eliminar_fruta/<fruta_id>/', views.eliminar_fruta, name='eliminar_fruta'),
    path('editar_fruta/<fruta_id>/', views.editar_fruta, name='editar_fruta'),
    path('fruta/lista', views.FrutaListView.as_view(), name = "ListaFruta"),
    path('fruta/nuevo', views.FrutaCreateView.as_view(), name = "NuevaFruta"),
    path('fruta/<pk>', views.FrutaDetailView.as_view(), name = "DetalleFruta"),
    path('fruta/<pk>/editar', views.FrutaUpdateView.as_view(), name = "EditarFruta"),
    path('fruta/<pk>/borrar', views.FrutaDeleteView.as_view(), name = "BorrarFruta"),
]