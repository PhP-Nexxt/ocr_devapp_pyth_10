from rest_framework.permissions import BasePermission #class de base de permissions


class AuthorPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj): # permission s'applique sur l'objet (Commentaire, Issue ou projet)
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', 'POST']
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user == obj.author # Les variables afferentes portent le même nom dans model.py = facilite les permissions)
        