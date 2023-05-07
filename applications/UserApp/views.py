from django.shortcuts import render
import json
from django.core.serializers import serialize
# Create your views here.
from annoying.decorators import render_to
from UserApp.models import *
from officineApp.models import Officine

# Create your views here.




@render_to('UserApp/liste.html')
def liste(request):
    if request.method == "GET":
        utilisateurs = Utilisateur.objects.filter()
        ctx = {
            "utilisateurs" : utilisateurs
        }
        return ctx

        

@render_to('UserApp/map.html')
def utilisateur(request):
    if request.method == "GET":
        medicaments = Utilisateur.objects.filter()
        ctx = {
            "medicaments" : medicaments
        }
        return ctx
        

@render_to('UserApp/map.html')
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
        
        officines = Officine.objects.filter(deleted = False)
        ctx = {
            "circonscriptions" : circonscriptions,
            "officines" : officines,
            "datas" : datas,
        }
        return ctx