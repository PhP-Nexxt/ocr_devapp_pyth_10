from rest_framework import serializers
from api_softdesk.models import Project, Contributor, Issue, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title","description", "type", "author", "id","created_time"]
        extra_kwargs = {'author': {'read_only': True}} # Mettre le champs author en lecture seule(afin que celui-ci ne puisse etre modifié via un post)
        
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ["title","description", "assign_user", "priority", "tag", "status", "project", "author", "id", "created_time"]
        extra_kwargs = {'author': {'read_only': True}} # Mettre le champs author en lecture seule(afin que celui-ci ne puisse etre modifié via un post)
    
    def validate(self, data): # Verifie si l'utilisateur fait partie des contributeurs
        assign_user = data.get("assign_user")
        project = data.get("project")
        is_contributor = project.contributor_set.filter(user=assign_user).exists() 
        if not is_contributor and project.author != assign_user:
            raise serializers.ValidationError(
                "User is not contributor to this project"
            )
        else:
            return data

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["project", "user", "id", "created_time"]
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["issue", "description", "uid", "author", "id", "created_time"]
        extra_kwargs = {'uid': {'read_only': True},'author':{'read_only': True}} # Mettre le champs uid et author en lecture seule
        
class IssueListSerializer(serializers.ModelSerializer): 
    class EMBEDDEDProjectSerializer(serializers.ModelSerializer): # Ici on cree une class project serializer à l'interieur de issue
        class Meta:
            model = Project
            fields = ["title", "id"]
    project = EMBEDDEDProjectSerializer()
    class Meta:
        model = Issue
        fields = ["title","description", "assign_user", "priority", "tag", "status", "project", "author", "id", "created_time"]
        extra_kwargs = {'author': {'read_only': True}} # Mettre le champs author en lecture seule(afin que celui-ci ne puisse etre modifié via un post)
        