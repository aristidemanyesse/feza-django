from produitApp.models import Produit
from settings.settings import BASE_DIR
from .models import *
import json, os


def produits_list():
    try :
        datas = {}
        for produit in Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT)):
            datas[str(produit.id)] =produit.name
            
        path = os.path.join(BASE_DIR, "static/administrations/medicaments.json")
        with open(path, "w") as filename:
            filename.write(json.dumps(datas))
            
    except Exception as e:
        print("Error produits_list by cron: %s" % e)
               