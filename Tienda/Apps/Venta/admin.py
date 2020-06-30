from django.contrib import admin
from Tienda.Apps.Venta.models import *
# Register your models here.

from .models import Cliente, Producto, Venta


admin.site.site_url = None # null
admin.site.site_header = 'BOTICA AYALA'
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'ApellidoPaterno', 'ApellidoMaterno','Nombre','Dni','Sexo']
    list_display_links = ['ApellidoPaterno', 'ApellidoMaterno','Nombre','Dni']
    search_fields = ['ApellidoPaterno', 'ApellidoMaterno','Nombre','Dni']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'Descripcion','Presentacion','FechaVencimiento', 'Precio', 'Activo']
    search_fields = ['descripcion']

class DetalleVentaInline(admin.TabularInline):
    model = Venta.Productos.through
    autocomplete_fields = ['Producto']
    extra = 3

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['Cliente']
    inlines = [DetalleVentaInline]
    list_display_links = ['FechaVenta']
    list_filter = ['FechaVenta', 'Cliente']
    list_display = ['id', 'FechaVenta', 'Cliente', 'Total']
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        Total = 0
        Venta = form.instance
        for detalle in Venta.detalleventa_set.all():
            Total += detalle.Total
        Venta.Total = Total
        Venta.save()


