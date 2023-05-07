
from rest_framework.serializers import ModelSerializer
from .models import *


class TypeOfficineSerializer(ModelSerializer):
    class Meta:
        model = TypeOfficine
        fields = '__all__'


class OfficineSerializer(ModelSerializer):
    class Meta:
        model = Officine
        fields = '__all__'


class CirconscriptionSerializer(ModelSerializer):
    class Meta:
        model = Circonscription
        fields = '__all__'


class ResponsableOfficineSerializer(ModelSerializer):
    class Meta:
        model = ResponsableOfficine
        fields = '__all__'


class OfficineDeGardeSerializer(ModelSerializer):
    class Meta:
        model = OfficineDeGarde
        fields = '__all__'


class GardeSerializer(ModelSerializer):
    class Meta:
        model = Garde
        fields = '__all__'
