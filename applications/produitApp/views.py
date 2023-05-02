from django.shortcuts import render
from annoying.decorators import render_to
from produitApp.models import *

# Create your views here.




@render_to('produitApp/medicaments.html')
def medicaments(request):
    if request.method == "GET":
        medicaments = Produit.objects.filter(deleted = False)
        types = TypeProduit.objects.filter(deleted = False)
        ctx = {
            "medicaments" : medicaments,
            "types": types
        }
        return ctx



@render_to('produitApp/medicaments_officine.html')
def medicaments_officine(request, officine):
    if request.method == "GET":
        officine = Officine.objects.filter(id = officine)
        prodoffs = officine.officine_for_produit.filter(produit__deleted = False)
        types = TypeProduit.objects.filter(deleted = False)
        stocks = StockState.objects.filter(deleted = False)
        ctx = {
            "prodoffs" : prodoffs,
            "types": types,
            "stocks": stocks,
        }
        return ctx