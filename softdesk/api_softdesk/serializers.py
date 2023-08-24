from rest_framework import serializers
from api_softdesk.models import Project, Contributor, Issue, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title","description", "type", "author", "id"]
        extra_kwargs = {'author': {'read_only': True}} # Mettre le champs author en lecture seule(afin que celui-ci ne puisse etre modifié via un post)
        
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ["title","description", "assign_user", "priority", "tag", "status", "project", "author", "id"]
        
class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["project", "user", "id"]
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["issue", "description", "uid", "author", "id"]
        extra_kwargs = {'uid': {'read_only': True}} # Mettre le champs uid en lecture seule
        
