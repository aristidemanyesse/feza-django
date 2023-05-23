from django.core.management.base import BaseCommand, CommandError
import os, csv, json
from officineApp.models import Circonscription, Officine
from produitApp.models import TypeProduit, StockState, ProduitInOfficine
from officineApp.models import TypeOfficine
from django.contrib.auth.models import User, Group, Permission
from settings import settings

def indexof(list, str):
    try:
        return list.index(str)
    except :
        return -1


def get(datas, header, key):
    try:
        index = indexof(header, key)
        if index >= 0:
            if index > len(header):
                return "erreur 1"
            return datas[index].lstrip() or None
        return "erreur3"
    except Exception as e:
        print(e)
        return "erreur4"
        
        
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    
    def handle(self, *args, **options):
        # for off in Officine.objects.all():
        #     test = off.lat
        #     off.lat = off.lon
        #     off.lon = test
        #     off.save()
        #     print(off)
        
        for pro in  ProduitInOfficine.objects.filter().order_by("?")[:16000]:
            pro.stock_state = StockState.objects.get(etiquette = StockState.RUPTURE)
            print(pro)
            pro.save()
            
        # path = os.path.join(settings.BASE_DIR, "static/administrations/hospitaux-de-cote-d'ivoire.csv") 
        # with open(path, 'rt', encoding = 'utf-8') as f:
        #     data = csv.reader(f)
        #     i = 0
        #     for row in data:
        #         if i == 0:
        #             header = row[0].split(';')
        #             i = 1
        #             continue
                
        #         row         = str(row).split(';')
        #         name        = get(row, header, "Nom de l'établissement").replace("']", "") or ""
        #         coordonnees = get(row, header, "geometry") or ""
        #         coordonnees = coordonnees.replace("'", "").replace('"', "")
        #         circonsp    = get(row, header, "Ville et commune") or get(row, header, "Quartier") or "---"
        #         categorie   = get(row, header, "Catégorie")
        #         coordonnees = coordonnees.split(",")
                
        #         type, created = TypeOfficine.objects.get_or_create(name = categorie)
        #         circonscription, created = Circonscription.objects.get_or_create(name = circonsp)
        #         officine, created = Officine.objects.get_or_create(type = type, circonscription=circonscription,name = name, lat=float(coordonnees[0]), lon=float(coordonnees[1]), localisation=get(row, header, "Quartier"))
                
        #         print(officine, " créée !")
                