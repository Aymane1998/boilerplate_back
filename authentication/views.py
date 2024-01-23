"""This module handles authentication views."""

from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Service, Unite, Departement, User
from .serializers import MyTokenObtainPairSerializer, UserSerializer, ServiceSerializer, UniteSerializer, \
    DepartementSerializer


# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    """This class handles the token generation view."""

    serializer_class = MyTokenObtainPairSerializer


class CurrentUserView(APIView):
    """This class handles the current user view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        """Handle the GET request."""
        serializer = UserSerializer(request.user)
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


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserUpdateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all().order_by('-updated_at')
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all().order_by('-updated_at')
    serializer_class = ServiceSerializer

class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all().order_by('-updated_at')
    serializer_class = ServiceSerializer

class ServiceDeleteView(generics.DestroyAPIView):
    queryset = Service.objects.all().order_by('-updated_at')
    serializer_class = ServiceSerializer

class UniteListCreateView(generics.ListCreateAPIView):
    queryset = Unite.objects.all().order_by('-updated_at')
    serializer_class = UniteSerializer

class DepartementListCreateView(generics.ListCreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class DepartementUpdateView(generics.UpdateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class DepartementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer