import datetime
import requests
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from  rest_framework import viewsets,permissions
from .serialize import UserSerializer,UserVerificationSerializer
from django.http import HttpResponse
from rest_framework import viewsets, permissions

class UserView(viewsets.ModelViewSet):
    serializer_class=UserVerificationSerializer
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    if permission_classes:
        status="True"
        logs="user is authenticated"+ "  " + str(datetime.datetime.now())
        print(logs)
