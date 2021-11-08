from django.urls import path

from .views import UpdateModelListAPIView, UpdateModelDetailAPIView
urlpatterns = [
    # path('', UpdateModelListAPIView.as_view()), # api/updates/ - List/Create
    path('<int:id>/', UpdateModelDetailAPIView.as_view()),
]