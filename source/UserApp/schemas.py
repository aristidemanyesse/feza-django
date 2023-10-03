from graphene_django_extras import  DjangoSerializerType
from .serializers import *

class UtilisateurType(DjangoSerializerType):
    class Meta:
        serializer_class = UtilisateurSerializer
        description = " Type definition for a single Utilisateur "
        exclude_fields = ('geometry',)
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "fullname": ("icontains", "iexact"),
            "otp": ("exact",),
            "imei": ("exact",),
            "circonscription__id": ("exact",),
            "contact": ("exact", ),
            "is_valide": ("exact", ),
        }
