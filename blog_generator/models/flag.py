from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown

from .flag_category import FlagCategory
from .commenter import Commenter
from .post import Post
from .comment import Comment

def get_default_flag_category():
    """ get a default value; create new status if not available """
    return FlagCategory.objects.get_or_create(type="spam")[0].id

class Flag(models.Model):
    # Set on a comment or post to draw admin's attention to it
    type=models.ForeignKey(FlagCategory, default=get_default_flag_category, on_delete=models.CASCADE)
    notes=models.TextField(blank=True)
    reporter=models.ForeignKey(Commenter, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} on {self.post or self.comment}"