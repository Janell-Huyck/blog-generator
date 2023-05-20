from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.utils.text import slugify
# from django.utils.html import mark_safe
# from django.utils.safestring import SafeString
# from django.utils.safestring import mark_safe
# from markdown import markdown

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.CharField(max_length=5000)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    slug = models.SlugField(max_length=100)
    status = models.CharField(max_length=10)

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
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(upload_to='post_images')
    image2 = models.ImageField(upload_to='post_images')
    image3 = models.ImageField(upload_to='post_images')
    image4 = models.ImageField(upload_to='post_images')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=100)
    status = models.CharField(max_length=10)
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    
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

class Commenter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
class Comment(models.Model):
    commenter = models.ForeignKey(Commenter, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    likes = models.IntegerField(default=0)
    
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
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    

# stopping at 33:47 on video, moving over to Hackerrank for interview prep for a bit


