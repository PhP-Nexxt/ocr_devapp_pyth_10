from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from api_softdesk.models import Project, Issue, Contributor, Comment
from api_softdesk.serializers import ProjectSerializer, IssueSerializer, ContributorSerializer, CommentSerializer
from api_softdesk.permissions import AuthorPermission, ContributorPermission # Import de la class concerné

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProjectSerializer
    
    permission_classes=[IsAuthenticated, AuthorPermission] # Indique à api que pas acces sans authentification et avec le bon auteur
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
    
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Project.objects.filter(author=self.request.user)
        return queryset
   
class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    
    permission_classes=[IsAuthenticated, ContributorPermission, AuthorPermission] # Indique à api que pas acces sans authentification
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
    
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)
    
class ContributorViewSet(viewsets.ModelViewSet): # ici pas de champs author donc pas besoin de recuperer la cession en cours
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes=[IsAuthenticated]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated, AuthorPermission] # Indique à api que pas acces sans authentification et il faut etre l'auteur)
    def perform_create(self, serializer): 
       serializer.save(author=self.request.user) # On récupere uniquement user de la cession en cours (authentifié)
    
    def perform_update(self, serializer): # On recupere uniquement user de la cession en cours (authentifié)
       serializer.save(author=self.request.user)

