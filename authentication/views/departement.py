from rest_framework import generics

from authentication.models import Departement
from authentication.permissions import IsAdmin
from authentication.serializers import DepartementSerializer

class DepartementListView(generics.ListAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    # permission_classes = [IsAdmin]

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
    # permission_classes = [IsAdmin]

class DepartementDeleteView(generics.DestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = [IsAdmin]