# Documentary Watch
DelphineLemire/documentary-watch

License : GPLv3

[Documentation](https://delphinelemire.github.io/documentary-watch/)

## Pourquoi? 

C'est un outil pour organiser ma veille documentaire. Quand je lis des articles sur le site Web,
parfois, j'aimerais lire d'autres anciens messages sur le même sujet mais je ne les trouve pas.
Cet outil doit me permettre de garder une vue d'ensemble sur un sujet donné.
Ce projet est pour mon usage personnel mais je le partage sur un référentiel public en tant que projet de portfolio.

## Côté

En tant que développeur, j'aime me concentrer sur les fonctionnalités qui ont de la valeur pour mes clients, donc je m'appuie sur les
des outils qui implémentent déjà un certain nombre de fonctionnalités utiles pour les sites Web et leur déploiement.

### Django

J'ai choisi de m'appuyer sur le framework [django](https://www.djangoproject.com/), un projet opensource, avec une large communauté,
fournissant des fonctionnalités génériques à toute application Web.
Par exemple, avec django, je peux développer rapidement des écrans d'administration d'informations et les notions d'authentification
et les droits d'accès sont nativement mis à disposition.

### Poetry

Je me suis inspiré de [cookiecutter-poetry](https://fpgmaas.github.io/cookiecutter-poetry/) pour adapter le
projet au gestionnaire du paquet de poésie.


J'ai choisi [poetry](https://python-poetry.org/) car en termes de gestion d'environnement virtuel, cela me semble très réussi ;
limite les oublis, et facilite les ajouts, mises à jour, suppressions de packages.

J'ai choisi [ruff](https://github.com/charliermarsh/ruff) recommandé par le projet cookiecutter-poetry comme outil de contrôle de la qualité du code, car il comprend un grand
nombre d'outils, notamment les versions de flake8 et il s'intègre parfaitement à la poésie.

N'hésitez pas à commenter pour l'améliorer.
