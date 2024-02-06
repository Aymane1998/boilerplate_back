from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Unite, Departement, Service

class DepartementRepresentationSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')
    class Meta:
        model = Departement
        fields = ['value', 'label']

class ServiceRepresentationSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')
    departement = DepartementRepresentationSerializer()
    class Meta:
        model = Service
        fields = ['value', 'label', 'departement']

class UniteRepresentationSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')
    service = ServiceRepresentationSerializer()
    class Meta:
        model = Unite
        fields = ['value', 'label', 'service']

class UniteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unite
        fields = '__all__'

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    departement = DepartementRepresentationSerializer()
    class Meta:
        model = Service
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # format Dates
        representation['created_at'] = instance.created_at.strftime('%d/%m/%Y') if instance.created_at else None
        representation['updated_at'] = instance.updated_at.strftime('%d/%m/%Y') if instance.updated_at else None
        return representation

class UserSerializer(serializers.ModelSerializer):
    unite = UniteRepresentationSerializer()

    class Meta:
        model = User

        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'first_name',
                  'last_name',
                  'unite',
                  'birth_date',
                  'about',
                  'unite',]
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # User's roles (groups names)
        representation['role'] = list(instance.groups.values_list('name', flat=True))
        return representation


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
