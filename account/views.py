from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import UserCreateSerialiser
from .models import User
from blog.tasks import send_email
from rest_framework import status


class UserMeView(APIView):

    permissions_classes = (IsAuthenticated,)

    def get(self, request, pk):

        user = User.objects.get(pk=pk)
        serializer = UserCreateSerialiser(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CreateUserView(APIView):

    def post(self, request):
        serializer = UserCreateSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)
        username, password, email = serializer.data.values()

        u = User(username=username, password=password, email=email)
        u.set_password(password)
        u.save()

        send_email.delay("Registration", "You have successfully registered", 'jeyoo578@gmail.com', ['email'])
        return Response(status=status.HTTP_201_CREATED, data={"message":"Thank you for registering. Please verify your email before continuing"})
