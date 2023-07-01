
from rest_framework.serializers import ModelSerializer
from .models import *


class UtilisateurSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class DemandeSerializer(ModelSerializer):
    class Meta:
        model = Demande
        fields = '__all__'

class OfficineDemandeSerializer(ModelSerializer):
    class Meta:
        model = OfficineDemande
        fields = '__all__'

class LigneDemandeSerializer(ModelSerializer):
    class Meta:
        model = LigneDemande
        fields = '__all__'


class ReponseSerializer(ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'

class LigneReponseSerializer(ModelSerializer):
    class Meta:
        model = LigneReponse
        fields = '__all__'