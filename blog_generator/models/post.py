from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown

from .post_status import PostStatus
from .author import Author
from .category import Category
from .tag import Tag
# from .comment import Comment


def get_default_post_status():
    """ get a default value for status; create new status if not available """
    return PostStatus.objects.get_or_create(status="draft")[0].id

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True, blank=True)
    image1 = models.ImageField(upload_to='post_images', blank=True)
    image2 = models.ImageField(upload_to='post_images', blank=True)
    image3 = models.ImageField(upload_to='post_images', blank=True)
    image4 = models.ImageField(upload_to='post_images', blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    comments = models.ManyToManyField('Comment', blank=True, related_name='comments')
    slug = models.SlugField(max_length=100, unique=True)
    status = models.ForeignKey(PostStatus, on_delete=models.CASCADE, default=get_default_post_status)
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    flagged = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
    
    def get_author(self):
        return self.author
    
    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
    
    def get_date(self):
        return self.date
    
    def get_last_updated_date(self):
        return self.last_updated_date
    
    def get_image1(self):
        return self.image1
    
    def get_image2(self):
        return self.image2
    
    def get_image3(self):
        return self.image3
    
    def get_image4(self):
        return self.image4
    
    def get_slug(self):
        return self.slug
    
    def get_status(self):
        return self.status
    
    def get_featured(self):
        return self.featured
    
    def get_views(self):
        return self.views
    
    def get_likes(self):
        return self.likes
    
    def get_shares(self):
        return self.shares
    
    # def get_comments(self):
    #     return Comment.objects.filter(post=self)