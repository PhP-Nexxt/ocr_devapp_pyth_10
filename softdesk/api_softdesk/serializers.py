from rest_framework import serializers
from api_softdesk.models import Project, Contributor, Issue

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title","description", "type", "author"]
        # extra_kwargs = {'password': {'write_only': True}} #En ecriture uniquement (pas affichage du PW) - extra_kwargs dictionnaire de serializer

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ["title","description", "assign_user", "priority", "tag", "status", "project", "author"]
        
class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["project", "user"]
        
