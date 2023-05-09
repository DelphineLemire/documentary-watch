# Développer

## Code de conduite

En tant que développeur, mon intention est de coller aux standards et de suivre la documentation des outils afin de promouvoir
un démarrage rapide pour une nouvelle personne sur le sujet et pour favoriser le travail d'équipe.

- favoriser le commit atomique
- ne pas contourner le fonctionnement d'un outil sans le documenter et surtout sans raison valable.
- n'oubliez pas de supprimer les liens vers les dépôts privés

##Architecture des applications

Cette application utilise [le framework de Django](https://www.djangoproject.com/).
Merci de vous rapprocher de la documentation pour la prise en main de ce projet.

### [Substituer le modèle utilisateur](https://docs.djangoproject.com/fr/4.1/topics/auth/customizing/#substituting-a-custom-user-model)

Ce projet remplace le modèle utilisateur par son propre modèle.

### Backend

Ce projet utilise le mécanisme de création des pages d'administration de [Django admin](https://docs.djangoproject.com/fr/4.1/ref/contrib/admin/).

### Api

[A FAIRE]

### Frontend

Ce projet utilise le [framework css Bulma](https://bulma.io/) et le vanilla javascript. 
Dans un premier temps, il utilisera le [lien CDN pour Bulma](https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css).

[EN COURS]

## Multilingue

Ce projet est traduit en 2 langues; français et anglais

S'assurer qu'un répertoire  *locale/fr/LC_MESSAGES* est présent dans le répertoire de chaque application.

Afin de générer les fichiers de traduction *po* , exécuter la commande suivante
```bash
python manage.py makemessages
```
Après avoir renseigné les phrases traduites, générer les fichiers *mo*  utilisés pour traduire le site web. 
```bash
python manage.py compilemessages
```


## Qualité du code

Ce projet utilise la fonctionnalité de *pre commit*, mais il est possible d'utiliser la commande suivante pour 
vérifier la qualité du code. 

```bash
make check
```
## Documentation

Ce projet utilise Mkdocs avec le thème material pour la documentation. 

Il est possible de tester la génération de la documentation avec la commande suivante

```bash
make check docs-test
```

Afin de générer et rendre disponible la documentation en local, il est possible d'utiliser la commande suivante. 

```bash
make check docs
```

La documentation en production de ce projet est générée par une action de projet sur github. 
