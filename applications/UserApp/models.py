from django.db import models
from django.contrib.auth.models import User

from coreApp.models import BaseModel
from officineApp.models import Circonscription

# Create your models here.


class Utilisateur(BaseModel):
    fullname             = models.CharField(max_length = 255, null = True, blank=True)
    telephone             = models.CharField(max_length = 255, null = True, blank=True)
    otp               = models.CharField(max_length = 6, null = True, blank=True)
    contact               = models.CharField(max_length = 255, null = True, blank=True)
    is_valide    = models.BooleanField(default = True)
    circonscription       = models.ForeignKey(Circonscription, on_delete = models.CASCADE, related_name="agence_employe")
    image                 = models.ImageField(default="default.png", upload_to = "stockage/images/employes/", max_length=255,  null=True, blank=True)

    class Meta:
        auto_populate = True
        number_elements_to_populate = 17
        
        
    def __str__(self):
        return self.fullname
