from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.exceptions import PermissionDenied
from api_auth.models import User
from api_auth.serializers import UserSerializer, UserDetailSerializer
from api_auth.permissions import UserPermissions

# Create your views here.

class UserViewSet(viewsets.ModelViewSet): # Appel toutes les methodes 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions] 
    
    def perform_create(self, serializer): # La methode set_password permet de hacher le Pw dans la DBase
        instance = serializer.save()
        instance.set_password(serializer.validated_data["password"])
        instance.save()

    def retrieve(self, request, pk=None ): #user by ID
        user = get_object_or_404(self.queryset, pk=pk)
        if not user.can_data_be_shared and user != request.user: #exeption si pas de partage des données et utilisateur different de l'utilisateur de la cession
            raise PermissionDenied(detail="User don't share his-her data") 
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
    
    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]: #update = PUT partial_Update = PATCH
            return UserDetailSerializer # Information complete de l'utilisateur
        else:
            return UserSerializer # Information partielle de l'utilisateur
