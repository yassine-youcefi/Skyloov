from django.urls import path
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views
from .views import SignUp


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('signup/', SignUp.as_view(), name='signup'),

]
