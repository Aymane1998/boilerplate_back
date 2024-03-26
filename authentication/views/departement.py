from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as rest_filters

from authentication.models import Departement
from authentication.permissions import IsAdmin
from authentication.serializers import DepartementSerializer
from authentication import filters


class DepartementListView(generics.ListAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = []
    filter_backends = [rest_filters.DjangoFilterBackend]
    filterset_class = filters.DepartmentFilters


class DepartementCreateView(generics.CreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = [IsAdmin]


class DepartementUpdateView(generics.UpdateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = [IsAdmin]


class DepartementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = [IsAuthenticated]


class DepartementDeleteView(generics.DestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = [IsAdmin]
