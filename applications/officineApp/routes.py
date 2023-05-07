
from .schemas import *
from .serializers import *
import graphene


class OfficineAppQuery(object):
    
    search_type_officine = TypeOfficineType.ListField(action=graphene.String(default_value="search_type_officine"))
    
    search_circonscription = CirconscriptionType.ListField(action=graphene.String(default_value="search_circonscription"))
    
    search_officine = OfficineType.ListField(action=graphene.String(default_value="search_officine"))
    
    search_responsable_officine = ResponsableOfficineType.ListField(action=graphene.String(default_value="search_responsable_officine"))
    
    search_garde = GardeType.ListField(action=graphene.String(default_value="search_garde"))
    
    search_officine_de_garde = OfficineDeGardeType.ListField(action=graphene.String(default_value="search_officine_de_garde"))
    
    

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