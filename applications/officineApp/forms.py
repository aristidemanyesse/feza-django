from django.forms import ModelForm
from .models import *

# Create the form class.
class OfficineForm(ModelForm):
    class Meta:
        model = Officine
        fields = "__all__"
        
        
# Create the form class.
class ResponsableOfficineForm(ModelForm):
    class Meta:
        model = ResponsableOfficine
        fields = "__all__"