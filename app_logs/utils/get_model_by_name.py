from django.apps import apps
from authentication import models as auth_models


def get_model_by_model_name(model_name):
    # return authentication user model if user.
    # without the if get an error between django user and authentication user
    if model_name == "User":
        return auth_models.User

    for apps_conf in apps.get_app_configs():
        try:
            foo_model = apps_conf.get_model(model_name)
            return foo_model

        except LookupError:
            foo_model = None

    return None
