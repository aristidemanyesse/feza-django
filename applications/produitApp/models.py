from django.db import models
from officineApp.models import Officine, TypeOfficine
from coreApp.models import BaseModel
# Create your models here.
from annoying.decorators import signals


class StockState(BaseModel):
    RUPTURE    = "-1"
    STOCK_BAS  = "0"
    DISPONIBLE = "1"
    
    name = models.CharField(max_length=225)
    etiquette = models.CharField(max_length=225, default="")
    classe = models.CharField(max_length=225, default="")
    
    
class TypeProduit(BaseModel):
    MEDICAMENT = "MEDICAMENT"
    PRESTATION = "PRESTATION"
    
    name = models.CharField(max_length=255,default="")
    etiquette = models.CharField(max_length=255,default="")


class Produit(BaseModel):
    name = models.CharField(max_length=255,default="")
    cis = models.CharField(max_length=255, default="")
    forme = models.CharField(max_length=255, default="")
    voies = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    codebarre = models.CharField(max_length=255, unique=True)
    only_ordonnance = models.BooleanField(default=False)
    type = models.ForeignKey(TypeProduit, null = True, blank = True, on_delete= models.CASCADE, related_name="type_produit")
    image = models.ImageField(max_length = 255, upload_to = "media/images/produits/", default="media/images/produits/default.jpg", null = True, blank=True)
    class Meta:
        ordering = ("name",)


class ProduitInOfficine(BaseModel):
    quantite = models.IntegerField(default=0)
    stock_state = models.ForeignKey(StockState, null = True, blank = True, on_delete=models.CASCADE, related_name="stock_in_officine")
    produit = models.ForeignKey(Produit, null = True, blank = True, on_delete= models.CASCADE, related_name="produit_in_officine")
    officine = models.ForeignKey(Officine, null = True, blank = True, on_delete= models.CASCADE, related_name="officine_for_produit")
    
    class Meta:
        ordering = ("produit__name", "-stock_state__etiquette")
    
    def __str__(self):
        return str(self.produit.name) + " dans " + str(self.officine.name)



class Assurance(BaseModel):
    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255)
    taux = models.FloatField(default=0.0)




@signals.post_save(sender=Produit)
def sighandler(instance, created, **kwargs):
    if created:
        for officine in Officine.objects.filter(type = TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE)):
            ProduitInOfficine.objects.create(
                officine = officine,
                produit = instance
            )
        
@signals.post_save(sender=Officine)
def sighandler(instance, created, **kwargs):
    if created:
        for produit in Produit.objects.all():
            ProduitInOfficine.objects.create(
                officine = instance,
                produit = produit
            )
            
            

@signals.pre_save(sender=ProduitInOfficine)
def sighandler(instance, **kwargs):
    if instance._state.adding:
        instance.stock_state = StockState.objects.get(etiquette = StockState.RUPTURE)
    