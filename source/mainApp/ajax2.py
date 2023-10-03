from UserApp.models import *
from demandeApp.models import *
from django.http.response import HttpResponse, JsonResponse
import json, requests
from datetime import datetime
from produitApp.models import ProduitInOfficine
from settings.settings import ONESIGNAL_APP_ID, ONESIGNAL_REST_API_KEY

def send_notification_to_user(user_id, title, content):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {ONESIGNAL_REST_API_KEY}'
    }
    payload = {
        'app_id': ONESIGNAL_APP_ID,
        'include_player_ids': [user_id],
        'headings': {'fr': title},
        'contents': {'fr': content}
    }
    response = requests.post('https://onesignal.com/api/v1/notifications', json=payload, headers=headers)
    if response.status_code == 200:
        print('Notification envoyée avec succès.')
    else:
        print('Erreur lors de l\'envoi de la notification:', response.status_code, response.json())




def ajouter(request):
    if request.method == "POST":
        datas = request.POST
        produits = [ x for x in datas["produits"].split(",") if x != ""]
        print(produits, datas["produit"])
        produit = Produit.objects.filter(id = datas["produit"]).exclude(id__in = produits).first()
        response = ""
        if produit is not None:
            response = f"""                
                <tr class="odd gradeX" id="{produit.id}">
                    <td><img src="{ produit.image.url }" style="width: 20px"></td>
                    <td style="font-size:11px; font-weight:bold">{produit.name}</td>
                    <td style="font-size:11px; font-weight:bold">...</td>
                    <td style="font-size:11px; font-weight:bold">
                        <input type="number" name="qte" class="form-control input-sm" value="1" min="1" />
                    </td>
                    <td style="border-right: 3px dashed grey">
                        <input type="checkbox" class="form-control input-xs" value="" />
                    </td>
                    <td style="font-size:11px; font-weight:bold">
                        <div class="hidde">
                         
                        </div>
                    </td>
                    <td style="font-size:11px; font-weight:bold">
                        <div class="hidde">
                            <input type="number"  name="substitut_qte" class="form-control input-sm" value="1" min="1" />
                        </div>
                    </td>
                    <td style="font-size:11px; font-weight:bold">
                        <div class="hidde">
                            <select name="rdv" class="form-control selectpicker" data-size="10" data-live-search="true" data-style="btn-default" >
                                <option value="0">------------</option>
                                <option value="1">disponible demain</option>
                                <option value="2">disponible après-demain</option>
                                <option value="5">disponible dans 5 jours</option>
                                <option value="7">disponible dans 1 semaine</option>
                                <option value="14">disponible dans 2 semaine</option>
                                <option value="30">disponible dans 1 mois</option>
                                <option value="60">disponible dans 2 mois</option>
                            </select>
                        </div>
                    </td>
                </tr>                       
            """
        return HttpResponse(response)


def check_demande(request):
    if request.method == "POST":
        try:
            date_format = "%Y-%m-%d %H:%M:%S"
            date_string = request.session.get("last_checked_date")
            mydate = datetime.strptime(date_string, date_format) if date_string is not None else datetime.now()
            demandes = request.officine.officine_demande.filter(deleted=False, created_at__gte = mydate)
            request.session["last_checked_date"] = datetime.now().strftime(date_format) 
            if demandes.count() > 0:
                send_notification_to_user("2ef45a96-70c1-44bf-8f83-028a3a5ef3d9", "Nouvelle demande", "Vous avez reçu une nouvelle demande de médicaments. Veuillez cliquer ici pour y répondre.")
                return JsonResponse({"status":True})

            return HttpResponse("")
        
        except Exception as e :
            print("Error check_demande: " + str(e))
            return JsonResponse({"status":False, "message":"Problème de mise à jour des demandes !"})
        


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
                        for key in substituts:
                            value = substituts[key]
                            if key == str(produit.id) and value != "":
                                _produit = Produit.objects.get(id = value)
                                pio, created = ProduitInOfficine.objects.get_or_create(officine=demande.officine, produit=_produit)
                                sub = SubsLigneReponse.objects.create(ligne=ligne, produit=_produit, quantite = int(substituts_qte[str(produit.id)]), price = pio.price)
                                total += pio.price * sub.quantite
                                break
                        
                        for key, value in rdv.items():
                            if key == str(produit.id) and int(value) >= 1:
                                RdvLigneReponse.objects.create(ligne=ligne, days=value)
                                break
                        
                reponse.price = total
                reponse.save()
                
            demande.is_valided = True
            demande.save()
            return JsonResponse({"status":True})
        
        except Exception as e :
            print("Error valider_demande: " + str(e))
            return JsonResponse({"status":False, "message":"Une erreur s'est produite lors de l'opération, veuillez recommencer !"})
