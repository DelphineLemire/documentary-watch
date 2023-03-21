# Installation

## Prérequis

Ce projet utilise :

- [git](https://git-scm.com/), pour le versionning
- [Poetry](https://python-poetry.org/docs/), pour gérer l'environnement python et les dépendances des packages,
et beaucoup plus.
- [Nodejs](https://nodejs.org/en), [npm](https://www.npmjs.com/) pour gérer les actifs

## Mise en place

Cette application utilise [le framework de Django](https://www.djangoproject.com).
Merci de vous rapprocher de la documentation pour la prise en main de ce projet.

### À des fins de test

#### Cloner

Cloner le référentiel localement
```
$ git clone https://github.com/DelphineLemire/documentary-watch.git
```
####  Installer l'environnement virtuel

Activer l'environnement virtuel
```
$ coquille de poésie
```
Installer les dépendances du package

```
installation de poésie $
```
note: cette commande n'installe pas la documentation

####  Gérer les variables d'environnement

Pour que l'application fonctionne, des variables d'environnement doivent être définies.

Ce projet utilise le package _[environ](https://github.com/joke2k/django-environ)_ pour gérer les variables d'environnement.
Pour cet environnement utilise le fichier _.env_ à la racine du projet.
Vous pouvez mettre à jour ce fichier avec vos propres données.

Pour que _environ_ prenne en compte ce fichier vous devez ajouter la variable d'environnement _DJANGO_READ_DOT_ENV_FILE=True_
par une méthode traditionnelle ou grâce au pyenv

####  Remplir la base de données

```
$ python manage.py migre
```
####  Créer un superutilisateur

```
$ python manage.py createsuperuser
```

Répondez aux questions

####  Gérer les actifs

Poussez le fichier js dans le répertoire statique/js
```
$ npm courir babel
```
Poussez et regardez le fichier de feuille de style dans le répertoire statique/css
```
$ npm exécuter sass
```

####  Lancer l'application localement

```
$ python manage.py serveur d'exécution
```
_Attention : ce mode de lancement de l'application est réservé uniquement à un usage démo ou
le développement de l'application._