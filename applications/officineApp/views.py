from django.shortcuts import render
from annoying.decorators import render_to
from officineApp.models import *
import json
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