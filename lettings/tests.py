import pytest
from django.test import Client
from django.urls import reverse, resolve
from .models import Address, Letting


@pytest.mark.django_db
def test_index():
    client = Client()
    address = Address.objects.create(number=1, street="Test street", city="Test city", state="TT",
                                     zip_code=1234, country_iso_code="TST")
    letting = Letting.objects.create(address=address, title="Test")
    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()

    assert path == "/lettings/"
    assert response.status_code == 200
    assert letting.title in content
    assert resolve(path).view_name == "lettings_index"


@pytest.mark.django_db
def test_letting():
    client = Client()
    address = Address.objects.create(number=1, street="Test street", city="Test city", state="TT",
                                     zip_code=1234, country_iso_code="TST")
    letting = Letting.objects.create(address=address, title="Test")
    path = reverse('letting', kwargs={"letting_id": letting.pk})
    response = client.get(path)
    content = response.content.decode()

    assert path == f"/lettings/{letting.pk}/"
    assert response.status_code == 200
    assert letting.title in content
    assert resolve(path).view_name == "letting"
