from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import DateFieldListFilter


@admin.register(SMS)
class SMSAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['number',"message", "utilisateur", "status",  "created_at"]