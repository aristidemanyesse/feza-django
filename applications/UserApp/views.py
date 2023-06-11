import json
from django.shortcuts import get_object_or_404

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

        

@render_to('UserApp/utilisateur.html')
def utilisateur(request, id):
    if request.method == "GET":
        utilisateur = get_object_or_404(Utilisateur, pk = id )
        ctx = {
            "utilisateur" : utilisateur
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
            item["utiliateurs"] = json.loads(serialize("geojson", Utilisateur.objects.filter(deleted = False, circonscription=cir))) 
            datas.append(item)
        
        utilisateurs = Utilisateur.objects.filter(deleted = False)
        ctx = {
            "circonscriptions" : circonscriptions,
            "utilisateurs" : utilisateurs,
            "datas" : datas,
        }
        return ctx