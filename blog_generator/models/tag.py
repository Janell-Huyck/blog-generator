from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown

from .tag_status import TagStatus


def get_default_tag_status():
    """ get a default value for status; create new status if not available """
    return TagStatus.objects.get_or_create(status="active")[0].id

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500, blank=True)
    status = models.ForeignKey(TagStatus, default=get_default_tag_status, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    