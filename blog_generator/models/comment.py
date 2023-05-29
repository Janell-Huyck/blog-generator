from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown

from .comment_status import CommentStatus
from .commenter import Commenter
from .post import Post

def get_default_comment_status():
    """ get a default value for status; create new status if not available """
    return CommentStatus.objects.get_or_create(status="draft")[0].id



class Comment(models.Model):
    commenter = models.ForeignKey(Commenter, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.ForeignKey(CommentStatus, on_delete=models.CASCADE, default=get_default_comment_status)
    likes = models.IntegerField(default=0)
    flagged = models.BooleanField(default=False)
    
    def __str__(self):
        return self.comment_text
    
    def get_commenter(self):
        return self.commenter
    
    def get_date(self):
        return self.date
    
    def get_post(self):
        return self.post
    
    def get_status(self):
        return self.status
    
    def get_likes(self):
        return self.likes