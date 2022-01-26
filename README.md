# Django Project Structure
This is a template/project structure for developing django-based applications -
either strictly through the `django-rest-framework` or just `django`.

The project is meant to be easily clonable, and used as the starter template for
the next big thing our team develops.

## Project Tree
```bash
.
├── apps
│   ├── app
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
│   └── second_app
│       ├── migrations
│       │   └── __init__.py
│       ├── templates
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── models.py
│       ├── service.py
│       ├── tests.py
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
### `apps`
* A mother-folder containing all apps for our project.
* An app can be a django template project, or an api


### `config`
* Contains project configuration files, including the primary URL file
* Contains settings split into `base`, `local`, `production` and `development`


### `deployments`
* Contains Docker and nginx specific files for deploying in different
environments


## References
- [Two Scoops of Django by Daniel and Audrey Feldroy](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [Django Best Practices](https://django-best-practices.readthedocs.io/en/latest/index.html)
- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- [HackSoft Django Style Guide](https://github.com/HackSoftware/Django-Styleguide)
- [Radoslav Georgiev - Django Structure for Scale and Longevity](https://www.youtube.com/watch?v=yG3ZdxBb1oo)
