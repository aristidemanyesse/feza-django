
from UserApp.models import *
from demandeApp.models import *
from django.http.response import JsonResponse
from datetime import datetime

from communicateApp.models import SMS


def valider_rdv(request):
    if request.method == "POST":
        try : 
            datas = request.POST
            rdv = RdvLigneReponse.objects.filter(id = datas["id"]).first()
            if rdv is not None:
                rdv.valided_date = datetime.now()
                rdv.valide = True
                rdv.save()
                
                SMS.objects.create(
                    utilisateur = rdv.ligne.reponse.demande.demande.utilisateur,
                    message = f"INFO iPi\nLe produit `{rdv.ligne.produit.name.capitalize()}` est maintenant disponible dans votre officine: {rdv.ligne.reponse.demande.officine} - {rdv.ligne.reponse.demande.officine.circonscription}.\n Tel: {rdv.ligne.reponse.demande.officine.contact}"
                )

                return JsonResponse({"status":True})
        
        except Exception as e :
            print("Error valider_rdv: " + str(e))
            return JsonResponse({"status":False, "message":"Une erreur s'est produite lors de l'opération, veuillez recommencer !"})