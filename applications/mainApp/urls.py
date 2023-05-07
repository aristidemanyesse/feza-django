
from django.shortcuts import redirect
from django.urls import path

from . import views, ajax

app_name = "mainApp"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('main/dashboard', views.dashboard, name="dashboard"),
    path('auth/login/', views.connexion, name="login"),
    path('auth/locked', views.locked, name="locked"),
    path('auth/logout/', views.deconnexion, name="logout"),
   
    
    path('auth/ajax/connexion/', ajax.connexion),
    path('auth/ajax/first_user/', ajax.first_user),
    path('auth/ajax/unlocked/', ajax.unlocked),
    path('auth/ajax/forgetpassword/', ajax.forgetpassword),
    path('auth/ajax/reset/', ajax.reset),
]