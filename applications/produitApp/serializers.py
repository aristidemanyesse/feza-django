
from rest_framework.serializers import ModelSerializer
from .models import *


class TypeProduitSerializer(ModelSerializer):
    class Meta:
        model = TypeProduit
        fields = '__all__'


class StockStateSerializer(ModelSerializer):
    class Meta:
        model = StockState
        fields = '__all__'


class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'


class ProduitInOfficineSerializer(ModelSerializer):
    class Meta:
        model = ProduitInOfficine
        fields = '__all__'


class AssuranceSerializer(ModelSerializer):
    class Meta:
        model = Assurance
        fields = '__all__'
