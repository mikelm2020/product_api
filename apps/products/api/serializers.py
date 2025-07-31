import locale
from decimal import Decimal

from rest_framework import serializers

from apps.products.models import Product

# try:
#     locale.setlocale(locale.LC_ALL, "es_MX.UTF-8")
# except locale.Error:
#     # Si la configuración regional no está disponible, se puede usar otra
#     # o manejar el error. En este caso, simplemente se imprime una advertencia.
#     print("Advertencia: No se pudo configurar la configuración regional 'es_MX.UTF-8'.")


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id"]

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que cero.")
        return value

    def validate_disponible(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError(
                "El campo 'disponible' debe ser un booleano."
            )
        return value

    def validate(self, attrs):
        if attrs.get("precio") is None and not attrs.get("disponible"):
            raise serializers.ValidationError(
                "Si el precio no se proporciona, el producto debe estar disponible."
            )
        return attrs

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id"]

    def to_representation(self, instance):
        """
        This method is responsible for modifying the representation of the data
        before it is sent in the API response.
        """
        # We get the default representation of the serializer
        representation = super().to_representation(instance)

        # We get the price, which in the model should be a Decimal
        precio = Decimal(representation["precio"])

        # Formatear el número manualmente para garantizar el separador de coma
        # Convertimos el Decimal a una cadena con 2 decimales
        precio_str = f"{precio:,.2f}"
        representation["precio"] = f"${precio_str}"

        return representation


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id"]

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que cero.")
        return value

    def validate_disponible(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError(
                "El campo 'disponible' debe ser un booleano."
            )
        return value

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.precio = validated_data.get("precio", instance.precio)
        instance.disponible = validated_data.get("disponible", instance.disponible)
        instance.save()
        return instance
