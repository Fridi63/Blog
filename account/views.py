from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import UserCreateSerialiser
from .models import User
from blog.tasks import send_email


class CheckUserView(APIView):

    permissions_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            "user": str(request.user)
        }
        return Response(content)


class CreateUserView(APIView):

    def post(self, request):
        serializer = UserCreateSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)
        username, password, email = serializer.data.values()

        u = User(username=username, password=password, email=email)
        u.set_password(password)
        u.save()

        send_email("Registration", "You have successfully registered", 'jeyoo578@gmail.com', email)
        return Response(data="User registered")
