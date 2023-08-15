from django.db import models
# Create your models here.

class Ingreso(models.Model):
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

class Fruta(models.Model):
    id = models.AutoField(primary_key=True)
    fruta = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    peso = models.CharField(max_length=100, default="0.0")   

    def __str__(self):
        return f"{self.id}"
  

class Carniceria(models.Model):
    id = models.AutoField(primary_key=True)
    carne = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    peso = models.CharField(max_length=100, default="0.0")

    def __str__(self):
        return f"{self.id}"

class Panaderia(models.Model):
    id = models.AutoField(primary_key=True)
    pan = models.CharField(max_length=100)
    cantidad = models.IntegerField()    
    peso = models.CharField(max_length=100, default="0.0") 
    def __str__(self):
        return f"{self.id}"