from django.urls import path
from .views import  StatusAPIView, StatusAPIDetailView 

urlpatterns = [
    path('',StatusAPIView.as_view()),
    path('<int:id>/',StatusAPIDetailView.as_view()), 
]

