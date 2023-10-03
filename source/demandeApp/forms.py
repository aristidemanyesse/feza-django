from django.forms import ModelForm
from .models import *

        
# Create the form class.
class DemandeForm(ModelForm):
    class Meta:
        model = Demande
        fields = "__all__"
        
        
# Create the form class.
class OfficineDemandeForm(ModelForm):
    class Meta:
        model = OfficineDemande
        fields = "__all__"
        
# Create the form class.
class ReponseForm(ModelForm):
    class Meta:
        model = Reponse
        fields = "__all__"
        