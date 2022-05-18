from django.test import Client
from django.urls import reverse, resolve


def test_index():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()

    assert path == "/"
    assert response.status_code == 200
    assert "Welcome" in content
    assert resolve(path).view_name == "index"


def test_dummy():
    assert 1
