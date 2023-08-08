from officineApp.routes import degrees_to_meters
from demandeApp.models import Demande
from .models import *
import time, math
from datetime import datetime, timedelta, date
from django.contrib.gis.db.models.functions import Distance

def create_garde():
    try :
        garde = Garde.objects.create(debut = date.today(), fin = date.today() + timedelta(days=7))
        for circonscription in Circonscription.objects.all()[:10]:
            total = circonscription.circonscription_officine.all().count()
            for officine in circonscription.circonscription_officine.all().order_by("?")[:round(total / 2)+1]:
                OfficineDeGarde.objects.create(officine = officine, garde = garde)
                
    except Exception as e:
        print("Error creating_garde by cron: %s" % e)
                
                


def propagation_demande():
    try :
        demandes = Demande.objects.filter(deleted=False, is_finished = False)
        for demande in demandes:
            propagate(demande)
    except Exception as e:
        print("Error creating_garde by cron: %s" % e)
                
                
                
def propagate(demande):
    print("Propagating")
    demande.propagating = True
    # demande.save()

    mon_point = Point(demande.lon, demande.lat, srid=4326)
    off_dem = demande.demande_officine.filter(deleted=False, propagated = False).annotate(distance=Distance('officine__geometry', mon_point)).order_by('distance')
    if off_dem.count() == 0:
        demande.is_finished = True
        demande.save()
        return True
    
    distance_plus_eloinée = round(degrees_to_meters(off_dem.last().distance), 2)
    print("official {} distance {}".format(off_dem.count(), distance_plus_eloinée))
    if distance_plus_eloinée <= 1500:
        print("distance inférieure à 1500")
        for off in off_dem:
            off.propagated = True
            off.save()
        demande.is_finished = True
        demande.save()
        
    else:
        print("distance superieure à 1500")
        rayon = 1500
        minutes = 0.5
        tours = math.ceil(distance_plus_eloinée / rayon)
        i = 1
        demande.demande_officine.filter(deleted=False, propagated = False).update(propagated=True)
        while i <= tours:
            print("tour ", i)
            for off in off_dem:
                if ((i-1) * rayon) < round(degrees_to_meters(off.distance), 2) <= (i * rayon):
                    print("----------------------------", off.officine , round(degrees_to_meters(off.distance), 2))
                    off.propagated = True
                    off.save()
            i += 1
            time.sleep(60 * minutes)
            
        demande.is_finished = True
        demande.save()
