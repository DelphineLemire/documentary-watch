# Prerequisite


This project use: 

- [git](https://git-scm.com/), for versionning
- [Poetry](https://python-poetry.org/docs/), to manage python environment and package dependencies, 
and much more. 

# Installation 

This application use [Django's framework](https://www.djangoproject.com/).
Please get closer to the documentation for the handling of this project.

## For test purpose

### Clone

Clone the repository locally
```
$ git clone https://github.com/DelphineLemire/documentary-watch.git
``` 
### Install virtual environment

Activate virtual environment
```
$ poetry shell
``` 
Install package dependencies

```
$ poetry install
``` 
note: this command not install documentation

### Manage Environment variables

In order for the application to work, environment variables must be defined. 

This project uses the package _[environ](https://github.com/joke2k/django-environ)_ to manage environment variables. 
For this environ uses the _.env_ file at the root of the project. 
You can update this file with your own data. 

So that _environ_ takes into account this file you must add the environment variable _DJANGO_READ_DOT_ENV_FILE=True_
by a traditional method or thanks to pyenv

### Populate database

```
$ python manage.py migrate
``` 
### Create superuser

```
$ python manage.py createsuperuser
``` 

Answer questions

### Launch the application locally

```
$ python manage.py runserver
``` 
_Warning: this way of launching the application is reserved only for demo use or for 
the development of the application._