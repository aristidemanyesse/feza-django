from django.contrib import admin

# Register your models here.
from .models import*
from django.contrib.admin import DateFieldListFilter
# Register your models here.

@admin.register(TypeProduit)
class TypeProduitAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['name', "etiquette"]


@admin.register(StockState)
class StockStateAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['name', "etiquette"]


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    date_hierarchy = 'created_at'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = [ 'name', "type", "codebarre", 'only_ordonnance']
    list_editable = ["type", "codebarre", 'only_ordonnance']



@admin.register(ProduitInOfficine)
class ProduitInOfficineAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    date_hierarchy = 'created_at'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["id", 'produit', "officine"]

