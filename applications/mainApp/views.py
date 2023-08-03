from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
import json
from django.core.serializers import serialize
from django.contrib.auth import authenticate, logout
from demandeApp.models import *
from officineApp.models import TypeOfficine

from officineApp.models import Officine
from produitApp.models import *
from UserApp.models import *
from .models import *
from datetime import datetime, timedelta
# Create your views here.



        

@render_to('mainApp/login.html')
def connexion(request):
    if request.method == "GET":
        logout(request)
        if 'locked' in request.session:
            del request.session['locked']
            
        return {}
        
        

@render_to('mainApp/locked.html')
def locked(request):
    if request.method == "GET":
        request.session['locked'] = True
        if "last_url" not in request.session:
            request.session['last_url'] = request.META["HTTP_REFERER"]
        return render(request, "auth/pages/locked.html")
        


def deconnexion(request):
    if request.method == "GET":
        return redirect("mainApp:login") 
        
        
        
@render_to('mainApp/dashboard.html')
def dashboard(request):
    if not request.user.is_superuser:
        return redirect("mainApp:dashboard_officine", request.officine.id)
        
    if request.method == "GET":
        officines = Officine.objects.filter(deleted = False, type  = TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE))
        markers = json.loads(serialize("geojson", officines))
        produits = Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT))
        users = Utilisateur.objects.filter(deleted = False)
        demandes = Demande.objects.filter(deleted = False, created_at__date= datetime.today())
        ctx = {
            "officines": officines,
            "produits": produits,
            "users": users,
            "demandes": demandes,
            "markers": markers
        }
        return ctx
        



        
@render_to('mainApp/dashboard_officine.html')
def dashboard_officine(request, id):
    if request.method == "GET":
        officine = get_object_or_404(Officine, pk=id)
        demandes = officine.officine_demande.filter(deleted = False, status = False, created_at__date= datetime.today())
        produits = Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT))
        ctx = {
            "officine": officine,
            "produits": produits,
            "officinedemandes": demandes,
        }
        return ctx
          
        