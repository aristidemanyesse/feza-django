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
        state = StockState.objects.get(etiquette = StockState.DISPONIBLE)
        type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT)
        for officine in Officine.objects.filter(type = TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE)):
            print("---------", officine)
            for i, produit in enumerate(Produit.objects.filter(type = type).order_by('?')[:10000]):
                print("-------------------", i, produit)
                ProduitInOfficine.objects.create(
                    officine = officine,
                    produit = produit,
                    stock_state = state
                    )
            
       
                
                
                