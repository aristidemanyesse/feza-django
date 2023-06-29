from django.contrib.gis import admin

# Register your models here.
from .models import*
from django.contrib.admin import DateFieldListFilter
# Register your models here.


admin.site.register(ResponsableOfficine)
class ResponsableOfficineAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    date_hierarchy = 'created_at'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['fullname', "officine", "contact"]

@admin.register(TypeOfficine)
class TypeOfficineAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['name', "etiquette"]


@admin.register(Circonscription)
class CirconscriptionAdmin(admin.GISModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['name']


@admin.register(Officine)
class OfficineAdmin(admin.GISModelAdmin):
    empty_value_display = '-'
    date_hierarchy = 'created_at'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['name', "type", "circonscription", 'localisation']



@admin.register(ResponsableOfficine)
class ResponsableOfficineAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    date_hierarchy = 'created_at'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['fullname', "officine", "contact"]




@admin.register(Garde)
class GardeAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    date_hierarchy = 'created_at'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['__str__', 'debut', "fin", "created_at"]


@admin.register(OfficineDeGarde)
class OfficineDeGardeAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    date_hierarchy = 'created_at'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['id', 'garde', "officine", "created_at"]
