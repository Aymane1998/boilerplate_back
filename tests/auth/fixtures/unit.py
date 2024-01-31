import pytest

from tests.auth.factorys.unite_factory import UniteFactory
from tests.auth.fixtures.departements import db_departements
from tests.auth.fixtures.service import db_services


@pytest.fixture
def db_units():

    return {
        "unite1": UniteFactory(departement=db_services['service1']),
    }
