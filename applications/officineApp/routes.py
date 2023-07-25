
from .schemas import *
from .serializers import *
import graphene, requests
from django.contrib.gis.db.models.functions import Distance
from .models import *
import math
from geopy.distance import geodesic

def meters_to_degrees(metre):
    return metre * 360 / 40000000

def degrees_to_meters(degree):
    return 40000000  * degree / 360



def route_for_officine(officine, point):
    try :
        multilinestring = {"":""}
        url = f"https://router.project-osrm.org/route/v1/car/{point.x},{point.y};{officine.lat},{officine.lon}?steps=true&geometries=geojson"
        response = requests.get(url)
        multilinestring = {}
        data = response.json()
        if data['code'] == 'Ok' :
            geometry = data['routes'][0]
            geometry["type"] = "Feature"
            multilinestring = json.dumps(geometry)
        return multilinestring
    except Exception as e:
        print(f"Error generation routing for {officine.name}", e)
    
    
class OfficineDistanceType(graphene.ObjectType):
    officine = graphene.String()
    distance = graphene.Float()
    route = graphene.String()

    
    
class OfficineAppQuery(object):
    
    search_type_officine = TypeOfficineType.ListField(action=graphene.String(default_value="search_type_officine"))
    
    search_circonscription = CirconscriptionType.ListField(action=graphene.String(default_value="search_circonscription"))
    
    search_officine = OfficineType.ListField(action=graphene.String(default_value="search_officine"))
    
    search_responsable_officine = ResponsableOfficineType.ListField(action=graphene.String(default_value="search_responsable_officine"))
    
    search_garde = GardeType.ListField(action=graphene.String(default_value="search_garde"))
    
    search_officine_de_garde = OfficineDeGardeType.ListField(action=graphene.String(default_value="search_officine_de_garde"))
    
    
    search_officine_distance = graphene.List(OfficineDistanceType, id=graphene.String(), longitude=graphene.Float(), latitude=graphene.Float())
    def resolve_search_officine_distance (root, info, id, longitude, latitude, **kwargs):
        point = Point(longitude, latitude, srid=4326)
        officine = Officine.objects.filter(id = id).annotate(distance=Distance('geometry', point)).first()
        if officine is not None:
            multilinestring = route_for_officine(officine, point)            
            return OfficineDistanceType(officine = officine.id, distance = round(degrees_to_meters(officine.distance), 2), route = json.dumps(multilinestring))

    

    search_officine_avialable = graphene.List(OfficineDistanceType, longitude=graphene.Float(required = False), latitude=graphene.Float(), distance=graphene.Int(), circonscription=graphene.String())
    def resolve_search_officine_avialable (root, info, longitude, latitude, distance, circonscription, **kwargs):
        officines = []
        point = Point(longitude, latitude, srid=4326)
        if distance > 0:
            datas = Officine.objects.filter(type__etiquette = TypeOfficine.PHARMACIE).annotate(distance=Distance('geometry', point)).order_by("distance")[:distance*20]
            for officine in datas:
                if degrees_to_meters(officine.distance) <= distance * 1000:
                    officines.append(officine)
                    
        elif circonscription != "" and circonscription is not None:
            officines = Officine.objects.filter(circonscription__id = circonscription).annotate(distance=Distance('geometry', point))

        datas = []
        for officine in officines: 
            # multilinestring = {}
            multilinestring = route_for_officine(officine, point)
            data = OfficineDistanceType(officine = officine.id, distance = round(degrees_to_meters(officine.distance), 2), route = json.dumps(multilinestring))
            datas.append(data)
                        
        return datas 
    
    

    search_officine_garde_avialable = graphene.List(OfficineDistanceType, longitude=graphene.Float(required = False), latitude=graphene.Float(), distance=graphene.Int(), circonscription=graphene.String())
    def resolve_search_officine_garde_avialable (root, info, longitude, latitude, distance, circonscription, **kwargs):
        point = Point(longitude, latitude, srid=4326)
        garde = Garde.objects.filter().order_by("-created_at").first()
        datas = []
        if garde is not None:
            offs = garde.garde_officine.filter().values_list('officine__id', flat=True)
            officines = []
            if distance > 0:
                lots = Officine.objects.filter(type__etiquette = TypeOfficine.PHARMACIE, id__in = offs).annotate(distance=Distance('geometry', point)).order_by("distance")[:distance*20]
                for officine in lots:
                    if degrees_to_meters(officine.distance) <= distance * 1000:
                        officines.append(officine)
                        
            elif circonscription != "" and circonscription is not None:
                officines = Officine.objects.filter(circonscription__id = circonscription, id__in = offs).annotate(distance=Distance('geometry', point))
            
            for officine in officines: 
                multilinestring = route_for_officine(officine, point)
                data = OfficineDistanceType(officine = officine.id, distance = round(degrees_to_meters(officine.distance), 2), route = json.dumps(multilinestring))
                datas.append(data)
             
        return datas 
    

class OfficineAppMutation(object):
    # Dtm
    create_type_officine = TypeOfficineType.CreateField()
    update_type_officine = TypeOfficineType.UpdateField()

    # Dsm
    create_circonscription = CirconscriptionType.CreateField()
    update_circonscription = CirconscriptionType.UpdateField()
    
    # Dtm
    create_officine = OfficineType.CreateField()
    update_officine = OfficineType.UpdateField()

    # Dsm
    create_responsable_officine = ResponsableOfficineType.CreateField()
    update_responsable_officine = ResponsableOfficineType.UpdateField()
    
    # Dtm
    create_garde = GardeType.CreateField()
    update_garde = GardeType.UpdateField()

    # Dsm
    create_officine_de_garde = OfficineDeGardeType.CreateField()
    update_officine_de_garde = OfficineDeGardeType.UpdateField()