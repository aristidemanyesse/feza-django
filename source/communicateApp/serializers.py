
from .models import *
from rest_framework.serializers import ModelSerializer


class SMSSerializer(ModelSerializer):
    class Meta:
        model = SMS
        fields = '__all__'
