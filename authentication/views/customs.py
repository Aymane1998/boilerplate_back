"""This module handles authentication views."""

from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

# from authentication.serializers import MyTokenObtainPairSerializer, UserSerializer
from authentication import serializers as auth_serializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    """This class handles the token generation view."""

    serializer_class = auth_serializer.MyTokenObtainPairSerializer


class CurrentUserView(APIView):
    """This class handles the current user view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = auth_serializer.UserSerializer

    def get(self, request):
        """Handle the GET request."""
        serializer = auth_serializer.UserSerializer(request.user)
        return Response(serializer.data)

    # def put(self, request):
    #     try:
    #         user = User.objects.get(pk=request.user.id)
    #         serializer = UserSerializer(user, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST
    #               )
    #     except User.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
