from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from gastos.models import Proveedor,Servicio

# Register your models here.

class ServicioAdminForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'fecha': AdminDateWidget(),
        }


class ServicioAdmin(admin.ModelAdmin):
    list_display=("__str__","abonado",'monto_pendiente')
    form = ServicioAdminForm
    list_filter=('pagado',)

admin.site.register(Proveedor)
admin.site.register(Servicio,ServicioAdmin)

