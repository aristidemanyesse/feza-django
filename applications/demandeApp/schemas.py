
from graphene_django_extras import  DjangoSerializerType
from demandeApp.serializers import *


class DemandeType(DjangoSerializerType):
    class Meta:
        serializer_class = DemandeSerializer
        description = " Type definition for a single Demande "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "utilisateur__id": ("exact",),
            "status": ("exact", ),
        }



class OfficineDemandeType(DjangoSerializerType):
    class Meta:
        serializer_class = OfficineDemandeSerializer
        description = " Type definition for a single OfficineDemande "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "demande__id": ("exact",),
            "status": ("exact", ),
            "officine__id": ("exact",),
            "officine__circonscription__id": ("exact",),
        }


class LigneDemandeType(DjangoSerializerType):
    class Meta:
        serializer_class = LigneDemandeSerializer
        description = " Type definition for a single LigneDemande "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "demande__id": ("exact",),
            "produit__id": ("exact",),
            "status": ("exact", ),
        }


class ReponseType(DjangoSerializerType):
    class Meta:
        serializer_class = ReponseSerializer
        description = " Type definition for a single Reponse "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "demande__id": ("exact",),
            "demande__demande__id": ("exact",),
            "demande__officine__id": ("exact",),
        }


class LigneReponseType(DjangoSerializerType):
    class Meta:
        serializer_class = LigneReponseSerializer
        description = " Type definition for a single LigneReponse "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "reponse__id": ("exact",),
            "produit__id": ("exact",),
            "status": ("exact", ),
        }


class SubsLigneReponseType(DjangoSerializerType):
    class Meta:
        serializer_class = SubsLigneReponseSerializer
        description = " Type definition for a single SubsLigneReponse "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "ligne__id": ("exact",),
            "produit__id": ("exact",),
        }


class RdvLigneReponseType(DjangoSerializerType):
    class Meta:
        serializer_class = RdvLigneReponseSerializer
        description = " Type definition for a single RdvLigneReponse "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "read": ("exact", ),
            "ligne__id": ("exact",),
            "ligne__reponse__demande__demande__utilisateur__id": ("exact",),
            "days": ("exact",),
            "valide": ("exact", ),
        }

