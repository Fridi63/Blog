from rest_framework import serializers
from account.models import User, Profile, Subscriber


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields=["about_me"]


class UserMeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
