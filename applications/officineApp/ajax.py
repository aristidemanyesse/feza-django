
from UserApp.models import *
from demandeApp.models import *
from django.http.response import HttpResponse, JsonResponse
from datetime import datetime
import json


def valider_rdv(request):
    if request.method == "POST":
        try : 
            datas = request.POST
            rdv = RdvLigneReponse.objects.filter(id = datas["id"]).first()
            if rdv is not None:
                rdv.valided_date = datetime.now()
                rdv.valide = True
                rdv.save()

                return JsonResponse({"status":True})
        
        except Exception as e :
            print("Error valider_demande: " + str(e))
            return JsonResponse({"status":False, "message":"Une erreur s'est produite lors de l'opération, veuillez recommencer !"})