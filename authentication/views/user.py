from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

from authentication import services
from authentication.models import User
from authentication.permissions import IsAdmin
from authentication.serializers import UserSerializer, CreateUserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = CreateUserSerializer
    permission_classes = []


class UserListView(generics.ListAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class ConfirmationActivationUserView(views.APIView):
    lookup_field = "token"
    permission_classes = []

    def get(self, request, token):
        service = services.ActivateEmailUser(token_value=token)
        user_has_been_activated = service.handler()

        if not user_has_been_activated:
            return response.Response(
                status=status.HTTP_403_FORBIDDEN, data="token expired"
            )

        service_get_user_token = services.GetUserTokens(service.get_user())
        dictionnary_token = service_get_user_token.get_user_auth_tokens()

        return response.Response(status=status.HTTP_200_OK, data=dictionnary_token)
