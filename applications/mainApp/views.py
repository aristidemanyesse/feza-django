from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
from django.http import HttpResponseRedirect
import json
from django.core.serializers import serialize
from django.contrib.auth import authenticate, logout
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
    if request.method == "GET":
        officines = Officine.objects.filter(deleted = False, type  = TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE))
        produits = Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT))
        users = Utilisateur.objects.filter(deleted = False)
        markers = json.loads(serialize("geojson", officines))
        ctx = {
            "officines": officines,
            "produits": produits,
            "users": users,
            "markers": markers
        }
        return ctx
        
        
        
# @render_to('fixtureApp/match.html')
# def match(request, id):
#     if request.method == "GET":
#         match = Match.objects.get(id=id)
#         predictions = match.prediction_match.filter()
#         scores = match.predictionscore_match.filter()
        
#         home_last_matchs = match.home.get_last_matchs(match, number = 10, edition = True)
#         home_last_forms = match.home.get_last_form(match, number = 5, edition = True)
        
#         away_last_matchs = match.away.get_last_matchs(match, number = 10, edition = True)
#         away_last_forms = match.away.get_last_form(match, number = 5, edition = True)
        
#         home_facts = match.match_facts.filter(team = match.home)
#         away_facts = match.match_facts.filter(team = match.away)
        
#         stats_home = match.get_home_before_stats()
#         stats_away = match.get_away_before_stats()
        
#         confrontations        = Match.objects.filter(id__in = eval(stats_home.list_confrontations)).order_by("-date")
#         similaires_ppg        = Match.objects.filter(id__in = eval(stats_home.list_similaires_ppg)).order_by("-date")
#         similaires_ppg2       = Match.objects.filter(id__in = eval(stats_home.list_similaires_ppg2)).order_by("-date")
#         similaires_betting    = Match.objects.filter(id__in = eval(stats_home.list_similaires_betting)).order_by("-date")
#         list_intercepts       = Match.objects.filter(id__in = eval(stats_home.list_intercepts)).order_by("-date")
        
#         home_rank = LigneRanking.objects.filter(team = match.home, ranking__date__lte = match.date).order_by('-ranking__date').first()
#         away_rank = LigneRanking.objects.filter(team = match.away, ranking__date__lte = match.date).order_by('-ranking__date').first()
                
#         rank = match.edition.edition_rankings.filter(date__lte = match.date).order_by('-date').first()
#         competitionstats = match.edition.edition_stats.filter(ranking__date__lte = match.date).order_by('-created_at').first()
#         extra_infos = match.get_extra_info_match()

#         ctx = {
#             "match"                 : match,
#             "confrontations"        : confrontations[:10],
#             "similaires_ppg"        : similaires_ppg,
#             "similaires_ppg2"       : similaires_ppg2,
#             "similaires_betting"    : similaires_betting,
#             "list_intercepts"       : list_intercepts,
#             "predictions"           : predictions,
#             "scores"                : scores,
#             "home_last_matchs"      : home_last_matchs,
#             "home_last_forms"       : home_last_forms,
#             "away_last_matchs"      : away_last_matchs,
#             "away_last_forms"       : away_last_forms,
#             "home_facts"            : home_facts,
#             "away_facts"            : away_facts,
#             "extra_infos"           : extra_infos,
#             "rank"                  : rank,
#             "home_rank"             : home_rank,
#             "away_rank"             : away_rank,
#             "stats_home"            : stats_home,
#             "stats_away"            : stats_away,
#             "competitionstats"      : competitionstats,
#         }
#         return ctx






# @render_to('fixtureApp/index_test.html')
# def features_test(request, ):
#     if request.method == "GET":
#         type = TypePrediction.get("1")
#         datas = PredictionTest.objects.filter(is_checked = False, type = type).values_list('match__id')
#         matchs = Match.objects.filter(id__in = datas)
        
#         ctx = {
#             "matchs"        : matchs,
#         }
#         return ctx
    