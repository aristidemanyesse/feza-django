from django.shortcuts import render
from annoying.decorators import render_to
from officineApp.models import *

# Create your views here.




@render_to('officineApp/liste.html')
def liste(request):
    if request.method == "GET":
        officines = Officine.objects.filter(deleted = False)
        ctx = {
            "officines" : officines
        }
        return ctx

        

@render_to('officineApp/map.html')
def map(request):
    if request.method == "GET":
        circonscriptions = Circonscription.objects.filter(deleted = False)
        ctx = {
            "circonscriptions" : circonscriptions
        }
        return ctx
        

@render_to('officineApp/officine.html')
def officine(request, id):
    if request.method == "GET":
        officine = Officine.objects.get(id = id, deleted = False)
        ctx = {
            "officine" : officine
        }
        return ctx

        

@render_to('officineApp/responsables.html')
def responsables(request):
    if request.method == "GET":
        medicaments = Officine.objects.filter()
        ctx = {
            "medicaments" : medicaments
        }
        return ctx