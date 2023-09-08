from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.exceptions import PermissionDenied
from api_auth.models import User
from api_auth.serializers import UserSerializer, UserDetailSerializer

# Create your views here.

class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet): # mixin limite au actions que l'on souhaite 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer): # La methode set_password permet de hacher le Pw dans la DBase
        instance = serializer.save()
        instance.set_password(serializer.validated_data["password"])
        instance.save()

    def retrieve(self, request, pk=None ): #user by ID
        user = get_object_or_404(self.queryset, pk=pk)
        if not user.can_data_be_shared:
            raise PermissionDenied(detail="User don't share his-her data")
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
