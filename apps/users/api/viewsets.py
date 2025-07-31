from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.users.api.serializers import (
    PasswordSerializer,
    UserListSerializer,
    UserSerializer,
)

serializer_class = UserSerializer
list_serializer_class = UserListSerializer


class UserViewSet(viewsets.GenericViewSet):
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class.Meta.model.objects.filter(
                is_active=True
            ).values("username")
            return self.queryset

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)

    @action(methods=["post"], detail=True)
    def set_password(self, request, pk=None):
        """
        Change password
        """
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data["password"])
            user.save()
            return Response(
                {"message": "La contraseña se actualizó correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Ocurrieron errores!", "error": password_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def list(self, request, *args, **kwargs):
        """
        Get a collection of users
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)
