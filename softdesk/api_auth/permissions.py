from rest_framework.permissions import BasePermission #class de base de permissions

class UserPermissions(BasePermission):
  
    def has_permission(self, request, view):
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS'] # Methode autorisés à toutes personne connectées
        pk = view.kwargs.get('pk') # Ici on recupere l'ID qui est passé en parametre
        
        USER_METHODS = ['PUT', 'PATCH', 'DELETE']
        if request.method in USER_METHODS and request.user and request.user.is_authenticated: # Il faut etre authentifié pour PUT PATCH DELETE
            return int(pk)==request.user.id # Possible uniquement si id user = id cession en cours (en parametre)
        elif request.method in SAFE_METHODS and request.user and request.user.is_authenticated: # Il faut que le User soit connecté quand il fait un GET 
            return True
        elif request.method=="POST": # Le User peut faire un POST sans etre connecté
            return True
        else:
            return False
        
    

