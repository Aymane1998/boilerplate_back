import pytest

from django.urls import reverse
from faker import Faker
from rest_framework import status

from authentication.models import Departement
from authentication.serializers import DepartementSerializer
from rest_framework.test import APIClient
from tests.auth.factorys.departement_factory import DepartementFactory
from tests.auth.fixtures.users import db_users


@pytest.fixture
def test_data(db, db_users):
    departement1 = DepartementFactory()

    return {"departement1": departement1, "user_admin": db_users["user_admin"]}


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
class TestDepartementCRUDAPIView:
    create_endpoint = "authentication:departement-create"
    list_endpoint = "authentication:departement-list"
    detail_endpoint = "authentication:departement-detail"
    update_endpoint = "authentication:departement-update"
    delete_endpoint = "authentication:departement-delete"

    faker = Faker("fr_FR")

    def test_create_departement(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)

        data_departement = {
            "name": self.faker.name(),
            "description": self.faker.paragraph(),
        }

        nbr_departement_before = Departement.objects.all().count()
        response = api_client.post(reverse(self.create_endpoint), data=data_departement)

        nbr_departement_after = Departement.objects.all().count()
        assert response.status_code == status.HTTP_201_CREATED
        assert nbr_departement_before + 1 == nbr_departement_after

    def test_get_list_departement(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        response = api_client.get(reverse(self.list_endpoint))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == Departement.objects.all().count()

    def test_put_departement(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        departement1 = test_data["departement1"]

        serializer_data = DepartementSerializer(departement1).data
        serializer_data["name"] = "lorem"

        response = api_client.put(
            reverse(self.update_endpoint, kwargs={"pk": departement1.id}),
            data=serializer_data,
        )

        assert response.status_code == status.HTTP_200_OK

        departement_updated = Departement.objects.get(id=departement1.id)
        assert departement_updated.name == "lorem"

    def test_delete_departement(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        departement1 = test_data["departement1"]

        response = api_client.delete(
            reverse(self.delete_endpoint, kwargs={"pk": departement1.id})
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        queryset = Departement.objects.filter(id=departement1.id)
        assert queryset.count() == 0

    def test_details_departement(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        departement1 = test_data["departement1"]

        response = api_client.get(
            reverse(self.detail_endpoint, kwargs={"pk": departement1.id})
        )

        assert response.status_code == status.HTTP_200_OK

        dep1 = Departement.objects.get(pk=departement1.id)
        assert dep1.name == departement1.name
