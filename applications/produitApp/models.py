from django.db import models
from officineApp.models import Officine
from coreApp.models import BaseModel
# Create your models here.


class StockState(BaseModel):
    DISPONIBLE = "DISPONIBLE"
    RUPTURE = "RUPTURE"
    STOCK_BAS = "STOCK_BAS"
    
    name = models.BooleanField(default=False)
    etiquette = models.BooleanField(default=False)
    
    
class TypeProduit(BaseModel):
    MEDICAMENT = "MEDICAMENT"
    PRESTATION = "PRESTATION"
    
    name = models.CharField(max_length=255,default="")
    etiquette = models.CharField(max_length=255,default="")


class Produit(BaseModel):
    name = models.CharField(max_length=255,default="")
    description = models.TextField(default="")
    codebarre = models.CharField(max_length=255)
    only_ordonnance = models.BooleanField(default=False)
    type = models.ForeignKey(TypeProduit, null = True, blank = True, on_delete= models.CASCADE, related_name="type_produit")
    image    = models.ImageField(max_length = 255, upload_to = "static/images/pays/", default="", null = True, blank=True)



class ProduitInOfficine(BaseModel):
    fullname = models.CharField(max_length=255)
    quantite = models.TextField(default="")
    stock_state = models.ForeignKey(StockState, null = True, blank = True, on_delete=models.CASCADE, related_name="stock_in_officine")
    produit = models.ForeignKey(Produit, null = True, blank = True, on_delete= models.CASCADE, related_name="produit_in_officine")
    officine = models.ForeignKey(Officine, null = True, blank = True, on_delete= models.CASCADE, related_name="officine_for_produit")



class Assurance(BaseModel):
    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255)
    taux = models.FloatField(default=0.0)

