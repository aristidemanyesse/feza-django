
from .schemas import *
import graphene


class CommunicateAppQuery(object):
    search_SMS            = SMSType.ListField(action=graphene.String(default_value="search_SMS"))
    
    
class CommunicateAppMutation(object):
    # SMSType
    create_SMS            = SMSType.CreateField()
    update_SMS            = SMSType.UpdateField()