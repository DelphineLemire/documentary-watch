# Develop

## Code of conduct

As a developer, my intention is to stick to the standards and follow the documentation of the tools in order to promote 
a quick start for a new person on the subject and to promote teamwork.

- favor atomic commit
- do not circumvent the operation of a tool without documenting it and especially without good reason.
- don't forget to remove links to private repositories

## Application architecture

This application uses [Django's framework](https://www.djangoproject.com/).
Please get closer to the documentation for the handling of this project.

### [Substituting a custom User Model ](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model)

This project replaces the user model with its own model.

### Backend

This project uses the default [Django's admin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/) 

### Api

[TODO]

### Frontend

This project uses [Framework CSS Bulma](https://bulma.io/) and Vanilla Javascript.
In a first time, It uses [Bulma's cdn link](https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css).

[IN PROGRESS]

## Internationalization

This project is translated into 2 languages; english and french. 

Make sure that a *locale/fr/LC_MESSAGES* directory is present in the directory of each of your applications

In order to generate translation file *po* 
```bash
python manage.py makemessages --all
```
After populated translated sentences, you must made to generate file *mo*, used to translate website
```bash
python manage.py compilemessages
```


## Code Quality 

This project uses a pre commit hook, but you can use next command to control code's quality

```bash
make check
```
## Documentation

This project uses Mkdocs with material theme for documentation.

You can test documentation generation with next command

```bash
make check docs-test
```

In order to generate and serve documentation on local, you can use the next command

```bash
make check docs
```

Production's documentation is serve from an action on project's github repository