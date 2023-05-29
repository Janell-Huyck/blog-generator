from django.contrib import admin

from .models.author import Author
from .models.author_status import AuthorStatus
from .models.post import Post
from .models.post_status import PostStatus
from .models.commenter import Commenter
from .models.commenter_status import CommenterStatus
from .models.comment import Comment
from .models.comment_status import CommentStatus
from .models.category import Category
from .models.category_status import CategoryStatus
from .models.tag import Tag
from .models.tag_status import TagStatus
from .models.flag import Flag
from .models.flag_category import FlagCategory


class PostAdmin(admin.ModelAdmin):
    exclude = ['slug']

class AuthorAdmin(admin.ModelAdmin):
    exclude = ['slug']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(AuthorStatus)
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



