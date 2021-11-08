from django.urls import path, include
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token # accounts app
from .views import  RegisterAPIView

urlpatterns = [
	path('register/', RegisterAPIView.as_view(), name='register'),
]
