from graphene_django_extras import DjangoSerializerType
from .serializers import *


class TypeProduitType(DjangoSerializerType):
    class Meta:
        serializer_class = TypeProduitSerializer
        filter_fields = {
            "id": ("exact", ),
            "name": ("exact",),
            "etiquette": ("exact",),
        }
        

class StockStateType(DjangoSerializerType):
    class Meta:
        serializer_class = StockStateSerializer
        filter_fields = {
            "id": ("exact", ),
            "name": ("exact",),
            "etiquette": ("exact",),
        }
        
        
class ProduitType(DjangoSerializerType):
    class Meta:
        serializer_class = ProduitSerializer
        filter_fields = {
            "id": ("exact", ),
            "name": ("icontains", "iexact"),
            "type__id": ("exact",),
            "only_ordonnance": ("exact",),
            "codebarre": ("exact", )
        }
        
        
class ProduitInOfficineType(DjangoSerializerType):
    class Meta:
        serializer_class = ProduitInOfficineSerializer
        filter_fields = {
            "id": ("exact", ),
            "quantite": ("lte", "gte", "exact"),
            "officine__id": ("exact",),
            "produit__id": ("exact",),
            "produit__name": ("icontains",),
            "stock_state__etiquette": ("exact",)
        }
        
        
class AssuranceType(DjangoSerializerType):
    class Meta:
        serializer_class = AssuranceSerializer
        filter_fields = {
            "id": ("exact", ),
            "name": ("exact",),
            "etiquette": ("exact",),
        }