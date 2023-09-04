from rest_framework import serializers
from api_auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password", "first_name", "last_name", "age","can_be_contacted", "can_data_be_shared", "id" ]
        extra_kwargs = {'password': {'write_only': True}} #En ecriture uniquement (pas affichage du PW) - extra_kwargs dictionnaire de serializer
