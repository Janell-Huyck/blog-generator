from rest_framework import serializers
from .models.post import Post
from .models.author import Author
from .models.comment import Comment
from .models.tag import Tag



class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = fields = ['first_name', 'last_name', 'email', 'bio', 'profile_picture', 'slug', 'status', 'home_page', 'name']  # Include 'name' in the fields

    def get_name(self, obj):
        return obj.get_full_name()
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
    
class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields = '__all__'