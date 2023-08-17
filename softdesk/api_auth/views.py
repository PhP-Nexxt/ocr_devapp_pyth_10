from django.shortcuts import render
from rest_framework import viewsets, mixins
from api_auth.models import User
from api_auth.serializers import UserSerializer

# Create your views here.

class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet): # mixin limite au actions que l'on souhaite 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer): # La methode set_password permet de hacher le Pw dans la DBase
        instance = serializer.save()
        instance.set_password(serializer.validated_data["password"])
        instance.save()

