# runapscheduler.py
import logging

from django.conf import settings
from produitApp.models import Produit, ProduitInOfficine

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from officineApp.cron import create_garde
import random



class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        ProduitInOfficine.objects.all().delete()
        for produit in Produit.objects.all():
            print(produit.name)
            produit.price = random.randint(500, 15000)
            produit.save()