import pytest
from ..factorys.user_factory import (
    AdminUserFactory,
)

@pytest.fixture
def db_users(db):

    user_admin = AdminUserFactory(username="user_admin")

    return {
        "user_admin": user_admin,
    }
