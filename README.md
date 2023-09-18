# ocr_devapp_pyth_10
Repository Projet 10 - Dev Application Python

Ce projet est réalisé dans le cadre de la formation OpenClassrooms Développeur d'Applications Python. Il s'agit de créer une API RESTful securisée avec Django REST. Ceci pour le compte de la societe fictive 'SoftDesk"

Les fonctionnalités sont les suivantes : 

Gestion des utilisateurs
- L’application prend en compte les choix de confidentialité de chaque utilisateur
en implémentant deux attributs : can_be_contacted (peut être contacté) : oui ou
non, et can_data_be_shared (peut-on partager les données) : oui ou non.
- Selon les normes RGPD, un utilisateur doit avoir plus de 15 ans pour collecter
ses données avec son consentement. Pour cela, nous récupérons et vérifions
son âge lors de l’inscription.
- Un utilisateur peut s’authentifier à l’application grâce à un username et un
password. L’authentification retourne un Json Web Token.
- L'utilisateur s’identifie dans chaque requête grâce au Json Web Token.
Gestion des projets
- Un utilisateur peut créer un projet. Il en devient l’auteur et le contributeur.
- Lors de la création, l’utilisateur doit pouvoir nommer le projet, ajouter une
description ainsi qu’un type (back-end, front-end, iOS ou Android).
- Le contributor est une ressource spécifique, qui lie un utilisateur à un projet.

- Seuls les contributeurs d’un projet peuvent accéder à ce dernier. Seuls les
contributeurs peuvent accéder aux ressources qui référencent un projet (l’issue
et le comment).
Créations des tâches et des problèmes
- Un contributeur qui travaille sur un projet doit pouvoir créer des Issues
(tâches/problèmes). Ces issues permettent de planifier des fonctionnalités à
mettre en œuvre ou des bugs à régler dans un projet donné.
- Lors de la création de l’issue, le contributeur doit pouvoir la nommer et ajouter
une description. Il doit aussi pouvoir assigner l’issue à un autre contributeur s’il
le souhaite. Attention, seuls les contributeurs du projet correspondant à l’issue
sont sélectionnables.
- Nous pouvons donner une priorité à l’issue (LOW, MEDIUM ou HIGH) pour
connaître son importance.
- Nous pouvons aussi donner une balise (BUG, FEATURE ou TASK) pour connaître
la nature de l’issue.
- Enfin, les contributeurs doivent pouvoir émettre un statut de progression (To
Do, In Progress ou Finished). Par défaut, une issue est en To Do.
Créations des commentaires pour faciliter la communication
- Afin de mieux cerner les problèmes et faciliter la communication, les
contributeurs d’un projet peuvent commenter les issues de ce projet grâce aux
comments.
- L’auteur d’un commentaire écrit un texte qui sera sauvegardé en tant que
description.
- Il doit aussi donner un lien vers une issue.
- Enfin, un identifiant unique de type uuid est automatiquement généré. Ce
dernier permet de mieux référencer le comment.
Informations complémentaires
- Chaque ressource doit posséder un horodatage (created_time), afin de savoir
quand la ressource a été créée.
Définition des auteurs
- Chaque ressource hors utilisateur doit posséder un author (auteur).
- L’auteur d’une ressource peut modifier ou supprimer cette ressource. Les autres
utilisateurs ne peuvent que lire la ressource.
Mise en place de la pagination
- Un système de pagination est implémenté pour le listage des ressources.


# Installation & lancement :

Installer Python en version 3.8.8 Lancez un terminal et placez vous dans le dossier de votre choix puis clonez le repository: `git clone https://github.com/PhP-Nexxt/ocr_devapp_pyth_10`

Placez vous dans le dossier ocr_devapp_pyth_10, puis créez un environnement virtuel:

`python -m venv venv_softdesk`

Ensuite, activez-le sur MacOs/Linux `source venv_softdesk/bin/activate` - ou sur Windows `venv_softdesk\scripts\activate.bat`

Installez ensuite les packages requis: `pip install -r requierement.txt`

Puis placez vous à la racine du projet (là ou se trouve le fichier manage.py), et effectuez les migrations: `python manage.py makemigrations` `python manage.py migrate`

Lancer le serveur: `python manage.py runserver`

Vous pouvez ensuite utiliser l'applicaton via les différents endpoints décrits dans la documentation en utilisant postman. Pour cela, vous devez d'abord créer un compte utilisateur à l'endpoint `http://127.0.0.1:8000/api/auth/user/` afin d'accéder aux fonctionnalités de l'application.