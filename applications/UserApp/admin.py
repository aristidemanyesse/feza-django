from django.contrib import admin

# Register your models here.
from .models import*
from django.contrib.admin import DateFieldListFilter
# Register your models here.

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['__str__', "circonscription", "contact", "imei", "otp", "is_valide"]

@admin.register(Demande)
class DemandeAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['__str__',"status", "ordonnance", "commentaire", "created_at"]


@admin.register(OfficineDemande)
class OfficineDemandeAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["officine", "demande", "status",  "created_at"]


@admin.register(LigneDemande)
class LigneDemandeAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['demande', "produit", "status", "created_at"]


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
    list_display = ['reponse', "produit", "status", "created_at"]
