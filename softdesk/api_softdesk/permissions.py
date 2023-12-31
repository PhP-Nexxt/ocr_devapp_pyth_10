from rest_framework.permissions import BasePermission #class de base de permissions
from api_softdesk.models import Project, Issue


class AuthorPermission(BasePermission): # Les variables afferentes portent le même nom dans model.py = facilite les permissions)
    
    def has_object_permission(self, request, view, obj): # permission s'applique sur l'objet (Commentaire, Issue ou projet)
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', 'POST'] # Methode autorisés à toutes personne connectées
        if request.method in SAFE_METHODS: 
            return True
        else:
            return request.user == obj.author # Methodes authorisé uniquement pour l'auteur (PUT, PATCH, DELETE)
        
class ContributorIssuePermission(BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method == "POST":
            project_id = request.data.get("project")
            project = Project.objects.filter(id=project_id).first() # On récupere un projet a partir de son ID en prenant le premier éléments
            # contributors = project.contributor_set.all().values_list("user", flat=True) # On recupere tous les contributeurs associés au projet dans une liste
            if project:
                is_contributor = project.contributor_set.filter(user=request.user).exists() # Verifie si l'utilisateur fait partie des contributeurs
                if is_contributor or project.author==request.user: # Contributeur ou auteur
                    return True
            return False
        else:
            return True
        
class ContributorCommentPermission(BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method == "POST":
            print(request.data)
            issue_id = request.data.get("issue")
            issue = Issue.objects.filter(id=issue_id).first() # On récupere un issue a partir de son ID en prenant le premier éléments
            # contributors = project.contributor_set.all().values_list("user", flat=True) # On recupere tous les contributeurs associés au projet dans une liste
            if issue:
                is_contributor = issue.project.contributor_set.filter(user=request.user).exists() # Verifie si l'utilisateur fait partie des contributeurs
                if is_contributor or issue.project.author==request.user: # Si autheur ou contributeur True
                    return True
            return False
        else:
            return True
        
class ContributorPermission(BasePermission):
    
    def has_permission(self, request, view):
        
        C_METHOD = ["POST", "DELETE"] # Seul author ou contributor autorise2 sur les requetes POST et DELETE
        if request.method in ["PUT", "PATCH"]:
            return False
        elif request.method in C_METHOD:
            project_id = request.data.get("project")
            project = Project.objects.filter(id=project_id).first() # On récupere un projet a partir de son ID en prenant le premier éléments
            if project:
                if project.author==request.user: # Si autheur ou contributeur True
                    return True
            return False
        else:
            return True
      
    
        
        

        

