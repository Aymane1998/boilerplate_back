import pytest

from tests.auth.factorys.departement_factory import DepartementFactory


@pytest.fixture
def db_departements():

    return {
        "departement1": DepartementFactory(),
        "departement2": DepartementFactory(),
        "departement3": DepartementFactory(),
    }
