from authentication import exceptions, services
from rest_framework import serializers, status

from notification import services as notification_services

from .models import Departement, Service, TokenResetPassword, Unite, User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class DepartementRepresentationSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source="id")
    label = serializers.CharField(source="name")

    class Meta:
        model = Departement
        fields = ["value", "label"]


class ServiceRepresentationSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source="id")
    label = serializers.CharField(source="name")
    departement = DepartementRepresentationSerializer()

    class Meta:
        model = Service
        fields = ["value", "label", "departement"]


class UniteRepresentationSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source="id")
    label = serializers.CharField(source="name")
    service = ServiceRepresentationSerializer()

    class Meta:
        model = Unite
        fields = ["value", "label", "service"]


class UniteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unite
        fields = "__all__"


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # format Dates
        representation["created_at"] = (
            instance.created_at.strftime("%d/%m/%Y") if instance.created_at else None
        )
        representation["updated_at"] = (
            instance.updated_at.strftime("%d/%m/%Y") if instance.updated_at else None
        )
        return representation


class UserSerializer(serializers.ModelSerializer):
    unite = UniteRepresentationSerializer()

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "first_name",
            "last_name",
            "unite",
            "birth_date",
            "about",
            "unite",
        ]
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # User's roles (groups names)
        representation["role"] = list(instance.groups.values_list("name", flat=True))
        return representation


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )

    def _get_username(self, validated_data):
        return validated_data.get("email").split("@")[0]

    def create(self, validated_data):
        service_check_creation = services.CheckCreationUser(validated_data.get("email"))

        if not service_check_creation.check_email_valid_domaine():
            detail = "Email non autorisé"
            raise exceptions.APIValidationError(
                detail=detail, status=status.HTTP_403_FORBIDDEN
            )

        if service_check_creation.check_user_exist() is None:
            user = User.objects.create(
                email=validated_data.get("email"),
                password=validated_data.get("password"),
                username=self._get_username(validated_data),
                is_active=False,
            )

        if service_check_creation.check_user_exist():
            if service_check_creation.check_user_active():
                detail = "Email already used."
                raise exceptions.APIValidationError(
                    detail=detail, status=status.HTTP_403_FORBIDDEN
                )

            else:
                user = service_check_creation.get_user()

        service_create_confirm_mail = services.CreateConfirmUserEmail(user=user)

        subject = "Confirmation de l'adresse mail pour le portail prestataire"
        message = f"Veuillez clicker sur le lien \
            {service_create_confirm_mail.get_url()} \
            afin de valider votre mail."
        list_mails = [user.email]

        service = notification_services.SendMailService(subject, message, list_mails)
        service.send_mails()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        if not attrs.get("username"):
            detail = "Miss username input value."
            raise exceptions.APIValidationError(detail, status.HTTP_406_NOT_ACCEPTABLE)

        try:
            user = services.GetUserByUsernameOrEmail(
                input=attrs.get("username")
            ).handler()

        except ValueError as error:
            raise exceptions.APIValidationError(
                detail=str(error),
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

        attrs["username"] = user.username

        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        return token


class ForgottenPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()


class ResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    token_value = serializers.CharField(source="token")

    class Meta:
        model = TokenResetPassword
        fields = (
            "token_value",
            "password",
        )
