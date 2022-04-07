from rest_framework import serializers
from .models import App,Plan
from django.contrib.auth import get_user_model


class AppSerializer(serializers.ModelSerializer):

        class Meta:
            fields = ('id', 'user', 'name', 'description',)
            model = App




class PlanSerializer(serializers.ModelSerializer):
    # app = serializers.StringRelatedField(read_only=True,)
    # def getUsername(self, obj):
    #     return obj.user.username
    #
    # username = serializers.SerializerMethodField("getUsername")

    class Meta:
        fields = ('id', 'user', 'app', 'plan',)
        model = Plan


class Subscription_detail_Serializer(serializers.ModelSerializer):
    app = serializers.StringRelatedField(read_only=True,)
    def getUsername(self, obj):
        return obj.user.username
    username = serializers.SerializerMethodField("getUsername")

    class Meta:
        fields = ('id', 'username', 'app', 'plan',)
        model = Plan


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
