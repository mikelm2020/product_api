from django_filters import rest_framework as filters

from apps.products.models import Product


class ProductFilterSet(filters.FilterSet):
    nombre_is_like = filters.CharFilter(field_name="nombre", lookup_expr="contains")

    class Meta:
        model = Product
        fields = (
            "precio",
            "disponible",
        )
