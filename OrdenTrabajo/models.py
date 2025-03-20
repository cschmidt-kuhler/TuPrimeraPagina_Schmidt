from django.db import models

# Create your models here.

class Herramienta(models.Model):
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serie = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} {self.modelo}"

class Operario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"

class OT(models.Model):
    nro_ot = models.IntegerField()
    cliente = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    terminado = models.BooleanField()

    def __str__(self):
        return self.cliente
