import pytest
from django.urls import reverse
from rest_framework import status

from apps.products.models import Product

pytestmark = pytest.mark.django_db


class TestProductViewSet:
    def test_list_products(self, authenticated_client, product_factory):
        # Create some test products
        product_factory.create_batch(3)

        url = reverse("products-list")
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3  # Verificar la lista con paginación

    def test_create_product(self, authenticated_client):
        url = reverse("products-list")
        data = {
            "nombre": "Test Product",
            "descripcion": "Test Description",
            "precio": 1000,
            "disponible": True,
        }

        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["message"] == "El producto se creo correctamente!"

    def test_retrieve_product(self, authenticated_client, product_factory):
        product = product_factory()

        url = reverse("products-detail", kwargs={"pk": product.pk})
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["nombre"] == product.nombre

    def test_update_product(self, authenticated_client, product_factory):
        product = product_factory()

        url = reverse("products-detail", kwargs={"pk": product.pk})
        data = {
            "nombre": "Updated Product",
            "descripcion": "Updated Description",
            "precio": 2000,
            "disponible": True,
        }

        response = authenticated_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "Producto actualizado correctamente!"

    def test_delete_product(self, authenticated_client, product_factory):
        product = product_factory()

        url = reverse("products-detail", kwargs={"pk": product.pk})
        response = authenticated_client.delete(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "Producto eliminado correctamente!"
        # Verificar que el producto está marcado como no disponible
        product.refresh_from_db()
        assert not product.disponible

    def test_filter_products(self, authenticated_client, product_factory):
        # Create products with different prices
        product_factory(precio=1000)
        product_factory(precio=2000)
        product_factory(precio=3000)

        url = reverse("products-list")
        response = authenticated_client.get(f"{url}?precio_min=2000")

        assert response.status_code == status.HTTP_200_OK
        assert (
            len(response.data["results"]) == 2
        )  # Should only return products with price >= 2000

    def test_search_products(self, authenticated_client, product_factory):
        product = product_factory(nombre="Unique Product Name")
        product_factory(nombre="Different Product")

        url = reverse("products-list")
        response = authenticated_client.get(f"{url}?search=Unique")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["nombre"] == product.nombre

    def test_order_products(self, authenticated_client, product_factory):
        product_factory(nombre="Product C", precio=1000)
        product_factory(nombre="Product A", precio=3000)
        product_factory(nombre="Product B", precio=2000)

        url = reverse("products-list")
        response = authenticated_client.get(f"{url}?ordering=nombre")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["nombre"] == "Product A"
