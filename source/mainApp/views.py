from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
import json, os
from django.core.serializers import serialize
from django.contrib.auth import authenticate, logout
from demandeApp.models import *
from officineApp.models import TypeOfficine, Officine
from produitApp.models import *
from UserApp.models import *
from settings.settings import BASE_DIR
from .models import *
from datetime import datetime, timedelta
from collections import defaultdict

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
        officines   = Officine.objects.filter(deleted = False, type  = TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE))
        markers     = json.loads(serialize("geojson", officines))
        produits    = Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT))
        users       = Utilisateur.objects.filter(deleted = False)
        demandes    = Demande.objects.filter(deleted = False, created_at__gte = datetime.now() - timedelta(days=7))
        
        demandes_validees = demandes.filter(is_finished = True)
        demandes_ignorees = demandes.exclude(is_finished = True)

        
        demandes_par_mois = {}
        validees_par_mois = {}

        # Parcourir les ventes et agréger par mois
        for demande in Demande.objects.filter(deleted = False).order_by('created_at'):
            date_demande = datetime.strptime(str(demande.created_at.date()), "%Y-%m-%d")
            mois_demande = date_demande.strftime("%Y-%m")  # Nom du mois en français
            try:
                demandes_par_mois[mois_demande] += 1
                validees_par_mois[mois_demande] += 1 if demande.is_finished else 0
            except KeyError:
                demandes_par_mois[mois_demande] = 0
                validees_par_mois[mois_demande] = 0
                
        ctx = {
            "officines": officines,
            "produits": produits,
            "users": users,
            "demandes": demandes,
            "markers": markers,
            "demandes_validees": demandes_validees,
            "demandes_ignorees": demandes_ignorees,
            "demandes_par_mois": demandes_par_mois,
            "validees_par_mois": validees_par_mois,
        }
        return ctx
        



        
        
@render_to('mainApp/dashboard_officine.html')
def dashboard_officine(request, id):
    if request.method == "GET":
        officine = get_object_or_404(Officine, pk=id)
        demandes = officine.officine_demande.filter(deleted = False, propagated = True)
        demandes_semaine = demandes.filter(deleted = False, created_at__gte = datetime.now() - timedelta(days=7))
        
        demandes_validees = demandes_semaine.filter(is_valided = True)
        demandes_ignorees = demandes_semaine.exclude(is_valided = True)
        
        produits = Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT))
                
        # Obtenir la date actuelle
        # Initialiser un dictionnaire pour stocker le total des ventes par mois
        demandes_par_mois = {}
        validees_par_mois = {}

        # Parcourir les ventes et agréger par mois
        for demande in demandes.order_by('created_at'):
            date_demande = datetime.strptime(str(demande.created_at.date()), "%Y-%m-%d")
            mois_demande = date_demande.strftime("%Y-%m")  # Nom du mois en français
            try:
                demandes_par_mois[mois_demande] += 1
                validees_par_mois[mois_demande] += 1 if demande.is_valided else 0
            except KeyError:
                demandes_par_mois[mois_demande] = 0
                validees_par_mois[mois_demande] = 0


        ctx = {
            "officine": officine,
            "produits": produits,
            "officinedemandes": demandes.filter(created_at__gte = datetime.now() - timedelta(days=1), is_valided = None).order_by('-created_at'),
            "demandes_semaine": demandes_semaine,
            "demandes_validees": demandes_validees,
            "demandes_ignorees": demandes_ignorees,
            "demandes_par_mois": demandes_par_mois,
            "validees_par_mois": validees_par_mois,
        }
        
        for dem in officine.officine_demande.filter(created_at__lte = datetime.now() - timedelta(days=1), is_valided = None):
            dem.is_valided = False
            dem.save()
            
        return ctx
          
        