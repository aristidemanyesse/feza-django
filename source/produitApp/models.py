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
    
    class Meta:
        ordering = ("name",)


class Produit(BaseModel):
    name              = models.CharField(max_length=255, default="")
    cis               = models.CharField(max_length=255, default="", null = True, blank = True,)
    forme             = models.CharField(max_length=255, default="", null = True, blank = True,)
    voies             = models.CharField(max_length=255, default="", null = True, blank = True,)
    description       = models.TextField(default="", null = True, blank = True,)
    codebarre         = models.CharField(max_length=255, unique=True)
    price             = models.IntegerField(null = True, blank = True)
    only_ordonnance   = models.BooleanField(default=False)
    type              = models.ForeignKey(TypeProduit, null = True, blank = True, on_delete= models.CASCADE, related_name="type_produit")
    image             = models.ImageField(max_length = 255, upload_to = "media/images/produits/", default="media/images/produits/default.jpg", null = True, blank=True)
    class Meta:
        ordering = ("name",)


class ProduitInOfficine(BaseModel):
    produit = models.ForeignKey(Produit, null = True, blank = True, on_delete= models.CASCADE, related_name="produit_in_officine")
    officine = models.ForeignKey(Officine, null = True, blank = True, on_delete= models.CASCADE, related_name="officine_for_produit")
    price = models.IntegerField(default=0)
    quantite = models.IntegerField(default=0)
     
    class Meta:
        ordering = ("produit__name",)
    
    def __str__(self):
        return str(self.produit.name) + " dans " + str(self.officine.name)



class Assurance(BaseModel):
    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255)
    taux = models.FloatField(default=0.0)




@signals.post_save(sender=ProduitInOfficine)
def sighandler(instance, created, **kwargs):
    if created:
        instance.price = instance.produit.price
        instance.save()
        
# @signals.post_save(sender=Officine)
# def sighandler(instance, created, **kwargs):
#     if created:
#         for produit in Produit.objects.all():
#             ProduitInOfficine.objects.create(
#                 officine = instance,
#                 produit = produit
#             )
            
            

@signals.pre_save(sender=ProduitInOfficine)
def sighandler(instance, **kwargs):
    if instance._state.adding:
        instance.stock_state = StockState.objects.get(etiquette = StockState.DISPONIBLE)
    