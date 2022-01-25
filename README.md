# Django Project Structure
This is a template/project structure for developing django-based applications -
either strictly through the `django-rest-framework` or just `django`.

The project is meant to be easily clonable, and used as the starter template for
the next big thing your team develops.

First, we'll define the scope of today's discussion.

We're here to talk about a long-standing project structure - not best practices. We'll deal with those later.

However, a lot of these decisions we're based on some accepted best practices. I'll be listing all my reference material at the presentation.

Additionally, I will not be taking questions or discussions today. Instead I ask that everyone takes detailed notes, and raises issues in the GitHub repository, and offers their contributions there. While I understand this adds extra steps for suggestions, it also serves as a place to concretely discuss improvements and offer detailed suggestions and examples in written form instead of verbal assumptions.



## Debugging and Tooling
* Add Silk
* Add Django Debug Toolbar


## Coding Style:
* https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/

## Instructions:
* Should we add a note for when we add new imports?

# Design Principles
* Each application should be designed in a way to be pluggable - dragged and
dropped into any other project and it'll still work independently.

# Code Checking
* We'll use mypy for static type checking

# Code Formatting
* We'll use black as our auto-formatter

# Testing
* We'll use pytest for testing

Disclaimer: I don't have 10 years of experience, nor do I have access to people
with 10 years of experience. What I do have is good reference material - books,
conferences, and documentation. These people are smarter than me, they are better
developers and they have more experience - I'm somewhat collecting and presenting
what they do.


Mani na

# Starting
Defining the scope of our projects
We need a project structure that is;
- Homogeneous across strativ applications
- Can be used to build Django Rest APIs and also support Django Templates
- We're limiting ourselves strictly to Django because there are developer
expectations - for instance, if you're a Django developer, you'll expect the
project to have a settings.py, a manage.py, etc.

What this allows -
When anyone visits this project, they are provided with a high-level view of the
project. We've found that this allows us to work easily with other developers
and even non-developers.


Please observe the following:
➤ We like to place all our API components into a package within an app called api/.
That allows us to isolate our API components in a consistent location. If we were to
put it in the root of our app, then we would end up with a huge list of API-specific
modules in the general area of the app.
➤ Viewsets belong in their own module.
➤ We always place routers in urls.py. Either at the app or project level, routers belong
in urls.py.


REST Framework Decisions:
For projects with a lot of small, interconnecting apps, it can be hard to hunt
down where a particular API view lives. In contrast to placing all API code
within each relevant app, sometimes it makes more sense to build an app
specifically for the API. This is where all the serializers, renderers, and views
are placed. Therefore, the name of the app should reflect its API version (see
Section 17.3.7: Version Your API).

For example, we might place all our views, serializers, and other API
components in an app titled apiv4. The downside is the possibility for the API
app to become too large and disconnected from the apps that power it. Hence we
consider an alternative in the next subsection.


# Zen of Python
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Git Ignore

https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files

Git Ignore:
We're gonna follow ->
https://github.com/github/gitignore/blob/main/Python.gitignore

With or without the nuclear option.
https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore



## Tree
```
│   .gitignore
│   Dockerfile
│   entrypoint.sh
│   manage.py
│   nginx.conf
│   README.md
│
├───app
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   urls.py
│   │   utils.py
│   │   __init__.py
│   │
│   ├───api
│   │   │   __init__.py
│   │   │
│   │   ├───v1
│   │   │       serializers.py
│   │   │       tests.py
│   │   │       urls.py
│   │   │       views.py
│   │   │       viewsets.py
│   │   │       __init__.py
│   │   │
│   │   └───v2
│   │           serializers.py
│   │           tests.py
│   │           urls.py
│   │           views.py
│   │           viewsets.py
│   │           __init__.py
│   │
│   ├───management
│   │       commands.py
│   │       __init__.py
│   │
│   ├───migrations
│   │       __init__.py
│   │
│   └───templates
├───config
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───settings
│           base.py
│           development.py
│           local.py
│           local_template.py
│           production.py
│
├───core
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   └───migrations
│           __init__.py
│
├───docs
│       CHANGELOG.md
│       CONTRIBUTING.md
│       LOCAL_DEVELOPMENT.md
│       PRODUCTION_DEPLOYMENT.md
│       swagger.yaml
│
├───requirements
│       common.txt
│       development.txt
│       local.txt
│       production.txt
│
├───static
└───templates
```

## References
Two Scoops of Django by Daniel and Audrey Feldroy

Where to Write Business Logic:
* https://stackoverflow.com/questions/57387711/django-rest-framework-where-to-write-complex-logic-in-serializer-py-or-views-py

Django Best Practices:
* https://django-best-practices.readthedocs.io/en/latest/index.html

Reference:
* https://github.com/cookiecutter/cookiecutter-django


## TODO
* Add versioning for swagger documentation - https://editor.swagger.io/
