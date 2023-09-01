from rest_framework.permissions import BasePermission #class de base de permissions
from api_softdesk.models import Project


class AuthorPermission(BasePermission): # Les variables afferentes portent le même nom dans model.py = facilite les permissions)
    
    def has_object_permission(self, request, view, obj): # permission s'applique sur l'objet (Commentaire, Issue ou projet)
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', 'POST'] # Methode autorisés à toutes personnews connectées
        if request.method in SAFE_METHODS: 
            return True
        else:
            return request.user == obj.author # Methodes authorisé uniquement pour l'auteur (PUT, PATCH, DELETE)
        
class ContributorPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj):# obj represente un objet issue
        project = obj.project #On associe l'objet project associé à l'issue
        contributors = project.contributor_set.all() # On recupere tous les contibuteurs associés au projet
        if request.method == "POST":
            return False
        else:
            return True
    
    def has_permission(self, request, view):
        print(request.data)
        project_id = request.data.get("project")
        project = Project.objects.get(id=project_id) # On récupere un projet a partir de son ID
        contributors = project.contributor_set.all().values_list("user", flat=True) # On recupere tous les contibuteurs associés au projet dans une liste
        # is_contributor = project.contributor_set.filter(user=user).exists()
        
        print(contributors)
        if request.method == "POST":
            return False
        else:
            return True
      
        
        

        

