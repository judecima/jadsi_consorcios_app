# admin.py
from django.contrib import admin
from .models import Lote, ExpensaMensual, Expensa
from .actions import generar_expensas

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    pass

@admin.register(ExpensaMensual)
class GastoAdmin(admin.ModelAdmin):
    pass

@admin.register(Expensa)
class ExpensaAdmin(admin.ModelAdmin):
    list_display = ('lote', 'mes', 'monto_a_pagar', 'pagado')
    actions = [generar_expensas]

