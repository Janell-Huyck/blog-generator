from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown



class PostStatus(models.Model):
    # Sets the status of Posts
    # Options include "published", "unpublished", "draft", "removed", "awaiting approval"
    status=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.status}"

