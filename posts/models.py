from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from markdown import markdown

def get_default_author_status():
    """ get a default value for status; create new status if not available """
    return AuthorStatus.objects.get_or_create(status="active")[0].id

def get_default_commenter_status():
    """ get a default value for status; create new status if not available """
    return CommenterStatus.objects.get_or_create(status="active")[0].id

def get_default_category_status():
    """ get a default value for status; create new status if not available """
    return CategoryStatus.objects.get_or_create(status="active")[0].id

def get_default_tag_status():
    """ get a default value for status; create new status if not available """
    return TagStatus.objects.get_or_create(status="active")[0].id

def get_default_comment_status():
    """ get a default value for status; create new status if not available """
    return CommentStatus.objects.get_or_create(status="draft")[0].id

def get_default_post_status():
    """ get a default value for status; create new status if not available """
    return PostStatus.objects.get_or_create(status="draft")[0].id

def get_default_flag_category():
    """ get a default value; create new status if not available """
    return FlagCategory.objects.get_or_create(type="spam")[0].id


class AuthorStatus(models.Model):
    # Sets the status of Authors
    # Options include "active", "inactive", "banned"
    status=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.status}"

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
    


class CommenterStatus(models.Model):
    # Sets the status of Commenters
    # Options include "active", "inactive", "banned"
    status=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.status}"

class Commenter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    status = models.ForeignKey(CommenterStatus, on_delete=models.CASCADE, default=get_default_commenter_status)
    
    def __str__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.first_name
    
    def get_email(self):
        return self.email
    


class CategoryStatus(models.Model):
    # Sets the status of Categories
    # Options include "active", "inactive"
    status=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.status}"

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

class TagStatus(models.Model):
    # Sets the status of Tags
    # Options include "active", "inactive"
    status=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.status}"
    
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
    
class PostStatus(models.Model):
    # Sets the status of Posts
    # Options include "published", "unpublished", "draft", "removed", "awaiting approval"
    status=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.status}"

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
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.ForeignKey(PostStatus, on_delete=models.CASCADE, default=get_default_post_status)
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    flagged = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
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
    
    def get_comments(self):
        return Comment.objects.filter(post=self)

class CommentStatus(models.Model):
    # Sets the status of Comments
    # Options include "draft", "published", "removed", "duplicate"
    status=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.status}"

class Comment(models.Model):
    commenter = models.ForeignKey(Commenter, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.ForeignKey(CommentStatus, on_delete=models.CASCADE, default=get_default_comment_status)
    likes = models.IntegerField(default=0)
    flagged = models.BooleanField(default=False)
    
    def __str__(self):
        return self.comment
    
    def get_commenter(self):
        return self.commenter
    
    def get_comment(self):
        return self.comment
    
    def get_date(self):
        return self.date
    
    def get_post(self):
        return self.post
    
    def get_status(self):
        return self.status
    
    def get_likes(self):
        return self.likes
    
class FlagCategory(models.Model):
    # The different types of flags available
    # Options include "spam", "offensive", "incorrect information", "out of date"
    type=models.CharField(max_length=10, unique=True)
    severity=models.IntegerField(default=3)

    def __str__(self):
        return f"{self.type}"

class Flag(models.Model):
    # Set on a comment or post to draw admin's attention to it
    type=models.ForeignKey(FlagCategory, default=get_default_flag_category, on_delete=models.CASCADE)
    notes=models.TextField(blank=True)
    reporter=models.ForeignKey(Commenter, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} on {self.post or self.comment}"