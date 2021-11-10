from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from account.views import CreateUserView, CheckUserView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/create/', CreateUserView.as_view()),
    path('api/check/', CheckUserView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

]
