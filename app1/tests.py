from django.test import TestCase, Client

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from models import Fruta, Avatar


### Test con el models Fruta ###
class FrutaTestCase(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.usuario = User.objects.create_user(username='Test1', password='12345678')
        
        # Crea una instancia de Fruta para las pruebas
        self.fruta = Fruta.objects.create(
            usuario=self.usuario,
            fruta='Manzana',
            cantidad=5,
            peso='1.5 kg'
        )

    def test_str_method(self):
        # Verifica que el método __str__ del modelo Fruta funcione correctamente
        expected_str = f"{self.fruta.id} - {self.usuario} - Fecha de Creación: {self.fruta.fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')}"
        self.assertEqual(str(self.fruta), expected_str)

    def test_fruta_attributes(self):
        # Verifica que los atributos de la instancia de Fruta sean correctos
        self.assertEqual(self.fruta.usuario, self.usuario)
        self.assertEqual(self.fruta.fruta, 'Manzana')
        self.assertEqual(self.fruta.cantidad, 5)
        self.assertEqual(self.fruta.peso, '1.5 kg')



### Test con el models User ###

class UserTestCase(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.user = get_user_model().objects.create_user(
            email='coder@gmail.com',
            password='12345678',
            name='Test2'
        )

    def test_str_method(self):
        # Verifica que el método __str__ del modelo User funcione correctamente
        expected_str = f"{self.user.email} - {self.user.name}"
        self.assertEqual(str(self.user), expected_str)

    def test_user_attributes(self):
        # Verifica los atributos del usuario
        self.assertEqual(self.user.email, 'coder@gmail.com')
        self.assertEqual(self.user.name, 'Coder Test')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)
        self.assertEqual(self.user.date_joined.date(), timezone.now().date())



### Test con el models Avatar ###
class AvatarTestCase(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.user = get_user_model().objects.create_user(
            email='coder2@gmail.com',
            password='12345678',
            name='Test3'
        )

        # Crea una instancia de Avatar para las pruebas
        self.avatar = Avatar.objects.create(
            user=self.user,
            image='avatares/test_avatar.png'  # Ruta ficticia a una imagen de avatar
        )

    def test_str_method(self):
        # Verifica que el método __str__ del modelo Avatar funcione correctamente
        expected_str = f"{self.user} - {self.avatar.image}"
        self.assertEqual(str(self.avatar), expected_str)

    def test_avatar_attributes(self):
        # Verifica los atributos del avatar
        self.assertEqual(self.avatar.user, self.user)
        self.assertEqual(self.avatar.image, 'avatares/test_avatar.png')  # Verifica la ruta de la imagen