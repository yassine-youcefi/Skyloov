
import pytest
from django.test import Client
from products.models import Products
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.fixture
def user():
    user = User.objects.create(username='testuser', password='testpassword')
    return user

@pytest.fixture
def unknown_client():
    return APIClient()

@pytest.fixture
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    client.user = user
    return client


@pytest.fixture
def product():
    return Products.objects.create(
        name="test product",
        brand="test brand",
        category="test category",
        price=50.0,
        quantity=4,
        rating=4.5,
        created_at="2023/05/06"
    )
    