from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import PostSerializer, CommentSerializers, LikeSerializers
from .models import Post


class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, post_pk):
        try:
            post = Post.objects.get(pk=post_pk, user=request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializers = PostSerializer(post)
        return Response(serializers.data)

    def post(self, request):
        print(request.auth)
        print(request.user)
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(user=request.user)
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiListView(APIView):

    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status.HTTP_404_NOT_FOUND)
        comments = post.comments.filter(is_approved=True)
        serializers = CommentSerializers(comments, many=True)
        return Response(serializers.data)

    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializers(date=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LikeView(APIView):
    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status.HTTP_404_NOT_FOUND)
        likes = post.likes.filter(is_liked=True).count()
        return Response({'likes': likes})

    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LikeSerializers(date=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
