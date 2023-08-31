from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index, name='index'),
    path('fruta/', views.fruta, name='fruta'),
    path('panaderia/', views.panaderia, name='panaderia'),
    path('carniceria/', views.carniceria, name='carniceria'),
    path('leer_fruta/', views.leer_fruta, name='leer_fruta'),
    path('eliminar_fruta/<fruta_id>/', views.eliminar_fruta, name='eliminar_fruta'),
    path('editar_fruta/<fruta_id>/', views.editar_fruta, name='editar_fruta'),
    path('leer_carne/', views.leer_carne, name='leer_carne'),
    path('eliminar_carne/<carne_id>/', views.eliminar_carne, name='eliminar_carne'),
    path('editar_carne/<carne_id>/', views.editar_carne, name='editar_carne'),
    path('leer_panaderia/', views.leer_panaderia, name='leer_panaderia'),
    path('eliminar_pan/<pan_id>/', views.eliminar_pan, name='eliminar_pan'),
    path('editar_pan/<pan_id>/', views.editar_pan, name='editar_pan'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_request, name='login'),
    path('acerca/', views.acerca, name='acerca'), 
    path('compras/', views.compras, name='compras'), 
    path('editarperfil/', views.editarPerfil, name='editarperfil'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)