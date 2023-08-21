from django.db import models
from api_auth.models import User

# Create your models here.

# Pour demain travailler sur les classes (ex :) 
# https://drive.google.com/drive/u/0/folders/1bMQJ8YI6R4Kgw6zvH-YPm6AYtOPiRaAe
    
class Project(models.Model):
    # Choix du type (List de choix limité)
    TYPE_CHOICE = (
        ("back-end", "back-end"),
        ("front-end", "front-end"),
        ("iOS", "iOS"),
        ("Andoid", "Android"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=10, choices = TYPE_CHOICE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Contributor(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)