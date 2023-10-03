from django.forms import ModelForm
from .models import *

# Create the form class.
class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"
        
        
# Create the form class.
class ProduitInOfficineForm(ModelForm):
    class Meta:
        model = ProduitInOfficine
        fields = "__all__"
        
        
# Create the form class.
class AssuranceForm(ModelForm):
    class Meta:
        model = Assurance
        fields = "__all__"