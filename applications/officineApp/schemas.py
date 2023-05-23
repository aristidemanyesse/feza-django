from graphene_django_extras import DjangoSerializerType
from .serializers import *


class TypeOfficineType(DjangoSerializerType):
    class Meta:
        serializer_class = TypeOfficineSerializer
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "name": ("exact",),
            "etiquette": ("exact",),
        }
        

class CirconscriptionType(DjangoSerializerType):
    class Meta:
        serializer_class = CirconscriptionSerializer
        exclude_fields = ('geometry',)
        filter_fields = {
            "id": ("exact", ),
            "name": ("exact", ),
            "deleted": ("exact", ),
        }
        
        
class OfficineType(DjangoSerializerType):
    class Meta:
        serializer_class = OfficineSerializer
        exclude_fields = ('geometry',)
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "name": ("icontains", "iexact"),
            "type__id": ("exact", ),
            "type__etiquette": ("exact", ),
            "circonscription__id": ("exact", )
        }
        
        
class ResponsableOfficineType(DjangoSerializerType):
    class Meta:
        serializer_class = ResponsableOfficineSerializer
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "first_name": ("icontains", "iexact"),
            "last_name": ("icontains", "iexact"),
            "username": ("icontains", "iexact"),
            "officine__id": ("exact",),
        }
        
        
class GardeType(DjangoSerializerType):
    class Meta:
        serializer_class = GardeSerializer
        filter_fields = {
            "debut": ("exact", "lte", "gte"),
            "fin": ("exact", "lte", "gte")
        }
        
        
class OfficineDeGardeType(DjangoSerializerType):
    class Meta:
        serializer_class = OfficineDeGardeSerializer
        filter_fields = {
            "officine__id": ("exact",),
            "garde__id": ("exact", )
        }
