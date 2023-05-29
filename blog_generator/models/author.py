from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown

from .author_status import AuthorStatus

def get_default_author_status():
    """ get a default value for status; create new status if not available """
    return AuthorStatus.objects.get_or_create(status="active")[0].id


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True)
    bio = models.CharField(max_length=5000, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    status = models.ForeignKey(AuthorStatus, on_delete=models.CASCADE, default=get_default_author_status)
    home_page = models.URLField(blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'slug': self.slug})
    
    def get_posts(self):
        return Post.objects.filter(author=self)
    
    def get_posts_count(self):
        return Post.objects.filter(author=self).count()
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.first_name
    
    def get_bio_as_markdown(self):
        return mark_safe(markdown(self.bio, safe_mode='escape'))
    
    def get_status(self):
        return self.status
    
    def get_profile_picture(self):
        return self.profile_picture
    
    def get_email(self):
        return self.email
    
    def get_slug(self):
        return self.slug
    