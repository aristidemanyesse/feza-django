from annoying.decorators import render_to
from produitApp.models import *
from django.shortcuts import redirect, get_object_or_404


# Create your views here.




@render_to('produitApp/medicaments.html')
def medicaments(request):
    if request.method == "GET":
        produits = Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT)).order_by("name")
        ctx = {
            "produits" : produits,
            "types": TypeProduit.objects.all()
        }
        return ctx



@render_to('produitApp/medicaments_officine.html')
def medicaments_officine(request, id):
    if request.method == "GET":
        officine = get_object_or_404(Officine, pk=id)
        prodoffs = officine.officine_for_produit.filter(produit__deleted = False).order_by("produit__name")
        produits = Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT)).exclude(id__in = prodoffs.values_list('produit', flat = True)).order_by("name")
        ctx = {
            "prodoffs" : prodoffs,
            "produits": produits,
           
        }
        return ctx

