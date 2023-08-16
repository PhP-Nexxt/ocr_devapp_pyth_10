from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    age = models.PositiveIntegerField() #Entier Positif
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    
# Pour demain travailler sur les classes (ex :) 
# https://drive.google.com/drive/u/0/folders/1bMQJ8YI6R4Kgw6zvH-YPm6AYtOPiRaAe
class Contributor():
    pass 
    #project = 
    #issue = 
    #comment = 