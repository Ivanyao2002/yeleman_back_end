# Back-End du projet devellopé par la Team Yeleman CI
***
***
****


## Contexte
> Notre projet vise à mettre en place une application permettant de rapprocher les propriétaires de maisons et 
leurs futures locataires. Nous nous sommes donnés pour vocation de simplifier les démarches énergivores et couteuses en lien avec les locations de logements. A travers notre application, nous garantissons un confort à la fois pour les locataires et les propriétaires de logements grace à nos procédures simplifiées.


## Liste des fonctionnalités

1. [ ]  Administrateur
- Validation du dossier des propriétaires
- Ajout des formules de souscriptions
- Génération de contrats

2. [ ]  Propriétaire
- Ajout de propriétés
- Validation des demandes de visite
- Validation des demandes de locations
- Souscription au compte premium

3. [ ]  Locataire
- Demande de visite
- Demande de location
- Souscription au compte premium

## Les étapes d'installation de l'application :
- Ouvrer un terminal puis cloner le lien github de l'application : 
```bash
 git clone https://github.com/Ivanyao2002/yeleman_back_end.git
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

## Variables du Fichier .env

```plaintext
# Clé secrète utilisée pour la sécurité de l'application
SECRET_KEY='votre_cle_secrete'

# Mode de débogage (True pour le développement, False pour la production)
DEBUG=True  # À mettre sur False en production

# Hôtes autorisés pour la connexion à l'application
ALLOWED_HOSTS='localhost,127.0.0.1,*'
CORS_ALLOWED_ORIGINS='http://localhost:4200'  # Hostname ou IP de l'application Angular
CSRF_TRUSTED_ORIGINS='http://localhost:4200'

# Configuration de la base de données
SQL_ENGINE='django.db.backends.postgresql'
SQL_DATABASE='nom_de_la_base_de_donnees'
SQL_USER='nom_utilisateur'
SQL_PASSWORD='votre_mot_de_passe'
SQL_HOST='adresse_ip_ou_hostname'
SQL_PORT='port_de_la_base_de_donnees' 

# Configuration de l'envoi de mail
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='votre_adresse_mail'
EMAIL_HOST_PASSWORD='votre_mot_de_passe'
DEFAULT_FROM_EMAIL="Titre"

# Configuration de Cloudinary pour la gestion des médias
CLOUDINARY_CLOUD_NAME='votre_nom_de_cloud'
CLOUDINARY_API_KEY='votre_api_key'
CLOUDINARY_API_SECRET='votre_api_secret'
 ``` 
 
## Les instructions de démarrage :
- Naviguez vers le repertoire source (src) puis lancer le server
```bash
 python manage.py runserver 
 ``` 
- Vous pouvez tester avec le navigateur ou avec Postman 
- Lien vers l'api : http://127.0.0.1:8000/api/
- Lien vers la documentation : http://127.0.0.1:8000/api/swagger/

