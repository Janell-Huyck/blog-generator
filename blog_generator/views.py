from rest_framework import viewsets
from .models.post import Post
from .models.author import Author
from .models.comment import Comment
from .serializers import PostSerializer, AuthorSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned comments to a given post,
        by filtering against a `post_id` query parameter in the URL.
        """
        queryset = Comment.objects.all()
        post_id = self.request.query_params.get('post_id', None)
        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)
        return queryset


from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')
