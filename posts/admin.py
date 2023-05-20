from django.contrib import admin

from posts.models import Author, Post, Commenter, Comment, Category, Tag

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Commenter)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)


