from annoying.decorators import render_to
from produitApp.models import *
from django.shortcuts import redirect, get_object_or_404


# Create your views here.




@render_to('produitApp/medicaments.html')
def medicaments(request):
    if request.method == "GET":
        medicaments = Produit.objects.filter(deleted = False).order_by("name")
        types = TypeProduit.objects.filter(deleted = False)
        ctx = {
            "medicaments" : medicaments,
            "types": types
        }
        return ctx



@render_to('produitApp/medicaments_officine.html')
def medicaments_officine(request, id):
    if request.method == "GET":
        officine = get_object_or_404(Officine, pk=id)
        prodoffs = officine.officine_for_produit.filter(produit__deleted = False).order_by("produit__name")
        types = TypeProduit.objects.filter(deleted = False)
        stocks = StockState.objects.filter(deleted = False)
        produits = Produit.objects.filter(deleted = False)
        ctx = {
            "prodoffs" : prodoffs,
            "types": types,
            "stocks": stocks,
            "produits": produits,
        }
        return ctx