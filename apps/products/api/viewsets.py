from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django_filters import rest_framework
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from apps.products.api.serializers import (
    CreateProductSerializer,
    ListProductSerializer,
    UpdateProductSerializer,
)
from apps.products.filters import ProductFilterSet
from apps.products.models import Product
from apps.products.pagination import ExtendedPagination


@extend_schema_view(
    list=extend_schema(operation_id="list"),
    retrieve=extend_schema(operation_id="retrieve"),
)
class ProductViewSet(viewsets.GenericViewSet):
    serializer_class = CreateProductSerializer
    list_serializer_class = ListProductSerializer
    queryset = Product.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        rest_framework.DjangoFilterBackend,
    ]
    filterset_class = ProductFilterSet
    search_fields = ("nombre", "precio", "disponible")
    ordering_fields = (
        "nombre",
        "precio",
    )
    pagination_class = ExtendedPagination

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

        # if self.queryset is None:
        # self.queryset = self.serializer_class.Meta.model.objects.filter(
        #     disponible=True
        # )
        # self.queryset = Product.objects.all()
        # return self.queryset

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)

    @extend_schema(
        request=ListProductSerializer,
        parameters=[
            OpenApiParameter(
                name="ordering",
                location=OpenApiParameter.QUERY,
                description="The fields can you use for ordering the results is: nombre and precio",
            ),
            OpenApiParameter(
                name="search",
                location=OpenApiParameter.QUERY,
                description="The field can you use for search is: nombre, precio and disponible",
            ),
        ],
        examples=[
            OpenApiExample(
                "Example 1",
                description="Request to product",
                value={
                    "nombre": "string",
                    "descripcion": "string",
                    "precio": 0,
                    "disponible": True,
                },
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        """
        Get a collection of Products
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=CreateProductSerializer,
        responses={201: None},
        examples=[
            OpenApiExample(
                "Example 1",
                description="Request to product",
                value={
                    "nombre": "string",
                    "descripcion": "string",
                    "precio": 0,
                    "disponible": True,
                },
            ),
        ],
    )
    def create(self, request):
        """
        Create an product
        """
        product_serializer = self.serializer_class(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(
                {"message": "El producto se creo correctamente!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "message": "Hay errores en el registro!",
                "errors": product_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        request=CreateProductSerializer,
        examples=[
            OpenApiExample(
                "Example 1",
                description="Request to product",
                value={
                    "nombre": "string",
                    "descripcion": "string",
                    "precio": 0,
                    "disponible": True,
                },
            ),
        ],
    )
    def retrieve(self, request, pk=None):
        """
        Get an product
        """
        product = self.get_object(pk)
        product_serializer = self.list_serializer_class(product)
        return Response(product_serializer.data)

    @extend_schema(
        request=UpdateProductSerializer,
        examples=[
            OpenApiExample(
                "Example 1",
                description="Request to product",
                value={
                    "nombre": "string",
                    "descripcion": "string",
                    "precio": 0,
                    "disponible": True,
                },
            ),
        ],
    )
    def update(self, request, pk=None):
        """
        Update an product
        """
        product = self.get_object(pk)
        product_serializer = UpdateProductSerializer(product, data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(
                {"message": "Producto actualizado correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización!",
                "error": product_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        request=CreateProductSerializer,
        examples=[
            OpenApiExample(
                "Example 1",
                description="Request to product",
                value={
                    "nombre": "string",
                    "descripcion": "string",
                    "precio": 0,
                    "disponible": True,
                },
            ),
        ],
    )
    def destroy(self, request, pk=None):
        """
        Set an product as inavailable
        """
        product_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).update(
            disponible=False
        )
        if product_destroy == 1:
            return Response(
                {"message": "Producto eliminado correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "El producto no existe!"}, status=status.HTTP_404_NOT_FOUND
        )
