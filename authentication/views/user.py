from rest_framework import generics

from authentication.models import User
from authentication.serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer