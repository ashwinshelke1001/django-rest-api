from rest_framework import generics, permissions, pagination
# from rest_framework import APIView
from django.contrib.auth import  get_user_model
from .serializer import UserRegisterSerializer 
from accounts.api.user.serializer import  UserDetailSerializer
from status.api.serializers import StatusInlineUserSerializer
from status.models import Status

User = get_user_model()

class UserStatusAPIView(generics.ListAPIView):
    """
    """
    serializer_class = StatusInlineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is not None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)


class UserDetailAPIView(generics.RetrieveAPIView):
    """
    """
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

class RegisterAPIView(generics.CreateAPIView):
    """
    """
    queryset = User.objects.all()
    serializers_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]    

    def get_serializer_context(self, *args, **kwargs):
        """
        """
        return {"request": self.request}
