
from graphene_django_extras import  DjangoSerializerType
from .serializers import *


class SMSType(DjangoSerializerType):
    class Meta:
        serializer_class = SMSSerializer
        description = " Type definition for a single SMS "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "utilisateur__id": ("exact",),
            "status": ("exact", ),
            "number": ("exact", ),
        }