from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from annoying.decorators import render_to
from UserApp.models import *

# Create your views here.




@render_to('UserApp/liste.html')
def liste(request):
    if request.method == "GET":
        utilisateurs = Utilisateur.objects.filter()
        ctx = {
            "utilisateurs" : utilisateurs
        }
        return ctx

        

@render_to('UserApp/map.html')
def utilisateur(request):
    if request.method == "GET":
        medicaments = Utilisateur.objects.filter()
        ctx = {
            "medicaments" : medicaments
        }
        return ctx
        

@render_to('UserApp/map.html')
def map(request):
    if request.method == "GET":
        medicaments = Utilisateur.objects.filter()
        ctx = {
            "medicaments" : medicaments
        }
        return ctx