import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from apps.products.tests.factories import ProductFactory
from apps.users.tests.factories import UserFactory

# Register factories
register(ProductFactory)
register(UserFactory)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_client(api_client, user_factory):
    user = user_factory()
    api_client.force_authenticate(user=user)
    return api_client
