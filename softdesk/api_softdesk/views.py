from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from api_softdesk.models import Project, Issue, Contributor, Comment
from api_softdesk.serializers import ProjectSerializer, IssueSerializer, ContributorSerializer, CommentSerializer
from api_softdesk.permissions import AuthorPermission, ContributorIssuePermission, ContributorCommentPermission # Import de la class concerné
from django.db.models import Q #Queryset qui permet de former des requetes

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProjectSerializer
    queryset = Project.objects.all() # Queryset par defaut 
    permission_classes=[IsAuthenticated, AuthorPermission] # Indique à api que pas acces sans authentification et avec le bon auteur
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
    
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Project.objects.filter(Q(author=self.request.user) |Q(contributor__user=self.request.user)) # Acces par l'auteur ou>| le contributeur
        return queryset
   
class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    
    permission_classes=[IsAuthenticated, ContributorIssuePermission, AuthorPermission] # Indique à api que pas acces sans authentification
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
    
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)
      
    def get_queryset(self):
        queryset = Issue.objects.filter(Q(project__author=self.request.user) |Q(project__contributor__user=self.request.user)) # Acces par l'auteur ou>| le contributeur au projet
        return queryset
    
class ContributorViewSet(viewsets.ModelViewSet): # ici pas de champs author donc pas besoin de recuperer la cession en cours
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes=[IsAuthenticated]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated, AuthorPermission, ContributorCommentPermission] # Indique à api que pas acces sans authentification et il faut etre l'auteur ou le contributeur)
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
    
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)
       
    def get_queryset(self):
        queryset = Comment.objects.filter(Q(issue__project__author=self.request.user) |Q(issue__project__contributor__user=self.request.user)) # Acces par l'auteur ou>| le contributeur au projet
        return queryset

