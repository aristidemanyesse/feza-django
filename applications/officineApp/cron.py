from .models import *
from datetime import datetime, timedelta, date

def create_garde():
    try :
        garde = Garde.objects.create(debut = date.today(), fin = date.today() + timedelta(days=7))
        for circonscription in Circonscription.objects.all()[:10]:
            total = circonscription.circonscription_officine.all().count()
            for officine in circonscription.circonscription_officine.all().order_by("?")[:round(total / 2)+1]:
                OfficineDeGarde.objects.create(officine = officine, garde = garde)
                
    except Exception as e:
        print("Error creating_garde by cron: %s" % e)
                