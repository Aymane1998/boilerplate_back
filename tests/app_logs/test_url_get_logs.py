import pytest
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status, test

from tests.data import (
    db_users,
    factorys,
)


@pytest.fixture
def test_data(db, db_users):
    user_admin = db_users["user_admin"]
    user_not_admin = factorys.UserFactory()

    user_changed = factorys.UserFactory()
    user_changed.first_name = "new_name"
    user_changed.save()

    user_changed.last_name = "new_last_name"
    user_changed.save()

    return {
        "user_admin": user_admin,
        "user_not_admin": user_not_admin,
        "user_changed": user_changed,
    }


@pytest.fixture
def api_client():
    return test.APIClient()


@pytest.mark.django_db
class TestUrlLogs:
    def endpoint(self, params, query_kwargs=None):
        url = reverse("logs:logs", kwargs=params)

        if query_kwargs:
            return f"{url}?{urlencode(query_kwargs)}"

        return url

    def test_get_response_200(self, api_client, test_data):
        user_admin = test_data["user_admin"]

        api_client.force_authenticate(user=user_admin)

        params = {"model": "User"}

        response = api_client.get(self.endpoint(params))
        assert response.status_code == status.HTTP_200_OK

    def test_only_user_admin_has_permission(self, api_client, test_data):
        user_not_admin = test_data["user_not_admin"]

        api_client.force_authenticate(user=user_not_admin)

        params = {"model": "User"}

        response = api_client.get(self.endpoint(params))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_need_to_be_connected(self, api_client, test_data):
        params = {"model": "User"}

        response = api_client.get(self.endpoint(params))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_only_our_object_history(self, api_client, test_data):
        user_admin = test_data["user_admin"]
        user_changed = test_data['user_changed']

        api_client.force_authenticate(user=user_admin)

        params = {"model": "User"}

        query_params = {"object_id": user_changed.id}

        response = api_client.get(self.endpoint(params, query_params))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["changes"]) == 2

        for change in response.data["changes"]:
            assert change["object_id"] == user_changed.id

    def test_get_only_change_from_field_choose(self, api_client, test_data):
        user_admin = test_data["user_admin"]
        user_changed = test_data["user_changed"]

        api_client.force_authenticate(user=user_admin)

        params = {"model": "User"}

        query_params = {"object_id": user_changed.id, "field": "first_name"}

        response = api_client.get(self.endpoint(params, query_params))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["changes"]) == 1

        for change in response.data["changes"]:
            assert change["field_changed"] == "first_name"

    def test_get_nothing_if_wrong_field(self, api_client, test_data):
        user_admin = test_data["user_admin"]
        user_changed = test_data["user_changed"]

        api_client.force_authenticate(user=user_admin)

        params = {"model": "User"}

        query_params = {"object_id": user_changed.id, "field": "not a field"}

        response = api_client.get(self.endpoint(params, query_params))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["changes"]) == 0

    def test_get_error_if_wrong_model_name(self, api_client, test_data):
        user_admin = test_data["user_admin"]
        user_changed = test_data["user_changed"]

        api_client.force_authenticate(user=user_admin)

        params = {"model": "not a model name"}

        query_params = {"object_id": user_changed.id, "field": "first_name"}

        response = api_client.get(self.endpoint(params, query_params))

        assert response.status_code == status.HTTP_400_BAD_REQUEST
