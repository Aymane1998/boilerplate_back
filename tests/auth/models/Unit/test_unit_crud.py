from cgi import test
from django.urls import reverse
from faker import Faker
import pytest
from rest_framework.test import APIClient
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_401_UNAUTHORIZED,
)

from authentication.models import Unite
from authentication.serializers import UniteSerializer
from tests.auth.factorys.unite_factory import UniteFactory
from tests.auth.fixtures.departements import db_departements
from tests.auth.fixtures.service import db_services
from tests.auth.fixtures.users import db_users


@pytest.fixture
def test_data(db, db_users, db_departements, db_services):
    departement1 = db_departements['departement1']

    service1 = db_services['service1']

    unite1 = UniteFactory(service=service1)

    return {
        "departement1": departement1,
        "service1": db_services['service1'],
        "user_admin": db_users["user_admin"],
        "unite1": unite1
    }


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestUniteCRUDAPIView:
    create_endpoint = "authentication:unite-create"
    list_endpoint = "authentication:unite-list"
    detail_endpoint = "authentication:unite-detail"
    update_endpoint = "authentication:unite-update"
    delete_endpoint = "authentication:unite-delete"

    faker = Faker("fr_FR")

    def test_create_service(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)

        data_unite = {
            "name": self.faker.name(),
            "description": self.faker.paragraph(),
            "service": test_data["service1"].pk
        }

        nbr_unite_before = Unite.objects.all().count()
        response = api_client.post(reverse(self.create_endpoint), data=data_unite)

        nbr_unite_after = Unite.objects.all().count()
        assert response.status_code == HTTP_201_CREATED
        assert nbr_unite_before + 1 == nbr_unite_after

    def test_get_list_create(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        response = api_client.get(reverse(self.list_endpoint))

        assert response.status_code == HTTP_200_OK
        assert len(response.data) == Unite.objects.all().count()

    def test_put_unite(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        unite1 = test_data["unite1"]

        serializer_data = UniteSerializer(unite1).data
        serializer_data["name"] = "lorem"
        serializer_data["service"] = test_data["service1"].pk

        response = api_client.put(
            reverse(self.update_endpoint, kwargs={"pk": unite1.id}),
            data=serializer_data, format='json'
        )

        assert response.status_code == HTTP_200_OK

        unite_updated = Unite.objects.get(id=unite1.id)
        assert unite_updated.name == "lorem"

    def test_delete_service(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        unite1 = test_data["unite1"]

        response = api_client.delete(
            reverse(self.delete_endpoint, kwargs={"pk": unite1.id})
        )

        assert response.status_code == HTTP_204_NO_CONTENT

        queryset = Unite.objects.filter(id=unite1.id)
        assert queryset.count() == 0

    def test_details_unite(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        unite1 = test_data["unite1"]

        response = api_client.get(
            reverse(self.detail_endpoint, kwargs={"pk": unite1.id})
        )

        assert response.status_code == HTTP_200_OK

        u1 = Unite.objects.get(pk=unite1.id)
        assert u1.name == unite1.name