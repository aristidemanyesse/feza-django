
from .schemas import *
import graphene


class UserAppQuery(object):
    search_utilisateur = UtilisateurType.ListField(action=graphene.String(default_value="search_utilisateur"))
    
    
class UserAppMutation(object):
    # Utilisateur
    create_utilisateur = UtilisateurType.CreateField()
    update_utilisateur = UtilisateurType.UpdateField()
