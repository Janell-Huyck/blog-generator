from django.contrib import admin

from posts.models import Author, AuthorStatus, Post, PostStatus, Commenter, CommenterStatus, Comment, CommentStatus, Category, CategoryStatus, Tag, TagStatus, Flag, FlagCategory

# Register your models here.
admin.site.register(Author)
admin.site.register(AuthorStatus)
admin.site.register(Post)
admin.site.register(PostStatus)
admin.site.register(Commenter)
admin.site.register(CommenterStatus)
admin.site.register(Comment)
admin.site.register(CommentStatus)
admin.site.register(Category)
admin.site.register(CategoryStatus)
admin.site.register(Tag)
admin.site.register(TagStatus)
admin.site.register(Flag)
admin.site.register(FlagCategory)



