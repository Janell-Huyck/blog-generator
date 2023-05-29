
import requests
import os
import openai
from rest_framework import viewsets
from .models.post import Post
from .models.author import Author
from .models.comment import Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
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


@api_view(['POST'])
def generate_post(request):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.8,
        max_tokens = 500,
        messages = [
            {"role": "system", "content": "You are a blog writer that writes whimsical and snarky blog posts about technical topics."},
            {"role": "user", "content": f"Write a blog post about {request.data['topic']}.  Use no more than 500 words."}
            ]
        )

    print(completion.choices[0].message.content)
    response_content = completion.choices[0].message.content.strip()
    new_post = Post(title=request.data['topic'], content=response_content, author=Author.objects.get(id=1))
    new_post.save()
    serializer = PostSerializer(new_post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

