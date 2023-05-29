from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown

from .commenter_status import CommenterStatus

def get_default_commenter_status():
    """ get a default value for status; create new status if not available """
    return CommenterStatus.objects.get_or_create(status="active")[0].id



class Commenter(models.Model):
    full_name=models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    status = models.ForeignKey(CommenterStatus, on_delete=models.CASCADE, default=get_default_commenter_status)
    
    def __str__(self):
        return self.full_name

    def get_email(self):
        return self.email
    