from django.db import models

from propietarios.models import Lote

# Create your models here.

class Novedad(models.Model):
    nombre=models.CharField(max_length=250)
    descripcion=models.TextField()
    fecha = models.DateField(verbose_name='Fecha de servicio')

    def __str__(self):
        return self.nombre
    

class Votacion(models.Model):
    nombre=models.CharField(max_length=250)
    descripcion=models.TextField()
    fecha = models.DateField(verbose_name='Fecha de servicio')
    lote = models.ManyToManyField(Lote, verbose_name=("Lote"))
    voto= models.BooleanField(verbose_name="Voto a favor",default=False)
    def __str__(self):
        return self.nombre
    

class PersonaNoGrata(models.Model):
    nombre=models.CharField(max_length=250, null=True,blank=True)
    apellido= models.CharField(max_length=250, null=True,blank=True)
    telefono=models.CharField(max_length=250, null=True,blank=True)
    direccion=models.CharField(max_length=250, null=True,blank=True)
    email=models.EmailField(max_length=254,blank=True,null=True)
    dni=models.IntegerField(null=True,blank=True)
    patente = models.CharField(max_length=250, null=True,blank=True)
    
    def __str__(self):
        return self.nombre
    