import base64
import uuid
from django.db import models
from UserApp.models import Utilisateur
from django.core.files.base import ContentFile
from coreApp.models import BaseModel
from officineApp.models import Officine
from produitApp.models import Produit
from annoying.decorators import signals
# Create your models here.



class Demande(BaseModel):
    utilisateur   = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, related_name="utilisateur_demande")
    status        = models.BooleanField(default= False)
    ordonnance    = models.ImageField(default="", upload_to = "media/images/demandes/", max_length=255, null=True, blank=True)
    base64        = models.TextField(default="", null=True, blank=True)
    commentaire   = models.TextField(default = "", null=True, blank=True)
    lon           = models.FloatField(default=0.0, null=True, blank=True)
    lat           = models.FloatField(default=0.0, null=True, blank=True)
    propagating   = models.BooleanField(default=False)
    is_finished   = models.BooleanField(default=False)
    is_satisfied  = models.BooleanField(default=False)
        
    def __str__(self):
        return "demande de " + str(self.utilisateur)
    

class OfficineDemande(BaseModel):
    demande       = models.ForeignKey(Demande, on_delete = models.CASCADE, related_name="demande_officine")
    officine      = models.ForeignKey(Officine, on_delete = models.CASCADE, related_name="officine_demande")
    is_valided    = models.BooleanField(null=True, blank=True)
    propagated    = models.BooleanField(default=False)
        
    def __str__(self):
        return str(self.demande) + " dans " + str(self.officine)
    
    

class LigneDemande(BaseModel):
    demande   = models.ForeignKey(Demande, on_delete = models.CASCADE, related_name="demande_lignes")
    produit   = models.ForeignKey(Produit, on_delete = models.CASCADE, related_name="produit_ligne")
    quantite  = models.IntegerField(default=1)
    status    = models.BooleanField(default= False)
        
    def __str__(self):
        return str(self.produit) + " pour " + str(self.demande)
    
    
   


class Reponse(BaseModel):
    demande       = models.ForeignKey(OfficineDemande, on_delete = models.CASCADE, related_name="demande_reponse")
    commentaire   = models.TextField(default = "", null=True, blank=True)
    price         = models.IntegerField(default= 0)
    read          = models.BooleanField(default= False)
        
    def __str__(self):
        return "Reponse pour " + str(self.id)
    

class LigneReponse(BaseModel):
    reponse   = models.ForeignKey(Reponse, on_delete = models.CASCADE, related_name="reponse_lignes")
    produit   = models.ForeignKey(Produit, on_delete = models.CASCADE, related_name="produit_ligne_reponse")
    price     = models.IntegerField(default= 0)
    quantite  = models.IntegerField(default=1)
    status    = models.BooleanField(default= False)
    
    class Meta:
        ordering = ("produit__name",)
        
    def __str__(self):
        return str(self.produit) + " pour " + str(self.reponse)


class SubsLigneReponse(BaseModel):
    ligne    = models.ForeignKey(LigneReponse, on_delete = models.CASCADE, related_name="lignes_sub")
    produit  = models.ForeignKey(Produit, on_delete = models.CASCADE, related_name="produit_subs_ligne_reponse")
    price    = models.IntegerField(default= 0)
    quantite = models.IntegerField(default=1)
        
    def __str__(self):
        return str(self.produit) + " pour " + str(self.ligne)


class RdvLigneReponse(BaseModel):
    ligne           = models.ForeignKey(LigneReponse, on_delete = models.CASCADE, related_name="rdv_ligne")
    days            = models.IntegerField(default=1)
    read            = models.BooleanField(default= False)
    valide          = models.BooleanField(default= False)
    valided_date    = models.DateTimeField(null=True, blank=True)
        
    def __str__(self):
        return "Rdv pour " + str(self.ligne)
    




@signals.pre_save(sender=Demande)
def sighandler(instance, **kwargs):
    if instance._state.adding:
        if instance.base64 != "":
            header, encoding_string = instance.base64.split(",", 1)
            ext = header.split('/')[-1]
            img_bytes = base64.b64decode(encoding_string)
            instance.ordonnance = ContentFile(base64.b64decode(encoding_string), name=f'{uuid.uuid4()}.png')
    