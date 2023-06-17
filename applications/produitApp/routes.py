
from officineApp.models import Circonscription, TypeOfficine
from officineApp.schemas import OfficineType
from .schemas import *
from .serializers import *
import graphene, json, requests, geojson
from django.contrib.gis.geos import Point, Polygon
from graphene_django import DjangoObjectType
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

class ProduitsAvialableInOfficineType(graphene.ObjectType):
    officine = graphene.String()
    produits = graphene.List(graphene.String)
    ratio = graphene.Int()
    distance = graphene.Float()
    route = graphene.String()

    
class ProduitAppQuery(object):
    
    search_type_produit = TypeProduitType.ListField(action=graphene.String(default_value="search_type_produit"))
    
    search_stock_state = StockStateType.ListField(action=graphene.String(default_value="search_stock_state"))
    
    search_produit = ProduitType.ListField(action=graphene.String(default_value="search_produit"))
    
    search_produit_in_officine = ProduitInOfficineType.ListField(action=graphene.String(default_value="search_produit_in_officine"))
    
    search_assurance = AssuranceType.ListField(action=graphene.String(default_value="search_assurance"))
    
    
    search_produits_avialable_in_officine = graphene.List(ProduitsAvialableInOfficineType, circonscription=graphene.String(), produits=graphene.List(graphene.String, required=True), longitude=graphene.Float(), latitude=graphene.Float())
    def resolve_search_produits_avialable_in_officine(root, info, circonscription, produits,  longitude, latitude,  **kwargs):
        point = Point(longitude, latitude, srid=4326)
        print(point)
        officines = Officine.objects.annotate(distance=Distance('geometry', point)).filter(deleted = False, geometry__distance_lte = (point, 5000), type=TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE))
        produits_in = Produit.objects.filter(deleted = False, id__in=produits)
        liste = []
        for officine in officines:
            pro_offs =  officine.officine_for_produit.filter(produit__id__in = produits_in.values_list('id', flat=True))
            pro_offs = pro_offs.exclude(stock_state__etiquette = StockState.RUPTURE)
            ratio = pro_offs.count()
            if ratio == 0 :
                continue
            
            print(officine)
            pros = [pro.produit.id for pro in pro_offs]
            liste.append({"officine": officine, "produits": pros, "ratio": ratio, "distance": round(officine.distance*100, 2)})
        
        liste_triee = sorted(liste, key=lambda x: (-x['ratio'], x['distance']))
        datas = []
        for elment in liste_triee[:15]:
            officine = elment["officine"]
            multilinestring = {"":""}
            try:
                url = f"https://router.project-osrm.org/route/v1/car/{point.x},{point.y};{officine.lat},{officine.lon}?steps=true&geometries=geojson"
                print(url)
                response = requests.get(url)
                data = response.json()
                if data['code'] == 'Ok':
                    geometry = data['routes'][0]
                    geometry[ "type"] = "Feature"
                    multilinestring = json.dumps(geometry)
            except Exception as e:
                print(f"Error generation routing for {officine.name}", e)

            item = ProduitsAvialableInOfficineType(officine = elment["officine"].id, produits = elment["produits"], ratio = elment["ratio"], distance = elment["distance"], route = json.dumps(multilinestring))
            datas.append(item)
        return datas
    
    
    class ProduitType(DjangoObjectType):
        class Meta:
            model = Produit
            
    class TypeProduitType(DjangoObjectType):
        class Meta:
            model = TypeProduit
        
    search_produits = graphene.List(ProduitType, produits=graphene.List(graphene.String, required=True))
    def resolve_search_produits(root, info, produits,  **kwargs):
        return Produit.objects.filter(id__in=produits)


    
class ProduitAppMutation(object):
    # Dtm
    create_type_produit = TypeProduitType.CreateField()
    update_type_produit = TypeProduitType.UpdateField()

    # Dsm
    create_stock_state = StockStateType.CreateField()
    update_stock_state = StockStateType.UpdateField()
    
    # Dtm
    create_produit = ProduitType.CreateField()
    update_produit = ProduitType.UpdateField()

    # Dsm
    create_produit_in_officine = ProduitInOfficineType.CreateField()
    update_produit_in_officine = ProduitInOfficineType.UpdateField()
    
    # Dtm
    create_assurance = AssuranceType.CreateField()
    update_assurance = AssuranceType.UpdateField()