from django_filters import rest_framework as filters

from apps.products.models import Product


class ProductFilterSet(filters.FilterSet):
    nombre_is_like = filters.CharFilter(field_name="nombre", lookup_expr="contains")
    precio_min = filters.NumberFilter(field_name="precio", lookup_expr="gte")
    precio_max = filters.NumberFilter(field_name="precio", lookup_expr="lte")

    class Meta:
        model = Product
        fields = (
            "precio",
            "disponible",
        )
