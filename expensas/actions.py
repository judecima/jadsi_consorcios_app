# actions.py
from django.db.models import Sum
from django.utils import timezone
from .models import Expensa, ExpensaMensual, Lote

def generar_expensas(modeladmin, request, queryset):
    # Obtener el mes actual
    mes_actual = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # Obtener la suma de los gastos para el mes actual
    gastos_mes_actual = ExpensaMensual.objects.filter(fecha__month=mes_actual.month).aggregate(Sum('monto'))['monto__sum'] or 0

    # Obtener la cantidad de lotes
    cantidad_lotes = Lote.objects.count()

    # Calcular el monto a pagar por cada lote
    monto_por_lote = gastos_mes_actual / cantidad_lotes

    # Crear una Expensa para cada lote
    for lote in Lote.objects.all():
        Expensa.objects.update_or_create(
            lote=lote,
            mes=mes_actual,
            defaults={'monto_a_pagar': monto_por_lote}
        )

    modeladmin.message_user(request, f"Se generaron las expensas para el mes {mes_actual.month}.", messages.SUCCESS)

generar_expensas.short_description = "Generar Expensas para el Mes Actual"
