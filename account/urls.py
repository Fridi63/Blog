from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import CreateUserView, UserMeView


urlpatterns = [

    path('create/', CreateUserView.as_view()),
    path('check/', UserMeView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]
