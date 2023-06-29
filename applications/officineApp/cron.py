from .models import *
from datetime import datetime, timedelta

def create_garde():
    try :
        garde = Garde.objects.create(debut = datetime.today, fin = datetime.today + timedelta(days=7))
        print("---------------------------", garde)
        for circonscription in Circonscription.objects.all():
            total = circonscription.circonscription_officine.all().count()
            for officine in circonscription.circonscription_officine.all().order_by("?")[:int(total / 2)+1]:
                OfficineDeGarde.objects.create(officine = officine, garde = garde)
                
    except Exception as e:
        print("Error creating_garde by cron: %s" % e)
                