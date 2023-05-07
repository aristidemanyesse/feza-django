from UserApp.models import Utilisateur
from graphene_django_extras import  DjangoSerializerType
from .serializers import *

class UtilisateurType(DjangoSerializerType):
    class Meta:
        serializer_class = UtilisateurSerializer
        description = " Type definition for a single Utilisateur "
        exclude_fields = ('geometry',)
        filter_fields = {
            "id": ("exact", ),
            "fullname": ("icontains", "iexact"),
            "otp": ("exact",),
            "circonscription__id": ("exact",),
            "contact": ("icontains", "iexact"),
            "is_valide": ("exact", ),
        }
