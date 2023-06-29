from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point, Polygon
from annoying.decorators import signals
from produitApp.models import Produit, StockState
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
    image           = models.ImageField(default="media/images/utilisateurs/default.jpg", upload_to = "media/images/utilisateurs/", max_length=255,  null=True, blank=True)

    class Meta:
        auto_populate = True
        number_elements_to_populate = 17
        
        
    def __str__(self):
        return str(self.fullname)




class Demande(BaseModel):
    utilisateur   = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, related_name="utilisateur_demande")
    officine      = models.ForeignKey(Officine, on_delete = models.CASCADE, related_name="officine_demande")
    status        = models.BooleanField(default= False)
    ordonnance    = models.ImageField(default="media/images/demandes/default.jpg", upload_to = "media/images/demandes/", max_length=255, null=True, blank=True)
    commentaire   = models.TextField(default = "")
        
    def __str__(self):
        return "demande de " + str(self.utilisateur) + " pour " + self.officine
    

class LigneDemande(BaseModel):
    demande         = models.ForeignKey(Demande, on_delete = models.CASCADE, related_name="demande_lignes")
    produit         = models.ForeignKey(Produit, on_delete = models.CASCADE, related_name="produit_ligne")
    status        = models.BooleanField(default= False)
    commentaire     = models.TextField(default = "")
        
    def __str__(self):
        return str(self.produit) + " pour " + self.demande
    
    
   
   
    

@signals.pre_save(sender=Utilisateur)
def sighandler(instance, **kwargs):
    if instance._state.adding:
        code = ""
        for i in range(4):
            code += str(random.randint(0,9))
        instance.otp = code
    
