from django.shortcuts import render
from annoying.decorators import render_to
from demandeApp.models import Demande, RdvLigneReponse
from officineApp.routes import degrees_to_meters
from officineApp.models import *
import json
from django.db.models import F

from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import redirect, get_object_or_404
from django.core.serializers import serialize
# Create your views here.




@render_to('officineApp/liste.html')
def liste(request):
    if request.method == "GET":
        officines = Officine.objects.filter(deleted = False, type =TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE))
        ctx = {
            "officines" : officines
        }
        return ctx

        

@render_to('officineApp/map.html')
def map(request):
    if request.method == "GET":
        circonscriptions = Circonscription.objects.filter(deleted = False)
        datas  = []
        for cir in circonscriptions:
            item = {}
            item["id"] = cir.id
            item["name"] = cir.name
            item["officines"] = json.loads(serialize("geojson", Officine.objects.filter(deleted = False, circonscription=cir))) 
            datas.append(item)
        
        officines = Officine.objects.filter(deleted = False, type =TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE))
        ctx = {
            "circonscriptions" : circonscriptions,
            "officines" : officines,
            "datas" : datas,
        }
        return ctx
        

@render_to('officineApp/officine.html')
def officine(request, id):
    if request.method == "GET":
        officine =  get_object_or_404(Officine, id = id, deleted = False, type =TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE))
        ctx = {
            "officine" : officine,
            "datas" : [json.loads(serialize("geojson", [officine]))],
        }
        return ctx

        

@render_to('officineApp/responsables.html')
def responsables(request):
    if request.method == "GET":
        medicaments = Officine.objects.filter()
        ctx = {
            "medicaments" : medicaments
        }
        return ctx
    
    

    
    

@render_to('officineApp/demandes.html')
def demandes(request, id):
    if request.method == "GET":
        officine = get_object_or_404(Officine, pk=id)
        demandes = officine.officine_demande.filter(deleted = False).order_by("-created_at")
        for demande in demandes:
            demande.distance = demande.officine.geometry.distance(Point(demande.demande.lon, demande.demande.lat, srid=4326))
            demande.distance = round(degrees_to_meters(demande.distance), 2)
            if demande.distance < 1000:
                demande.distance = f"{demande.distance} m"
            else:
                demande.distance = f"{round(demande.distance / 1000, 1)} km"
        ctx = {
            "demandes" : demandes,          
        }
        return ctx
    

    
    

@render_to('officineApp/demandes_genarales.html')
def demandes_genarales(request):
    if request.method == "GET":
        demandes = Demande.objects.filter(deleted = False).order_by("-created_at")
        ctx = {
            "demandes" : demandes,          
        }
        return ctx

    
    

@render_to('officineApp/rdv.html')
def rdv(request, id):
    if request.method == "GET":
        officine = get_object_or_404(Officine, pk=id)
        rdv = RdvLigneReponse.objects.filter(deleted =False, ligne__reponse__demande__officine = officine).order_by("-created_at", "valide")
        ctx = {
            "rdv" : rdv,          
        }
        return ctx