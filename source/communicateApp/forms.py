from django.forms import ModelForm
from .models import *

        
# Create the form class.
class SMSForm(ModelForm):
    class Meta:
        model = SMS
        fields = "__all__"
        