# Django Project Structure
This is a template/project structure for developing django-based applications -
either strictly through the `django-rest-framework` or just `django`.

The project is meant to be easily clonable, and used as the starter template for
the next big thing our team develops.


## Scope
Develop a structure for both `django-rest-framework` and `django` projects.
Easily clonable when starting new projects
Folder structure only, not “best practices”
No questions, instead we’ll have everything raised as an issue in a repository
We won’t be talking about best practices in implementation details
We’ll hold all questions in a GitHub repository, so things can move forward
The discussions also serve historic significance - people can backtrack why some
decisions were made.


## Project Tree
```bash
.
├── apps
│   ├── app_one # A Django Rest Framework Project
│   │   ├── api
│   │   │   ├── v1
│   │   │   │   ├── __init__.py
│   │   │   │   ├── serializers.py
│   │   │   │   ├── services.py
│   │   │   │   ├── tests.py
│   │   │   │   ├── urls.py
│   │   │   │   └── views.py
│   │   │   ├── v2
│   │   │   │   ├── __init__.py
│   │   │   │   ├── serializers.py
│   │   │   │   ├── services.py
│   │   │   │   ├── tests.py
│   │   │   │   ├── urls.py
│   │   │   │   └── views.py
│   │   │   └── __init__.py
│   │   ├── management
│   │   │   ├── commands.py
│   │   │   └── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── templates
│   │   ├── tests
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   └── app_two # A normal Django project
│       ├── migrations
│       │   └── __init__.py
│       ├── templates
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── models.py
│       ├── service.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── config
│   ├── settings
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── __init__.py
│   │   ├── local.py
│   │   ├── local_template.py
│   │   └── production.py
│   ├── asgi.py
│   ├── __init__.py
│   ├── urls.py
│   └── wsgi.py
├── deployments
│   ├── django-project
│   │   └── Dockerfile
│   ├── nginx
│   │   ├── default.conf
│   │   └── Dockerfile
│   └── docker-compose.yml
├── docs
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── deployment.md
│   ├── local-development.md
│   └── swagger.yaml
├── requirements
│   ├── common.txt
│   ├── development.txt
│   ├── local.txt
│   └── production.txt
├── static
├── entrypoint.sh
├── manage.py
├── pytest.ini
└── README.md

```

## Rationale
Each `app` should be designed in way to be pluggable, that is, dragged and dropped
into any other project and it’ll work independently.

* We won’t have a `core` in our projects. This should be maintained separately
and versioned accordingly as a library.

### `apps`
* A mother-folder containing all apps for our project.
* An app can be a django template project, or an api

#### `api`
* We like to place all our API components into a package within an app called
api/. That allows us to isolate our API components in a consistent location. If
we were to put it in the root of our app, then we would end up with a huge list
of API-specific modules in the general area of the app.

For projects with a lot of small, interconnecting apps, it can be hard to hunt
down where a particular API view lives. In contrast to placing all API code
within each relevant app, sometimes it makes more sense to build an app
specifically for the API. This is where all the serializers, renderers, and views
are placed. Therefore, the name of the app should reflect its API version

##### `api-versioning`
It might often be necessary to support multiple versions of an API throughout the lifetime of a project. Therefore, we're adding in support right from the start.

For different API versions, we're assuming the following will change:
- Serializers
- Views
- URLs
- Services

Whereas the `model`s will be shared.

### `config`
* Contains project configuration files, including the primary URL file
* Contains settings split into `base`, `local`, `production` and `development`


### `deployments`
* Contains Docker and nginx specific files for deploying in different
environments


### `documentation`
* We’ll have CHANGELOG.md
* We’ll have CONTRIBUTING.md
* We’ll have deployment instructions
* We’ll have local instructions


### `services`
* We’ll be writing business logic in services instead of anywhere else.


### `gitignore`
* https://github.com/github/gitignore/blob/main/Python.gitignore


## References
- [Two Scoops of Django by Daniel and Audrey Feldroy](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [Django Best Practices](https://django-best-practices.readthedocs.io/en/latest/index.html)
- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- [HackSoft Django Style Guide](https://github.com/HackSoftware/Django-Styleguide)
- [Radoslav Georgiev - Django Structure for Scale and Longevity](https://www.youtube.com/watch?v=yG3ZdxBb1oo)
- Vaccina Backend Projects (namely `backend-healthcheck`)
