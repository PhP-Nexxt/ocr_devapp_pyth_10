from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from api_softdesk.models import Project, Issue, Contributor, Comment
from api_softdesk.serializers import ProjectSerializer, IssueSerializer, ContributorSerializer, CommentSerializer

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    permission_class=[IsAuthenticated] # Indique à api que pas acces sans authentification
    def perform_create(self, serializer): 
        instance = serializer.save(author=self.request.user) # On récupere le user de la cession en cours

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    
class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

