import pytest
from tests.data import UserFactory


@pytest.fixture
def db_users(db):
    user_admin = UserFactory(is_staff=True)

    return {
        "user_admin": user_admin,
    }
