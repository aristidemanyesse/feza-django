from django.conf import settings
from produitApp.models import Produit
from django.core.management.base import BaseCommand
from officineApp.cron import create_garde
import random



class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        for produit in Produit.objects.filter(price = None):
            print(produit.name)
            produit.price = random.randint(500, 15000)
            produit.save()