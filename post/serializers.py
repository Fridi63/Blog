from rest_framework import serializers
from post.models import Category, Post, Comment


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields=["name"]


class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ["author", "title", "content", "categories"]


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = ["user", "content"]
