import factory

from .user_factory import UserFactory
from authentication import models


class ConfirmationEmailTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ConfirmationEmailToken

    user = factory.SubFactory(UserFactory)
    token = factory.Faker("uuid4")
