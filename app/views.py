from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import App

from .serializers import AppSerializer, UserSerializer


class AppViewSet(viewsets.ModelViewSet):

    queryset = App.objects.all()
    serializer_class = AppSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

