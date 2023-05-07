
from .schemas import *
from .serializers import *
import graphene


class ProduitAppQuery(object):
    
    search_type_produit = TypeProduitType.ListField(action=graphene.String(default_value="search_type_produit"))
    
    search_stock_state = StockStateType.ListField(action=graphene.String(default_value="search_stock_state"))
    
    search_produit = ProduitType.ListField(action=graphene.String(default_value="search_produit"))
    
    search_produit_in_officine = ProduitInOfficineType.ListField(action=graphene.String(default_value="search_produit_in_officine"))
    
    search_assurance = AssuranceType.ListField(action=graphene.String(default_value="search_assurance"))
    
    

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
