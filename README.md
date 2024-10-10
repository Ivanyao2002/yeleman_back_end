# Back-End du projet devellopé par la Team Yeleman CI
***
***
****


## Contexte
> Notre projet vise à mettre en place une application permettant de rapprocher les propriétaires de maisons et 
leurs futures locataires. Nous nous sommes donnés pour vocation de simplifier les démarches énergivores et couteuses en lien avec les locations de logements. A travers notre application, nous garantissons un confort à la fois pour les locataires et les propriétaires de logements grace à nos procédures simplifiées.


### Nos développeurs

1. [ ]  YAO DAMO IVAN ODILON (Lead Technique)
2. [ ]  KONE KOLOTIOLOMAN DIEUDONNE
3. [ ]  KONATE AISSATA
4. [ ]  COULIBALY ROKIA
5. [ ]  KOFFI KOUADIO FRANCK VICTORIEN


## Liste des fonctionnalités

1. [ ]  Administrateur
- Validation du dossier des propriétaires
- Génération de contrats
2. [ ]  Propriétaire
- Validation des demandes de visite
3. [ ]  Locataire
- Demande de visite

## Les étapes d'installation de l'application :
- Ouvrer un terminal puis cloner le lien github de l'application : 
```bash
 git clone https://github.com/Ivanyao2002/Fitness_tracking_api.git
 ```
- Créer un environnement virtuel dans le repertoire 
```bash
 python -m venv venv ou env ( Pour windows )
 python3 -m venv venv ou env ( Pour Unix ) 
 ```
- Naviguer vers le fichier activate.bat soit dans scripts ou bin, puis activer l'environnement 
```bash
 source activate ( Pour Unix ) 
 activate ( Pour windows) 
 ```
- Revener au repertoire de votre projet puis installer les dépendances de l'application à partir du fichier requirements.txt
```bash
 pip install -r requirements.txt ( Pour windows ) 
 pip3 install -r requirements.txt ( Pour Unix )
 ```
- Installez et configurez une base de données Postgresql 'forum_db' configurer les accès dans le fichier settings.py
- Naviguez vers le repertoire source (src) puis créer et appliquer les migrations 
```bash
 python manage.py makemigrations 
 python manage.py migrate
 ``` 
 
## Les instructions de démarrage :
- Naviguez vers le repertoire source (src) puis lancer le server
```bash
 python manage.py runserver 
 ``` 
- Vous pouvez tester avec le navigateur ou avec Postman 
- Lien vers l'api : http://127.0.0.1:8000/api/
- Lien vers la documentation : 

