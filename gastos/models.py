from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre=models.CharField(max_length=250, null=True,blank=True)
    cuil=models.CharField(max_length=250, null=True,blank=True)
    descripcion=models.CharField(max_length=250, null=True,blank=True)
    telefono=models.CharField(max_length=250, null=True,blank=True)
    direccion=models.CharField(max_length=250, null=True,blank=True)
    email=models.EmailField(max_length=254,blank=True,null=True)
    contratado = models.BooleanField(default=False)

    def __str__(self):
        return f"Servicio {self.descripcion} - {self.nombre}"



class Servicio(models.Model):
    nombre=models.CharField(max_length=250)
    descripcion=models.TextField()
    monto=models.DecimalField(default=10000,verbose_name='Monto del gasto',decimal_places=2,max_digits = 9)
    abonado=models.DecimalField(default=0,verbose_name='Monto abonado',decimal_places=2,max_digits = 9)
    fecha = models.DateField(verbose_name='Fecha de servicio')
    prestador = models.ForeignKey(to=Proveedor,on_delete=models.SET_NULL,null=True)
    pagado=models.BooleanField(default=False)
    
    @property
    def monto_pendiente(self):
        return self.monto-self.abonado 
    
    def __str__(self):
        return self.nombre
    