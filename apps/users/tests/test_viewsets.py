import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_list_users(self, authenticated_client, user_factory):
        # Create some test users
        users = user_factory.create_batch(3)

        url = reverse("users-list")
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        # Verificamos que los usuarios creados están en la respuesta
        usernames = [user["username"] for user in response.data]
        for user in users:
            assert user.username in usernames

    def test_create_user(self, authenticated_client):
        url = reverse("users-list")
        data = {"username": "testuser", "password": "testpass123"}

        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["message"] == "El usuario se creo correctamente!"

    def test_retrieve_user(self, authenticated_client, user_factory):
        user = user_factory()

        url = reverse("users-detail", kwargs={"pk": user.pk})
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == user.username

    def test_set_password(self, authenticated_client, user_factory):
        user = user_factory()

        url = reverse("users-set-password", kwargs={"pk": user.pk})
        data = {"password": "newpassword123", "password_confirm": "newpassword123"}

        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "La contraseña se actualizó correctamente!"

    def test_delete_user(self, authenticated_client, user_factory):
        user = user_factory()

        url = reverse("users-detail", kwargs={"pk": user.pk})
        response = authenticated_client.delete(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "Usuario eliminado correctamente!"

        # Verify user is marked as inactive
        user.refresh_from_db()
        assert not user.is_active
