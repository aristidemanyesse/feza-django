
from django.shortcuts import redirect
from django.urls import path

from . import views

app_name = "UserApp"
urlpatterns = [
    path('liste/', views.liste, name="liste"),
    path('map/', views.map, name="map"),
    # path('fixtures/test/', views.features_test, name="features_test"),
    # path('fixtures/<int:year>/<int:month>/<int:day>/', views.fixtures, name="fixtures"),
    path('utilisateur/<uuid:id>/', views.utilisateur, name="utilisateur"),
]