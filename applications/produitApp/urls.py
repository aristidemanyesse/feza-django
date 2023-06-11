
from django.shortcuts import redirect
from django.urls import path

from . import views, ajax

app_name = "produitApp"
urlpatterns = [
    path('medicaments/', views.medicaments, name="medicaments"),
    path('medicaments_officine/<uuid:id>/', views.medicaments_officine, name="medicaments_officine"),
    
    path('ajax/disponible/', ajax.disponible, name="disponible"),
    path('ajax/indisponible/', ajax.indisponible, name="indisponible"),
    path('ajax/get/', ajax.get, name="get"),

    # path('fixtures/test/', views.features_test, name="features_test"),
    # path('fixtures/<int:year>/<int:month>/<int:day>/', views.fixtures, name="fixtures"),
    # path('match/<uuid:id>/', views.match, name="match"),
]