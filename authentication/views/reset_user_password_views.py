from authentication import models, serializers, services
from django import shortcuts

from rest_framework import status, response, views


class ForgottenPasswordView(views.APIView):
    permission_classes = []
    serializer_class = serializers.ForgottenPasswordSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            user = services.GetUserByUsernameOrEmail(input=data["username"]).handler()

            if user == None:
                raise ValueError("No user found.")

            service = services.SendMailResetPasswordService(user)
            service.handler()

            return response.Response(status=status.HTTP_200_OK, data="mail send")

        except ValueError as error:
            return response.Response(
                status=status.HTTP_406_NOT_ACCEPTABLE,
                data=str(error),
            )


class ResetPasswordView(views.APIView):
    permission_classes = []
    serializer_class = serializers.ResetPasswordSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        token = shortcuts.get_object_or_404(
            models.TokenResetPassword, token=data["token_value"]
        )

        service = services.ResetUserPasswordService(
            token=token,
            password=data["password"],
        )
        service.handler()

        return response.Response(status=status.HTTP_200_OK, data="Password updated")
