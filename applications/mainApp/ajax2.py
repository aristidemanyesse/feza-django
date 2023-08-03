from UserApp.models import *
from demandeApp.models import *
from django.http.response import HttpResponse, JsonResponse
import json

from produitApp.models import ProduitInOfficine

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
            produits_qte = json.loads(datas["produits_qte"])
            substituts = json.loads(datas["substituts"])
            substituts_qte = json.loads(datas["substituts_qte"])
            rdv = json.loads(datas["rdv"])
            
            produits = [x for x in prods]
            demande = OfficineDemande.objects.filter(id = datas["demande"]).first()
            produits = Produit.objects.filter(id__in = produits)
            
            if demande is not None and produits.count() > 0 :
                reponse =  Reponse.objects.create(demande=demande, commentaire = datas["comment"])
                total = 0
                for produit in produits :
                    status = prods[str(produit.id)]
                    pio, created = ProduitInOfficine.objects.get_or_create(officine=demande.officine, produit=produit)
                    ligne = LigneReponse.objects.create(reponse=reponse, produit=produit, quantite=int(produits_qte[str(produit.id)]), price = pio.price, status= status)
                    if status:
                        total += pio.price * ligne.quantite if status else 0
                    else:
                        for key, value in substituts.items():
                            if key == str(produit.id):
                                _produit = Produit.objects.get(id = value)
                                pio, created = ProduitInOfficine.objects.get_or_create(officine=demande.officine, produit=_produit)
                                sub = SubsLigneReponse.objects.create(ligne=ligne, produit=_produit, quantite = int(substituts_qte[str(produit.id)]), price = pio.price)
                                total += pio.price * sub.quantite
                                break
                        
                        for key, value in rdv.items():
                            if key == str(produit.id):
                                RdvLigneReponse.objects.create(ligne=ligne, days=value)
                                break
                        
                reponse.price = total
                reponse.save()
                
            demande.status = True
            demande.save()
            return JsonResponse({"status":True})
        
        except Exception as e :
            print("Error valider_demande: " + str(e))
            return JsonResponse({"status":False, "message":"Une erreur s'est produite lors de l'opération, veuillez recommencer !"})
