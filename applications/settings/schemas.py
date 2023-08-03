import graphene
from UserApp.routes import UserAppQuery, UserAppMutation
from officineApp.routes import OfficineAppQuery, OfficineAppMutation
from produitApp.routes import ProduitAppQuery, ProduitAppMutation
from demandeApp.routes import DemandeAppQuery, DemandeAppMutation
from graphene_django_extras import all_directives

class RootQuery(
    UserAppQuery,
    OfficineAppQuery,
    ProduitAppQuery,
    DemandeAppQuery,
    graphene.ObjectType):
    pass


class RootMutations(
    UserAppMutation,
    OfficineAppMutation,
    ProduitAppMutation,
    DemandeAppMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutations,  directives=all_directives)
