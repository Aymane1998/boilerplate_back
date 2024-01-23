from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Unite, Departement, Service


class UniteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unite
        fields = '__all__'

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at.strftime('%d/%m/%Y') if instance.created_at else None
        representation['updated_at'] = instance.updated_at.strftime('%d/%m/%Y') if instance.updated_at else None
        representation['departement'] = {'value': instance.departement.id,
                                         'label': instance.departement.name} if instance.departement else None
        representation['service'] = {'value': instance.departement.service.id,
                                     'label': instance.departement.service.name} if instance.departement else None
        return representation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'first_name', 'last_name', 'unite']
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['role'] = list(instance.groups.values_list('name', flat=True))
        if instance.unite:
            representation['unite'] = {'value': instance.unite.id, 'label': instance.unite.name}
            representation['service'] = {'value': instance.unite.service.id, 'label': instance.unite.service.name}
            representation['departement'] = {'value': instance.unite.service.departement.id, 'label': instance.unite.service.departement.name}
        return representation


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
