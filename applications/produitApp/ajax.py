from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.core.serializers import serialize
from django.urls import reverse
from settings import settings as parametres
from django.utils.translation import gettext as _


from officineApp.forms import *
from produitApp.forms import *
import coreApp.tools as tools


# Create your views here.
def disponible(request):
    if request.method == "POST":
        try:
            datas = request.POST
            item, created = ProduitInOfficine.objects.get_or_create(produit = Produit.objects.get(id = datas["prod"]), officine = Officine.objects.get(id = datas["off"]))
            item.stock_state = StockState.objects.get(etiquette = StockState.DISPONIBLE)
            item.save()
            return JsonResponse({"status":True, "message":""})
        
        except Exception as e:
            print("erreur save :", e)
            return JsonResponse({"status":False, "message": _("Erreur lors du processus. Veuillez recommencer : ")+str(e)})


def indisponible(request):
    if request.method == "POST":
        try:
            datas = request.POST
            pro = ProduitInOfficine.objects.get(id = datas["item"])
            pro.delete()
            return JsonResponse({"status":True, "message":""})
        
        except Exception as e:
            print("erreur save :", e)
            return JsonResponse({"status":False, "message": _("Erreur lors du processus. Veuillez recommencer : ")+str(e)})
        
        
        

def get(request):
    if request.method == "POST":
        try:
            datas = request.POST
            pro = Produit.objects.get(id = datas["id"])
            return JsonResponse({"status":True, "data":serialize('json', [pro])}, safe=True)
        
        except Exception as e:
            print("erreur save :", e)
            return JsonResponse({"status":False, "message": _("Erreur lors du processus. Veuillez recommencer : ")+str(e)})
