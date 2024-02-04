from django.contrib import admin
from propietarios.models import Lote,Propietario,Multa

# Register your models here.

class MultaAdmin(admin.ModelAdmin):
    filter_horizontal=('afectados',)
admin.site.register(Lote)
admin.site.register(Propietario)
admin.site.register(Multa,MultaAdmin)