from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from api_softdesk.models import Project, Issue, Contributor, Comment
from api_softdesk.serializers import ProjectSerializer, IssueSerializer, ContributorSerializer, CommentSerializer, IssueListSerializer
from api_softdesk.permissions import AuthorPermission, ContributorIssuePermission, ContributorCommentPermission, ContributorPermission # Import de la class concerné
from django.db.models import Q #Queryset qui permet de former des requetes

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().select_related("author") # Queryset par defaut 
    permission_classes=[IsAuthenticated, AuthorPermission] # Indique à api que pas acces sans authentification et avec le bon auteur
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
    
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(author=self.request.user) |Q(contributor__user=self.request.user)) # Acces par l'auteur ou>| le contributeur
        return queryset
   
class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all().select_related("project", "assign_user", "author") # select_related = green code > On appel la requete en une fois
    serializer_class = IssueSerializer
    
    permission_classes=[IsAuthenticated, ContributorIssuePermission, AuthorPermission] # Indique à api que pas acces sans authentification
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
    
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)
      
    def get_queryset(self):
        queryset = super().get_queryset() # Recupere queryset "Greencode"
        queryset = queryset.filter(Q(project__author=self.request.user) |Q(project__contributor__user=self.request.user)) # Acces par l'auteur ou>| le contributeur au projet
        return queryset
     
    def get_serializer_class(self): # ici on choisi le serializer selon ce que l'on vaut faire selon l'action
       if self.action in ["list", "retrieve"]: # Ici on verifie si l'action récuperé est une list(de tous les eléments) un retrieve(detail d'un elément)
          return IssueListSerializer # Ici on envoie la liste 
       else:
          return IssueSerializer
        
    
class ContributorViewSet(viewsets.ModelViewSet): # ici pas de champs author donc pas besoin de recuperer la cession en cours
    queryset = Contributor.objects.all().select_related("project", "user")
    serializer_class = ContributorSerializer
    permission_classes=[IsAuthenticated, ContributorPermission]
    
    def get_queryset(self): 
        queryset = super().get_queryset() # Acces a la fonction initiale
        queryset = queryset.filter(Q(project__author=self.request.user) |Q(user=self.request.user)) # Acces par l'auteur ou>| le contributeur au projet
        return queryset
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().select_related("issue", "author")
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated, AuthorPermission, ContributorCommentPermission] # Indique à api que pas acces sans authentification et il faut etre l'auteur ou le contributeur)
    
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
       
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)
       
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(issue__project__author=self.request.user) |Q(issue__project__contributor__user=self.request.user)) # Acces par l'auteur ou>| le contributeur au projet
        return queryset

"""
select_related et prefetch_related sont deux méthodes de Django ORM 
qui permettent de charger les objets liés à un ensemble d'objets donnés. 
Ces méthodes peuvent être utilisées pour améliorer les performances de 
votre application en réduisant le nombre de requêtes SQL nécessaires.  
La principale différence entre select_related et prefetch_related est 
que select_related charge les objets liés en une seule requête SQL, 
tandis que prefetch_related charge les objets liés en deux requêtes SQL.  
select_related peut être utilisé pour charger les objets liés à un ensemble 
d'objets donnés, lorsque les objets liés sont des objets uniques, 
tels que des objets liés par une relation ForeignKey ou OneToOneField.  
prefetch_related peut être utilisé pour charger les objets liés à un 
ensemble d'objets donnés, lorsque les objets liés sont des ensembles d'objets, 
tels que des objets liés par une relation ManyToManyField
ex 5o projets avec 10 issue par projet = 500-* requetes
"""