import uuid
from PIL import Image
from django.contrib.gis.db import models
from annoying.decorators import signals
from coreApp.models import BaseModel
from officineApp.models import Circonscription, Officine
import random
# Create your models here.


class Utilisateur(BaseModel):
    fullname        = models.CharField(max_length = 255, null = True, blank=True)
    otp             = models.CharField(max_length = 6, null = True, blank=True)
    contact         = models.CharField(max_length = 255, unique=True)
    imei         = models.CharField(max_length = 255)
    is_valide       = models.BooleanField(default = False)
    geometry        = models.PointField(srid=4326, null=True, blank=True)
    geometry_json   = models.TextField(default="")
    circonscription = models.ForeignKey(Circonscription, on_delete = models.CASCADE, related_name="circonscription_utilisateur" , null = True, blank=True)
    image           = models.ImageField(default="", upload_to = "media/images/utilisateurs/", max_length=255,  null=True, blank=True)

    class Meta:
        auto_populate = True
        number_elements_to_populate = 17
        
        
    def __str__(self):
        return str(self.fullname)



    

@signals.pre_save(sender=Utilisateur)
def sighandler(instance, **kwargs):
    # if instance._state.adding:
    code = ""
    for i in range(4):
        code += str(random.randint(0,9))
    instance.otp = code
    