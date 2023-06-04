from django.core.management.base import BaseCommand, CommandError
import os, csv, json
from officineApp.models import Circonscription, Officine
from produitApp.models import Produit, TypeProduit, StockState, ProduitInOfficine
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
        ProduitInOfficine.objects.filter().delete()
        # for off in Officine.objects.all(type = TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE)):
        #     test = off.lat
        #     off.lat = off.lon
        #     off.lon = test
        #     off.save()
        #     print(off)
        
        # for pro in  ProduitInOfficine.objects.filter().order_by("?")[:1600000]:
        #     pro.stock_state = StockState.objects.get(etiquette = StockState.RUPTURE)
        #     print(pro)
        #     pro.save()
            
       
                
                
                