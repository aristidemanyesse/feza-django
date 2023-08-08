from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import DateFieldListFilter


@admin.register(Demande)
class DemandeAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['__str__',"propagating", "is_finished", "ordonnance", "commentaire", "created_at"]


@admin.register(OfficineDemande)
class OfficineDemandeAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["officine", "demande", "is_valided",  "created_at"]


@admin.register(LigneDemande)
class LigneDemandeAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['demande', "produit", "quantite", "status", "created_at"]


@admin.register(Reponse)
class ReponseAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["demande", "read", "commentaire", "created_at"]


@admin.register(LigneReponse)
class LigneReponseAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['reponse', "produit", "price", "quantite", "status", "created_at"]


@admin.register(SubsLigneReponse)
class SubsLigneReponseAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['ligne', "produit", "quantite", "price", "created_at"]


@admin.register(RdvLigneReponse)
class SubsLigneReponseAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['ligne', "days", "valide", "created_at"]
