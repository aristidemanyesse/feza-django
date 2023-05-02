from django.contrib.gis.db import models
from coreApp.models import BaseModel
# Create your models here.
from django.contrib.auth.models import User


class TypeOfficine(BaseModel):
    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255)


class Circonscription(BaseModel):
    name = models.CharField(max_length=255)
    geometry = models.PolygonField()


class Officine(BaseModel):
    name = models.CharField(max_length=255)
    localisation = models.TextField(default="")
    geometry = models.PointField()
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, null=True, blank=True)
    contact2 = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(TypeOfficine, null = True, blank = True, on_delete= models.CASCADE, related_name="type_officine")
    circonscription = models.ForeignKey(Circonscription, null = True, blank = True, on_delete= models.CASCADE, related_name="circonscription_officine")
    image    = models.ImageField(max_length = 255, upload_to = "static/images/pays/", default="", null = True, blank=True)
    image2    = models.ImageField(max_length = 255, upload_to = "static/images/pays/", default="", null = True, blank=True)
    image3    = models.ImageField(max_length = 255, upload_to = "static/images/pays/", default="", null = True, blank=True)




class ResponsableOfficine(User, BaseModel):
    fullname = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    officine = models.ForeignKey(Officine, null = True, blank = True, on_delete= models.CASCADE, related_name="officine_responsable")



class Garde(BaseModel):
    debut = models.DateField(default="", null=True, blank=True)
    fin = models.DateField(default="", null=True, blank=True)


class OfficineDeGarde(BaseModel):
    garde = models.ForeignKey(Garde, null = True, blank = True, on_delete= models.CASCADE, related_name="garde_officine")
    officine = models.ForeignKey(Officine, null = True, blank = True, on_delete= models.CASCADE, related_name="officine_garde")


