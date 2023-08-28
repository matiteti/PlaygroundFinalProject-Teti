from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('menu_inicio/', views.menu_inicio, name='menu_inicio'),
    path('leer_fruta/', views.leer_fruta, name='leer_fruta'),
    path('leer_carne/', views.leer_carne, name='leer_carne'),
    path('leer_panaderia/', views.leer_panaderia, name='leer_panaderia'),
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
    
    path('eliminar_carne/<carne_id>/', views.eliminar_carne, name='eliminar_carne'),
    path('editar_carne/<carne_id>/', views.editar_carne, name='editar_carne'),
    path('carne/lista', views.CarneListView.as_view(), name = "ListaCarne"),
    path('carne/nuevo', views.CarneCreateView.as_view(), name = "NuevaCarne"),
    path('carne/<pk>', views.CarneDetailView.as_view(), name = "DetalleCarne"),
    path('carne/<pk>/editar', views.CarneUpdateView.as_view(), name = "EditarCarne"),
    path('carne/<pk>/borrar', views.CarneDeleteView.as_view(), name = "BorrarCarne"),

    path('eliminar_pan/<pan_id>/', views.eliminar_pan, name='eliminar_pan'),
    path('editar_pan/<pan_id>/', views.editar_pan, name='editar_pan'),
    path('pan/lista', views.PanListView.as_view(), name = "ListaPan"),
    path('pan/nuevo', views.PanCreateView.as_view(), name = "NuevoPan"),
    path('pan/<pk>', views.PanDetailView.as_view(), name = "DetallePan"),
    path('pan/<pk>/editar', views.PanUpdateView.as_view(), name = "EditarPan"),
    path('pan/<pk>/borrar', views.PanDeleteView.as_view(), name = "BorrarPan"),
]