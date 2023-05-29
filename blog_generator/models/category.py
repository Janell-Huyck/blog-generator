from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown

from .category_status import CategoryStatus


def get_default_category_status():
    """ get a default value for status; create new status if not available """
    return CategoryStatus.objects.get_or_create(status="active")[0].id


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500, blank=True )
    status = models.ForeignKey(CategoryStatus, default=get_default_category_status, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description