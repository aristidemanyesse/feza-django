from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
import json, uuid
from django.urls import reverse
from settings import settings as parametres
from django.utils.translation import gettext as _


from officineApp.forms import *
from produitApp.forms import *
import coreApp.tools as tools


# Create your views here.
def changeState(request):
    if request.method == "POST":
        try:
            datas = request.POST
            pro = ProduitInOfficine.objects.get(id = datas["item"])
            pro.stock_state = StockState.objects.get(id = datas["state"])
            pro.save()
            
            print(pro)
            return JsonResponse({"status":True, "message":""})
        
        except Exception as e:
            print("erreur save :", e)
            return JsonResponse({"status":False, "message": _("Erreur lors du processus. Veuillez recommencer : ")+str(e)})
