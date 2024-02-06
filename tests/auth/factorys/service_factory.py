import factory

from authentication.models import Service
from tests.auth.factorys.departement_factory import DepartementFactory

class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = factory.Faker('name')
    description = factory.Faker('paragraph')
    departement = factory.SubFactory(DepartementFactory)

    @factory.post_generation
    def skills(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # Use the provided list of skills
            self.skills.set(extracted)
