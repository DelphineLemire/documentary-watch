# Documentary Watch
DelphineLemire/documentary-watch

License : GPLv3

[Documentation](https://delphinelemire.github.io/documentary-watch/)

## Why? 

C'est un outil for organize my documentary watch . When I read posts website, 
sometimes, I would like to read other old posts on the same topic but I can't find them. 
This tool should allow me to keep an overview on a given subject.
This project is for my personal use but I share on public repository as a portfolio's project. 

## On the technical side 

As a developer, I like to focus on features that are of value to my clients, so I rely on existing 
tools that already implement a number of useful features for websites and their deployment.

### Django

I chose to rely on the [django](https://www.djangoproject.com/) framework, an opensource project, with a large community, 
providing generic functionalities to any web application. 
For example, with django , I can quickly develop info admin screens and the notions of authentication 
and access rights are natively made available.

### Poetry

I was inspired by [cookiecutter-poetry](https://fpgmaas.github.io/cookiecutter-poetry/) to adapt the 
project to the poetry package manager.


I chose [poetry](https://python-poetry.org/) because in terms of virtual environment management, it seems very successful to me; 
limits omissions, and facilitates additions, updates, deletions of packages. 

I chose [ruff](https://github.com/charliermarsh/ruff) recommended by the cookiecutter-poetry project as a code quality control tool, because it includes a large 
number of tools, in particular the versions of flake8 and it integrates perfectly with poetry.

Do not hesitate to comment to improve it. 
