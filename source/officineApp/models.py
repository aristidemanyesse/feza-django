import base64
import random
import uuid
from django.contrib.gis.db import models
from coreApp.models import BaseModel
# Create your models here.
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point, Polygon
from annoying.decorators import signals
import osm2geojson
import json
from django.core.files.base import ContentFile


class TypeOfficine(BaseModel):
    PHARMACIE   = "PHARMACIE"
    OFFICINE    = "OFFICINE"
    LABORATOIRE = "LABORATOIRE"
    CLINIQUE    = "CLINIQUE"
    
    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255)


class Circonscription(BaseModel):
    name = models.CharField(max_length=255)
    xml           = models.TextField(default="", null = True, blank=True)
    geometry = models.PolygonField(srid=4326, default=Polygon( ((0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)) ), blank=True)
    geometry_json        = models.TextField(default="", null = True, blank=True)
    
    class Meta:
        ordering = ("name",)


class Officine(BaseModel):
    name            = models.CharField(max_length=255)
    localisation    = models.TextField(default="", null=True, blank=True)
    geometry        = models.PointField(default="", srid=4326, blank=True)
    geometry_json   = models.TextField(default="", null=True, blank=True)
    lon             = models.FloatField(default=0.0, null=True, blank=True)
    lat             = models.FloatField(default=0.0, null=True, blank=True)
    contact         = models.CharField(max_length=255, null=True, blank=True)
    contact2        = models.CharField(max_length=255, null=True, blank=True)
    type            = models.ForeignKey(TypeOfficine, null = True, blank = True, on_delete= models.CASCADE, related_name="type_officine")
    circonscription = models.ForeignKey(Circonscription, null = True, blank = True, on_delete= models.SET_NULL, related_name="circonscription_officine")
    base64          = models.TextField(default="", null=True, blank=True)
    image           = models.ImageField(max_length = 255, upload_to = "media/images/officines/", default="", null = True, blank=True)
    image2          = models.ImageField(max_length = 255, upload_to = "media/images/officines/", default="", null = True, blank=True)
    image3          = models.ImageField(max_length = 255, upload_to = "media/images/officines/", default="", null = True, blank=True)

    class Meta:
        ordering = ("name",)



class ResponsableOfficine(User, BaseModel):
    fullname = models.CharField(max_length=255, null = True, blank = True,)
    contact = models.CharField(max_length=255, null = True, blank = True,)
    is_never_connected = models.BooleanField(default=True)
    officine = models.ForeignKey(Officine, null = True, blank = True, on_delete= models.CASCADE, related_name="officine_responsable")


class Garde(BaseModel):
    debut = models.DateField(default="", null=True, blank=True)
    fin = models.DateField(default="", null=True, blank=True)

    def __str__(self):
        return "Garde du " + str(self.debut) + " au " + str(self.fin)

    class Meta:
        ordering = ("-created_at", "-debut",)


class OfficineDeGarde(BaseModel):
    garde = models.ForeignKey(Garde, null = True, blank = True, on_delete= models.CASCADE, related_name="garde_officine")
    officine = models.ForeignKey(Officine, null = True, blank = True, on_delete= models.CASCADE, related_name="officine_garde")
    
    def __str__(self):
        return "Garde de " + str(self.officine) + " pour " + str(self.garde)






@signals.pre_save(sender=Officine)
def sighandler(instance, **kwargs):
    instance.geometry = Point(instance.lat, instance.lon)
    instance.geometry_json = instance.geometry.geojson
        
    if instance.base64 != "":
        header, encoding_string = instance.base64.split(",", 1)
        ext = header.split('/')[-1]
        img_bytes = base64.b64decode(encoding_string)
        instance.image = ContentFile(base64.b64decode(encoding_string), name=f'{uuid.uuid4()}.png')


@signals.post_save(sender=Officine)
def sighandler(instance, created, **kwargs):
    if created:
        code = "ipi"
        for i in range(9):
            code += str(random.randint(0,9))        
        respo = ResponsableOfficine.objects.create(
            officine = instance,
            fullname = "...",
            username = code,
            contact = ""
        )
        respo.set_password("ipipass")
        respo.save()
        



@signals.pre_save(sender=Circonscription)
def sighandler(instance, **kwargs):
    if instance.xml != "":
        geojson = osm2geojson.xml2geojson(instance.xml, filter_used_refs=False, log_level='INFO')
        print(geojson)
        # geometry = GEOSGeometry(geojson)
        # print(geometry)
        # instance.geometry = geometry
        # instance.geometry_json = instance.geometry.geojson