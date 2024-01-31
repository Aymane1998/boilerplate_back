import pytest

from tests.auth.factorys.service_factory import ServiceFactory
from tests.auth.fixtures.departements import db_departements

@pytest.fixture
def db_services(db_departements):

    return {
        "service1": ServiceFactory(departement=db_departements['departement1']),
    }
