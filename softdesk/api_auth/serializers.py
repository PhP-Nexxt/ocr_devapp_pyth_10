from rest_framework import serializers
from api_auth.models import User

class UserSerializer(serializers.ModelSerializer): 
    # age = serializers.IntegerField(min_value=15) # Age min pour inscription = 15 ans
    class Meta:
        model = User
        fields = ["username","password", "first_name", "last_name", "age","can_be_contacted", "can_data_be_shared", "id" ]
        extra_kwargs = {'password': {'write_only': True},
                        'last_name': {'write_only': True},
                        'first_name': {'write_only': True},
                        'age': {'write_only': True, "min_value":15}, # Age min pour inscription = 15 ans
                        'can_data_be_shared': {'write_only': True},
                        'can_be_contacted': {'write_only': True},
                        } #En ecriture uniquement (pas affichage du PW) - extra_kwargs dictionnaire de serializer

class UserDetailSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=15) # Age min pour inscription = 15 ans
    class Meta:
        model = User
        fields = ["username","password", "first_name", "last_name", "age","can_be_contacted", "can_data_be_shared", "id" ]
        extra_kwargs = {'password': {'write_only': True}} #En ecriture uniquement (pas affichage du PW) - extra_kwargs dictionnaire de serializer
