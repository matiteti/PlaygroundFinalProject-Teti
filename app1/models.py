from django.db import models
from django.contrib.auth.models import AbstractBaseUser,  PermissionsMixin, UserManager, User
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("El email esta mal")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=225, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]


class Fruta(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fruta = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    peso = models.CharField(max_length=100, default="0.0")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        fecha_hora_creacion = self.fecha_creacion.strftime("%d/%m/%Y %H:%M:%S")
        return f"{self.id} - {self.usuario} - Fecha de Creación: {fecha_hora_creacion}"

class Carniceria(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carne = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    peso = models.CharField(max_length=100, default="0.0")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        fecha_hora_creacion = self.fecha_creacion.strftime("%d/%m/%Y %H:%M:%S")
        return f"{self.id} - {self.usuario} - Fecha de Creación: {fecha_hora_creacion}"

class Panaderia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pan = models.CharField(max_length=100)
    cantidad = models.IntegerField()    
    peso = models.CharField(max_length=100, default="0.0") 
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        fecha_hora_creacion = self.fecha_creacion.strftime("%d/%m/%Y %H:%M:%S")
        return f"{self.id} - {self.usuario} - Fecha de Creación: {fecha_hora_creacion}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models. ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.image}"