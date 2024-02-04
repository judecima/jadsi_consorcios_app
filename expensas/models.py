# models.py
from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _

class Lote(models.Model):
    nombre = models.CharField(max_length=100)
    numero_lote = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class ExpensaMensual(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)



class Expensa(models.Model):
    monto_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE)
    mes = models.DateField(_("Mes de la Expensa"), default=date.today)

    def __str__(self):
        return f"Expensa para {self.lote.nombre} - {self.mes}"
