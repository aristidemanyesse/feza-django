
from rest_framework.serializers import ModelSerializer
from .models import *


class UtilisateurSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'
