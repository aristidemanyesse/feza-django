
from demandeApp.models import *
from rest_framework.serializers import ModelSerializer


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

class SubsLigneReponseSerializer(ModelSerializer):
    class Meta:
        model = SubsLigneReponse
        fields = '__all__'

class RdvLigneReponseSerializer(ModelSerializer):
    class Meta:
        model = RdvLigneReponse
        fields = '__all__'