from django.core.management.base import BaseCommand, CommandError
import os
from produitApp.models import TypeProduit, StockState
from officineApp.models import TypeOfficine
from django.contrib.auth.models import User, Group, Permission

import threading
    
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        
        print("Super admin registered")
        user = User(
            username = "admin",
            email = "",
            first_name = "Super",
            last_name = "Administrateur",
        )
        user.set_password("12345678")
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        
        datas = {
            "Médicament":"MEDICAMENT",
            "Prestation":"PRESTATION"
        }
        for x in datas:
            TypeProduit.objects.get_or_create(
                name = x, 
                etiquette = datas[x], 
            )
            
            
        datas = {
            "Disponible":"1",
            "Stock bas":"0",
            "Insdisponible":"-1",
        }
        for x in datas:
            StockState.objects.get_or_create(
                name = x, 
                etiquette = datas[x], 
            )
            
            
            
            