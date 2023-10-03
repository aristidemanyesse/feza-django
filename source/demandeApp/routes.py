
from .schemas import *
import graphene


class DemandeAppQuery(object):
    search_demande            = DemandeType.ListField(action=graphene.String(default_value="search_demande"))
    search_officine_demande   = OfficineDemandeType.ListField(action=graphene.String(default_value="search_officine_demande"))
    search_ligne_demande      = LigneDemandeType.ListField(action=graphene.String(default_value="search_ligne_demande"))
    search_reponse            = ReponseType.ListField(action=graphene.String(default_value="search_reponse"))
    search_ligne_reponse      = LigneReponseType.ListField(action=graphene.String(default_value="search_ligne_reponse"))
    search_subs_ligne_reponse = SubsLigneReponseType.ListField(action=graphene.String(default_value="search_subs_ligne_reponse"))
    search_rdv_ligne_reponse  = RdvLigneReponseType.ListField(action=graphene.String(default_value="search_rdv_ligne_reponse"))
    
    
class DemandeAppMutation(object):
    # DemandeType
    create_demande            = DemandeType.CreateField()
    update_demande            = DemandeType.UpdateField()
    
    # DemandeType
    create_officine_demande   = OfficineDemandeType.CreateField()
    update_officine_demande   = OfficineDemandeType.UpdateField()
    
    # LigneDemandeType
    create_ligne_demande      = LigneDemandeType.CreateField()
    update_ligne_demande      = LigneDemandeType.UpdateField()
    
    
    # ReponseType
    create_reponse        = ReponseType.CreateField()
    update_reponse        = ReponseType.UpdateField()
    
    # LigneReponseType
    create_ligne_reponse  = LigneReponseType.CreateField()
    update_ligne_reponse  = LigneReponseType.UpdateField()
    
    # LigneReponseType
    create_subs_ligne_reponse  = SubsLigneReponseType.CreateField()
    update_subs_ligne_reponse  = SubsLigneReponseType.UpdateField()