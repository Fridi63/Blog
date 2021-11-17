from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from account.views import CreateUserView, UserMeView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Blog Swagger')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('', schema_view)

]
