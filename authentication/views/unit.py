from rest_framework import generics

from authentication.models import Unite
from authentication.permissions import IsAdmin
from authentication.serializers import UniteSerializer

class UniteListView(generics.ListAPIView):
    queryset = Unite.objects.all()
    serializer_class = UniteSerializer

class UniteCreateView(generics.CreateAPIView):
    queryset = Unite.objects.all()
    serializer_class = UniteSerializer
    permission_classes = [IsAdmin]

class UniteUpdateView(generics.UpdateAPIView):
    queryset = Unite.objects.all()
    serializer_class = UniteSerializer
    permission_classes = [IsAdmin]

class UniteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unite.objects.all()
    serializer_class = UniteSerializer

class UniteDeleteView(generics.DestroyAPIView):
    queryset = Unite.objects.all()
    serializer_class = UniteSerializer
    permission_classes = [IsAdmin]