from rest_framework.permissions import BasePermission #class de base de permissions
from api_softdesk.models import Project


class AuthorPermission(BasePermission): # Les variables afferentes portent le même nom dans model.py = facilite les permissions)
    
    def has_object_permission(self, request, view, obj): # permission s'applique sur l'objet (Commentaire, Issue ou projet)
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', 'POST'] # Methode autorisés à toutes personne connectées
        if request.method in SAFE_METHODS: 
            return True
        else:
            return request.user == obj.author # Methodes authorisé uniquement pour l'auteur (PUT, PATCH, DELETE)
        
class ContributorPermission(BasePermission):
    
    """
    def has_object_permission(self, request, view, obj):# obj represente un objet issue
        project = obj.project #On associe l'objet project associé à l'issue
        contributors = project.contributor_set.all() # On recupere tous les contibuteurs associés au projet
        if request.method == "POST":
            return False
        else:
            return True
    """
    
    def has_permission(self, request, view):
        
        
        if request.method == "POST":
            print(request.data)
            project_id = request.data.get("project")
            project = Project.objects.filter(id=project_id).first() # On récupere un projet a partir de son ID en prenant le premier éléments
            # contributors = project.contributor_set.all().values_list("user", flat=True) # On recupere tous les contributeurs associés au projet dans une liste
            if project:
                is_contributor = project.contributor_set.filter(user=request.user).exists() # Verifie si l'utilisateur fait partie des contributeurs
            return False
        else:
            return True
      
        
        

        

