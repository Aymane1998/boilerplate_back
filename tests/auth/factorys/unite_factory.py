import factory

from authentication.models import Unite
from tests.auth.factorys.service_factory import ServiceFactory

class UniteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Unite

    name = factory.Faker('name')
    description = factory.Faker('paragraph')
    service = factory.SubFactory(ServiceFactory)

    @factory.post_generation
    def skills(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # Use the provided list of skills
            self.skills.set(extracted)
