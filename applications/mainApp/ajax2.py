from UserApp.models import *
from django.http.response import HttpResponse, JsonResponse
import json

def ajouter(request):
    if request.method == "POST":
        datas = request.POST
        produits = datas["produits"].split(",")
        produit = Produit.objects.filter(id = datas["produit"]).exclude(id__in = produits).first()
        response = ""
        if produit is not None:
            response = f"""
                <tr class="odd gradeX" id="{produit.id }">
                    <td><img src="{produit.image.url}" style="width: 20px"></td>
                    <td style="font-size:11px; font-weight:bold">{produit.name }</td>
                    <td>
                        <input type="checkbox" class="form-control input-xs" value="" />
                    </td>
                </tr>
            """
        return HttpResponse(response)



def valider_demande(request):
    if request.method == "POST":
        try : 
            datas = request.POST
            prods = json.loads(datas["produits"])
            produits = [x for x in prods]
            demande = Demande.objects.filter(id = datas["demande"]).first()
            produits = Produit.objects.filter(id__in = produits)
            
            if demande is not None and produits.count() > 0 :
                reponse =  Reponse.objects.create(demande=demande, commentaire = datas["comment"])
                for produit in produits :
                    LigneReponse.objects.create(reponse=reponse, produit=produit, status= prods[str(produit.id)])
            
            demande.status = True
            demande.save()
            return JsonResponse({"status":True})
        
        except Exception as e :
            print("Error valider_demande: " + str(e))
            return JsonResponse({"status":False, "message":_("Une erreur s'est produite lors de l'opération, veuillez recommencer !")})
