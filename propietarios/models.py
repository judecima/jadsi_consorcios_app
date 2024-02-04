from django.db import models
from django.core.validators import RegexValidator
    

class Propietario(models.Model):
    nombre=models.CharField(max_length=250, null=True,blank=True)
    apellido= models.CharField(max_length=250, null=True,blank=True)
    telefono=models.CharField(max_length=10, null=True,blank=True,validators=[
            RegexValidator(r'^\d{10}$','Solo se permiten ingresar nros.'
            ),
        ],)
    direccion=models.CharField(max_length=250, null=True,blank=True)
    email=models.EmailField(max_length=254,blank=True,null=True)
    
    def __str__(self):
        return self.nombre


class Lote(models.Model):
    nro_lote = models.IntegerField(unique=True,null=True,blank=True)
    seccion = models.CharField(max_length=250, null=True,blank=True)
    construccion=models.BooleanField(default=False)
    aguado=models.BooleanField(default=False)
    agua=models.BooleanField(default=False)
    electricidad=models.BooleanField(default=False)
    Propietario = models.ForeignKey(to=Propietario,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return f'Lote Nro: {self.nro_lote}'
    
class Multa(models.Model):
    nombre=models.CharField(max_length=250, null=True,blank=True)
    descripcion=models.TextField(max_length=250, null=True,blank=True)
    Propietario = models.ForeignKey(to=Propietario,on_delete=models.SET_NULL,null=True)
    afectados = models.ManyToManyField(to='Propietario',related_name='afectados_multas')
    Resolucion=models.TextField(max_length=250, null=True,blank=True)
    Monto = models.DecimalField(default=10000,verbose_name='Monto de multa',decimal_places=2,max_digits = 8)
    def __str__(self):
        return self.nombre