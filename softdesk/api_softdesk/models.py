import uuid # Generer un "Universally Unique Identifier (UUID)"
from django.db import models
from api_auth.models import User

# Create your models here.

    
class Project(models.Model):
    # Choix du type (List de choix limité)
    TYPE_CHOICE = (
        ("back-end", "back-end"),
        ("front-end", "front-end"),
        ("iOS", "iOS"),
        ("Android", "Android"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=10, choices = TYPE_CHOICE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self): # Creation d'un representant en utilisant le titre (et non l'objet)
        return self.title
    
class Contributor(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # Il ne peut pas avoir 2 fois le meme contributeur sur un projet
    class Meta:
        unique_together=("project", "user")
        
    
class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assign_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assign_user")
    
    # Choix de la priorité
    PRIORITY_CHOICE = (
        ("law", "law"),
        ("medium", "medium"),
        ("hight", "hight"),
    )
    priority = models.CharField(max_length=10, choices = PRIORITY_CHOICE)
    
    # Choix de la balise
    TAG_CHOICE = (
        ("bug", "bug"),
        ("feature", "feature"),
        ("task", "task"),
    )
    tag = models.CharField(max_length=10, choices = TAG_CHOICE)
    
    STATUS_CHOICE = (
        ("to_do", "to_do"),
        ("in_progress", "in_progress"),
        ("finished", "finished"),
    )
    status = models.CharField(max_length=20, choices = STATUS_CHOICE, default="to_do")
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="author")
    
    def __str__(self): # Creation d'un representant en utilisant le titre (et non l'objet)
        return self.title
   
class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.TextField()
    uid = models.CharField(max_length=100, default=str(uuid.uuid4())) # Appel uuid v4 exadecimal 32 caracteres)
    author = models.ForeignKey(User,on_delete=models.CASCADE) # Lien avec author
        