# ocr_devapp_pyth_10
Repository Projet 10 - Dev Application Python

OCR_Projet10_SoftDesk

Ce projet est réalisé dans le cadre de la formation OpenClassrooms Développeur d'Applications Python Il s'agit de ...

Les fonctionnalités sont les suivantes : 
...

Installation & lancement :

Installer Python en version 3.8.8 Lancez un terminal et placez vous dans le dossier de votre choix puis clonez le repository: git clone https://github.com/PhP-Nexxt/ocr_devapp_pyth_10

Placez vous dans le dossier ocr_devapp_pyth_10, puis créez un environnement virtuel:

python -m venv venv_softdesk

Ensuite, activez-le Sur MacOs/Linux source venv_litreview/bin/activate Sur Windows:venv_litereview\scripts\activate.bat

Installez ensuite les packages requis: pip install -r requierement.txt

Puis placez vous à la racine du projet (là ou se trouve le fichier manage.py), et effectuez les migrations: python manage.py makemigrations python manage.py migrate

Lancer le serveur: python manage.py runserver

Vous pouvez ensuite utiliser l'applicaton avec l'url : 