from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from authentication.permissions import IsAdmin
from authentication.serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

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
