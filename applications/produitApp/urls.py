
from django.shortcuts import redirect
from django.urls import path

from . import views

app_name = "produitApp"
urlpatterns = [
    path('medicaments/', views.medicaments, name="medicaments"),
    path('medicaments_officine/<uuid:id>/', views.medicaments_officine, name="medicaments_officine"),
    # path('fixtures/test/', views.features_test, name="features_test"),
    # path('fixtures/<int:year>/<int:month>/<int:day>/', views.fixtures, name="fixtures"),
    # path('match/<uuid:id>/', views.match, name="match"),
]