from rest_framework import viewsets, mixins
from api_softdesk.models import Project, Issue, Contributor
from api_softdesk.serializers import ProjectSerializer, IssueSerializer, ContributorSerializer

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    """
    def perform_create(self, serializer): # La methode set_password permet de hacher le Pw dans la DBase
        instance = serializer.save()
        instance.set_password(serializer.validated_data["password"])
        instance.save()
    """
    
class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    
class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

