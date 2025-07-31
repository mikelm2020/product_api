from django.db import models


class Product(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
