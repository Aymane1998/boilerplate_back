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

from authentication.models import Service, Departement
from authentication.serializers import ServiceSerializer
from tests.auth.factorys.service_factory import ServiceFactory
from tests.auth.fixtures.departements import db_departements
from tests.auth.fixtures.users import db_users

@pytest.fixture
def test_data(db, db_users, db_departements):
    departement1 = db_departements['departement1']

    service1 = ServiceFactory(departement=departement1)

    return {
        "departement1": departement1,
        "service1": service1,
        "user_admin": db_users["user_admin"]
    }


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestServiceCRUDAPIView:
    create_endpoint = "authentication:service-create"
    list_endpoint = "authentication:service-list"
    detail_endpoint = "authentication:service-detail"
    update_endpoint = "authentication:service-update"
    delete_endpoint = "authentication:service-delete"

    faker = Faker("fr_FR")

    def test_create_service(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)


        data_service = {
            "name": self.faker.name(),
            "description": self.faker.paragraph(),
            "departement": test_data["departement1"].pk
        }

        nbr_service_before = Service.objects.all().count()

        response = api_client.post(reverse(self.create_endpoint), data=data_service)

        nbr_service_after = Service.objects.all().count()
        assert response.status_code == HTTP_201_CREATED
        assert nbr_service_before + 1 == nbr_service_after

    def test_get_list_create(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        response = api_client.get(reverse(self.list_endpoint))

        assert response.status_code == HTTP_200_OK
        assert len(response.data) == Service.objects.all().count()

    def test_put_service(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        service1 = test_data["service1"]

        serializer_data = ServiceSerializer(service1).data
        serializer_data["name"] = "lorem"
        serializer_data["departement"] = test_data["departement1"].pk

        response = api_client.put(
            reverse(self.update_endpoint, kwargs={"pk": service1.id}),
            data=serializer_data, format='json'
        )

        assert response.status_code == HTTP_200_OK

        service_updated = Service.objects.get(id=service1.id)
        assert service_updated.name == "lorem"

    def test_delete_service(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        service1 = test_data["service1"]

        response = api_client.delete(
            reverse(self.delete_endpoint, kwargs={"pk": service1.id})
        )

        assert response.status_code == HTTP_204_NO_CONTENT

        queryset = Service.objects.filter(id=service1.id)
        assert queryset.count() == 0

    def test_details_service(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)
        service1 = test_data["service1"]

        response = api_client.get(
            reverse(self.detail_endpoint, kwargs={"pk": service1.id})
        )

        assert response.status_code == HTTP_200_OK

        serv1 = Service.objects.get(pk=service1.id)
        assert serv1.name == service1.name