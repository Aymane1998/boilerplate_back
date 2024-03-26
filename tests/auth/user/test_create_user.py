import pytest

from authentication import models
from django import urls
from rest_framework import status, test

from factory.faker import faker
from tests.auth.factorys.user_factory import UserFactory


@pytest.fixture
def test_data(db):
    user_active = UserFactory(is_active=True)
    user_not_active = UserFactory(is_active=False, email="testGood@reseau.free.fr")

    return {"user_active": user_active, "user_not_active": user_not_active}


@pytest.fixture
def api_client():
    return test.APIClient()


@pytest.mark.django_db
class TestCreateUser:
    faker = faker.Faker()

    def endpoint(self):
        return urls.reverse("authentication:user-create")

    def test_create_user(self, api_client, test_data):
        password = "password"
        data = {
            "email": "test@reseau.free.fr",
            "password": password,
            "confirm_password": password,
        }

        response = api_client.post(self.endpoint(), data=data)

        assert response.status_code == status.HTTP_201_CREATED

    def test_creat_user_already_active(self, api_client, test_data):
        user_active = test_data["user_active"]
        password = "password"
        data = {
            "email": user_active.email,
            "password": password,
        }

        response = api_client.post(self.endpoint(), data=data)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_creat_user_not_good_domain(self, api_client, test_data):
        user_active = test_data["user_active"]
        password = "password"
        data = {
            "email": user_active.email,
            "password": password,
        }

        response = api_client.post(self.endpoint(), data=data)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_creat_user_inactive_good_password(self, api_client, test_data):
        user_not_active = test_data["user_not_active"]
        password = "password"
        data = {
            "email": user_not_active.email,
            "password": password,
        }

        response = api_client.post(self.endpoint(), data=data)

        assert response.status_code == status.HTTP_201_CREATED

    def test_try_create_email_not_activate(self, api_client, test_data):
        user_not_active = test_data["user_not_active"]
        password = "password"
        data = {
            "email": user_not_active.email,
            "password": password,
        }

        # create user first time
        response = api_client.post(self.endpoint(), data=data)
        assert response.status_code == status.HTTP_201_CREATED
        query_confirmation_mail_old = models.ConfirmationEmailToken.objects.all()
        assert query_confirmation_mail_old.count()
        id_token_old = query_confirmation_mail_old.first().id

        # check if recreate token and delete old one
        response = api_client.post(self.endpoint(), data=data)
        assert response.status_code == status.HTTP_201_CREATED

        query_confirmation_mail = models.ConfirmationEmailToken.objects.all()
        assert query_confirmation_mail.count() == 1
        assert query_confirmation_mail.first().user == user_not_active
        assert query_confirmation_mail.first().id != id_token_old
