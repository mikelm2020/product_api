from django.contrib import admin

from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "descripcion",
        "precio",
        "disponible",
    )
    search_fields = (
        "nombre",
        "precio",
        "disponible",
    )
    ordering = ("precio",)
    list_filter = (
        "disponible",
        "precio",
    )
