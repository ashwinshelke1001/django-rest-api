'''
'''
from django.urls import path, include
from django.contrib import admin
from accounts.api.views import  UserDetailAPIView, UserStatusAPIView 

urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view(), name='login'),
    # url(r'^register/$', RegisterAPIView.as_view(), name='register'),
    path('<str:username>/status/', UserStatusAPIView.as_view(), name='status-api'),
]