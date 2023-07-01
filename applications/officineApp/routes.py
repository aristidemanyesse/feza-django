
from .schemas import *
from .serializers import *
import graphene, requests
from django.contrib.gis.db.models.functions import Distance
import math
from geopy.distance import geodesic




def distance_to_decimal_degrees(distance, latitude):
    lat_radians = latitude * (math.pi / 180)
    # 1 longitudinal degree at the equator equal 111,319.5m equiv to 111.32km
    return distance.m / (111_319.5 * math.cos(lat_radians))



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
            response = requests.get(url)
            multilinestring = {}
            data = response.json()
            if data['code'] == 'Ok':
                geometry = data['routes'][0]
                geometry["type"] = "Feature"
                multilinestring = json.dumps(geometry)
            
            data = {"officine": officine, "distance": round(officine.distance*100, 2)}
            url = f"https://router.project-osrm.org/route/v1/car/{point.x},{point.y};{officine.lat},{officine.lon}?steps=true&geometries=geojson"
            
            return OfficineDistanceType(officine = officine.id, distance = officine.distance, route = json.dumps(multilinestring))

    

    search_officine_avialable = graphene.List(OfficineDistanceType, longitude=graphene.Float(required = False), latitude=graphene.Float(), distance=graphene.Int(), circonscription=graphene.UUID())
    def resolve_search_officine_avialable (root, info, longitude, latitude, distance, circonscription, **kwargs):
        print("Resolving hello world...", longitude, latitude, distance, circonscription)
        if distance > 0:
            point = Point(longitude, latitude, srid=4326)
            officines = Officine.objects.annotate(distance=Distance('geometry', point)).filter(type__etiquette = TypeOfficine.PHARMACIE).order_by("distance")[:10]
        else:
            officines = Officine.objects.filter(circonscription__id = circonscription)
        
        datas = []
        print(officines.count())
        for officine in officines: 
            try:
                
                multilinestring = {"":""}
                # url = f"https://router.project-osrm.org/route/v1/car/{point.x},{point.y};{officine.lat},{officine.lon}?steps=true&geometries=geojson"
                # response = requests.get(url)
                # multilinestring = {}
                # data = response.json()
                # if data['code'] == 'Ok' :
                #     geometry = data['routes'][0]
                #     geometry["type"] = "Feature"
                #     multilinestring = json.dumps(geometry)
                
                data = OfficineDistanceType(officine = officine.id, distance = round(officine.distance*100, 2), route = json.dumps(multilinestring))
                datas.append(data)
            except Exception as e:
                print(f"Error generation routing for {officine.name}", e)
                        
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