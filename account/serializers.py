from rest_framework import serializers
from account.models import User, Profile, Subscriber
from post.models import Like, Comment, Category, Post


class ProfileSerializer(serializers.Serializer):


    class Meta:
        model = Profile
        fields=["about_me"]


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


class UserCreateSerialiser(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ["username", "password", "email"]
