
from django.shortcuts import redirect
from django.urls import path

from . import views

app_name = "officineApp"
urlpatterns = [
    path('', views.liste, name="liste"),
    path('map/', views.map, name="map"),
    path('responsables/', views.responsables, name="responsables"),
    # path('fixtures/test/', views.features_test, name="features_test"),
    # path('fixtures/<int:year>/<int:month>/<int:day>/', views.fixtures, name="fixtures"),
    path('officine/<uuid:id>/', views.officine, name="officine"),
    path('demandes/<uuid:id>/', views.demandes, name="demandes"),

]