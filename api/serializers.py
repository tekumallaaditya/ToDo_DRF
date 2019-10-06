from rest_framework import serializers
from api import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class todoSerializer(serializers.ModelSerializer):
    """This is to serialize the todo feed"""

    class Meta:
        model = models.todofeed
        fields = ('id', 'item', 'status', 'user')


class userSerializer(serializers.ModelSerializer):
    """this is used during user creation"""

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


    def create(self, validated_data):
        print('inside the create user method')
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user= user)
        return user





