from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api import serializers, models


class todoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.todoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    queryset = models.todofeed.objects.all()

    def list(self, request, *args, **kwargs):
        user_id = request.user
        print(user_id)
        res = models.todofeed.objects.filter(user= user_id)
        serializer = serializers.todoSerializer(res, many=True)
        response = {'message': 'todos of the user', 'result': serializer.data}
        return Response(serializer.data, status= status.HTTP_200_OK )

    def create(self, request,*args, **kwargs):
        user_id = request.user
        print('in create method and user : {} and data is: {}'.format(user_id, request.data))
        res = request.data
        res['user'] = user_id.id
        print('res -->>>> {}'.format(res))
        serializer = serializers.todoSerializer(data=res)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_200_OK )


class userViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.userSerializer
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated,)
