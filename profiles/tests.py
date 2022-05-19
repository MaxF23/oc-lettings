import pytest
from django.test import Client
from django.urls import reverse, resolve
from .models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_index():
    client = Client()
    user = User.objects.create(username="test_user", id=1)
    Profile.objects.create(user_id=1, favorite_city="Paris")
    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()

    assert path == "/profiles/"
    assert response.status_code == 200
    assert user.username in content
    assert resolve(path).view_name == "profiles_index"


@pytest.mark.django_db
def test_profile():
    client = Client()
    user = User.objects.create(username="test_user", id=1)
    Profile.objects.create(user_id=1, favorite_city="Paris")
    path = reverse('profile', kwargs={"username": user.username})
    response = client.get(path)
    content = response.content.decode()

    assert path == f"/profiles/{user.username}/"
    assert response.status_code == 200
    assert user.username in content
    assert resolve(path).view_name == "profile"
