from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth.models import AnonymousUser 
from django.db import models
import uuid,inspect,  os
from django.db.models.signals import pre_save, post_save
from django.dispatch.dispatcher import receiver
from django.contrib.contenttypes.models import ContentType
import django.db.models.options as options

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('auto_populate', "number_elements_to_populate")

# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    protected = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        auto_populate = True
        ordering = ['-created_at']
        abstract = True
        number_elements_to_populate = 852


class Etat(models.Model):
    EN_COURS = 1
    TERMINE = 2
    ANNULE = 3

    name = models.CharField(max_length=255)
    etiquette = models.CharField(max_length=255)
    classe = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class History(LogEntry, models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class MyCodeException:
    ERROR = 401
    ERROR_MIDDLEWARE = 402
    USER_NOT_CONNECTED = 403
    PAGE_NOT_FOUND = 404
    SAME_PASSWORDS = 405
    BAD_PASSWORD = 406
    USERNAME_ALREADY_EXISTS = 407

    ACCESS_DENIED = 500
    BAD_CREDENTIALS = 501
    USER_PASSWORD_NOT_CHANGED = 502
    NOT_OR_BAD_TOKEN = 503
    CHANGING_PASSWORD_EXPIRED = 504

    SENDING_ERROR_MAIL = 600

    LOW_AVAILABLE_VOLUME = 800
    SCISSION_WITH_NULL_VOLUME = 801
    SAME_VOLUME = 802
    OPERATION_VOLUME_SIZE_NULL = 803

    class Meta:
        abstract = True


################################################################################################
