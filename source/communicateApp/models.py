from django.db import models
import requests, json
from UserApp.models import Utilisateur
from coreApp.models import BaseModel
from annoying.decorators import signals
from settings.settings import SEND_MESSAGE_URL, TOKEN_URL
# Create your models here.

class SMS(BaseModel):
    token         = models.TextField(default="", null=True, blank=True)
    number        = models.TextField(default = "", null=True, blank=True)
    message       = models.TextField(default = "", null=True, blank=True)
    status        = models.BooleanField(default= False)
    utilisateur   = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, null=True, blank=True, related_name="utilisateur_sms")
    
    def __str__(self):
        return "SMS envoyé à " + str(self.utilisateur)
    
    
    def get_SMS_token(self):
        try :
            headers = {
                'Authorization': 'Basic VURwNEFVTkFYVURLcDU3ampjOGM0aEhtMTk5R1VGUTQ6WWtORzhNeGQ0QXRoQVJYbQ==',
                'Content-Type': 'application/x-www-form-urlencoded',  # You can specify the content type if needed
                'Accept': 'application/json',  # You can specify the content type if needed
            }
            data = {'grant_type': 'client_credentials'}
            response = requests.post(TOKEN_URL, data=data, headers=headers)
            if response.status_code == 200:
                return response.json()['access_token']
            raise Exception(response.text)
        except Exception as e:
            print("Error creating token SMS", e, )
    
    
    def send_SMS(self):
        try:
            token = self.get_SMS_token()
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            data = {
                    "outboundSMSMessageRequest": {
                        "address": f"tel:+225{self.number}",
                        "senderAddress":"tel:+2250000",
                        "outboundSMSTextMessage":{
                            "message": f"{self.message}"
                        }
                    }
                }
            response = requests.post(SEND_MESSAGE_URL, data=json.dumps(data), headers=headers)
            if response.status_code == 201:
                self.status, self.token = response.status_code == 201, token
                self.save()
                return response.status_code == 201, token
            raise Exception(response.text)

        except Exception as e:
            print('POST request failed with status code:', e)
        
    



@signals.post_save(sender=SMS)
def sighandler(instance, created, **kwargs):
    if created:
        instance.number = instance.utilisateur.contact if instance.utilisateur is not None else instance.number
        instance.number = instance.number.replace(" ", "")
        if len(instance.number) != 10:
            raise Exception("Numero de téléphone est incorrect !!")
        instance.send_SMS()
        