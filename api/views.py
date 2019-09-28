from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from api import serializers, models


class todoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.todoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    queryset = models.todofeed.objects.all()

class userViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.userSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
