from rest_framework import serializers
from .models import App
from django.contrib.auth import get_user_model


class AppSerializer(serializers.ModelSerializer):

        class Meta:
            fields = ('id', 'user', 'text', 'created_at',)
            model = App


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
