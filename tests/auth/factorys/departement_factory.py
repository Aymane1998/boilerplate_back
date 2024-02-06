import factory

from authentication.models import Departement

class DepartementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Departement

    name = factory.Faker('name')
    description = factory.Faker('paragraph')

    @factory.post_generation
    def skills(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # Use the provided list of skills
            self.skills.set(extracted)
