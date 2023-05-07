import graphene
from UserApp.routes import UserAppQuery, UserAppMutation
from officineApp.routes import OfficineAppQuery, OfficineAppMutation
from produitApp.routes import ProduitAppQuery, ProduitAppMutation
from graphene_django_extras import all_directives

class RootQuery(
    UserAppQuery,
    OfficineAppQuery,
    ProduitAppQuery,
    graphene.ObjectType):
    pass


class RootMutations(
    UserAppMutation,
    OfficineAppMutation,
    ProduitAppMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutations,  directives=all_directives)
