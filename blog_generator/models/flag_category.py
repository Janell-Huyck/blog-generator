from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown
    
class FlagCategory(models.Model):
    # The different types of flags available
    # Options include "spam", "offensive", "incorrect information", "out of date"
    type=models.CharField(max_length=10, unique=True)
    severity=models.IntegerField(default=3)

    def __str__(self):
        return f"{self.type}"
