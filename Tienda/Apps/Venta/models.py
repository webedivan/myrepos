from django.db import models

# Create your models here.
class Cliente (models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=35)
    Dni = models.CharField('DNI',max_length=8)
    SEXOS =(('M','Masculino'),('F','Femenino'))
    Sexo = models.CharField(max_length=1,choices=SEXOS,default='M')
    def __str__(self):
        return f'{self.ApellidoPaterno.upper()} {self.ApellidoMaterno.upper()}, {self.Nombre}'

class Producto (models.Model):
    Descripcion = models.CharField('descripcion',max_length=50)
    Presentacion = models.CharField(max_length=35)
    FechaVencimiento = models.DateTimeField()
    Precio = models.DecimalField(max_digits=6 ,decimal_places=2)
    Activo = models.BooleanField(default=True)
    Stock  = models.PositiveIntegerField
    def __str__(self):
        return f'{self.Descripcion}'

class Venta(models.Model):
    FechaVenta =models.DateTimeField(auto_now=True)
    Cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    Total = models.DecimalField(max_digits=9 ,decimal_places=2, null=True, blank=True)
    Productos = models.ManyToManyField(Producto, through='DetalleVenta')
    def __str__(self):
        return f'Venta{self.id}, Total{self.Total}'
class DetalleVenta(models.Model):
    Venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    Producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    Cantidad = models.IntegerField()
    Total = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    def save(self, *args, **kwargs):
        self.Total = self.Cantidad * self.Producto.Precio
        super().save(*args, **kwargs)
