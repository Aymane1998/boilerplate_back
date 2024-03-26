import pytest

from rest_framework import status, test

from django.urls import reverse
from tests.auth.factorys import user_factory


@pytest.fixture
def test_data(db):
    user_password = "password"
    user = user_factory.UserFactory(
        username="test_user",
        password=user_password,
        email="test_user@iliad.fr",
        is_active=True,
    )

    user_not_activate = user_factory.UserFactory(
        username="test_user_not_activate",
        password=user_password,
        email="test_user_not_activate@iliad.fr",
        is_active=False,
    )

    return {
        "user": user,
        "user_password": user_password,
        "user_not_activate": user_not_activate,
    }


@pytest.fixture
def api_client():
    return test.APIClient()


@pytest.mark.django_db
class TestLoginUser:
    def endpoints(self):
        return reverse("authentication:token-obtain-pair")

    def test_login_username_user(self, api_client, test_data):
        user = test_data["user"]
        user_password = test_data["user_password"]

        data = {"username": user.username, "password": user_password}
        response = api_client.post(self.endpoints(), data=data)

        assert response.status_code == status.HTTP_200_OK

    def test_login_email_user(self, api_client, test_data):
        user = test_data["user"]
        user_password = test_data["user_password"]

        data = {"username": user.email, "password": user_password}
        response = api_client.post(self.endpoints(), data=data)

        assert response.status_code == status.HTTP_200_OK

    def test_user_not_good_username(self, api_client, test_data):
        user_password = test_data["user_password"]
        data = {"username": "wrong", "password": user_password}
        response = api_client.post(self.endpoints(), data=data)

        assert response.status_code == status.HTTP_406_NOT_ACCEPTABLE

    def test_user_not_good_password(self, api_client, test_data):
        user = test_data["user"]
        data = {"username": user.username, "password": "wrong"}
        response = api_client.post(self.endpoints(), data=data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_user_not_activate(self, api_client, test_data):
        user = test_data["user_not_activate"]
        user_password = test_data["user_password"]

        data = {"username": user.username, "password": user_password}
        response = api_client.post(self.endpoints(), data=data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
