## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt` (Si de nouvelles dépendances sont ajoutées, executer `pip freeze > requirements.txt`afin des les ajouter au fichier requirements.txt)
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Prérequis

- [S'inscrire sur CircleCI](https://circleci.com/signup/)  et lier le compte Github
- [S'inscrire sur DockerHub](https://hub.docker.com/)
- [S'inscrire sur Heroku](https://signup.heroku.com/) et créer une nouvelle application

Fonctionnement du déploiement

- CircleCI sert d'orchestrateur, toute les étapes du déploiement sont configurées dans le fichier .circleci/config.yml.
- Dans sa configuration actuelle, CircleCI: 
  - Effectue le linting et les tests sur un conteneur docker python
  - Construit l'image docker nommée oc-lettings et la publie sur le compte Dockerhub en la taguant avec le hash de commit de CircleCI, si les tests sont valides
  - Deploie cette image sur heroku, si la construction et la publication sur Dockerhub sont valides
  - La construction de l'image et son déploiement ne s'effectuent que pour des changements sur la branche principale du projet

Configuration de CircleCI

- Une fois le compte Github rélié à CircleCI, aller sur la page projects.
- Sur la ligne du repository que l'on souhaite, afficher les options du projet en cliquant sur Project Settings.
- Aller sur l'onglet Environment Variables et ajouter: 
  - Une variable nommée DOCKERHUB_USER ayant pour valeur le nom d'utilisateur Dockerhub
  - Une variable nommée DOCKERHUB_PWD ayant pour valeur le mot de passe du compte Dockerhub
  - Une variable nommée HEROKU_APP_NAME ayant pour valeur le nom de l'application créee sur Heroku
  - Une variable nommée HEROKU_API_KEY ayant pour valeur la clé API d'Heroku (pour la retrouver ou en générer une nouvelle, cliquer sur l'avatar Heroku et aller sur la page de paramètres du compte)
- Retourner sur la page des projets de CircleCI et suivre le projet en choisissant l'option la plus rapide (utliser le fichier .circleci/config.yml présent dans le repo)
