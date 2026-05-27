# Intoduction to Web-App Back-End Development

This is my guide for web-app backend development, based on selected courses from:
- the [Meta Back-End Developer Professional Certificate](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/professional-certificates/meta-back-end-developer) specialization on Coursera
- and the [Backend Developer with Python](https://www.udacity.com/course/backend-developer-with-python--nd0044) nanodegree on Udacity.

From these specializations, I have selected the following topics/courses:

1. [Introduction to Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/introduction-to-back-end-development)
2. [Introduction to Databases for Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/intro-to-databases-back-end-development)
3. [Django Web Framework](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/django-web-framework?authProvider)
4. [APIs](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/apis)
5. [The Full Stack](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/the-full-stack?authProvider=deutschetelekom)
6. [SQL & Python Data Modeling for the Web](https://www.udacity.com/course/sql-and-data-modeling-for-the-web--cd0046)
7. [Software Architecture Patterns](https://www.udacity.com/course/software-architecture-patterns--cd14601)
8. [Identity and Access Management](https://www.udacity.com/course/identity-access-management--cd0039)

This module deals with the third topic/course: **Django Web Framework**.

- [Intoduction to Web-App Back-End Development](#intoduction-to-web-app-back-end-development)
  - [1. Introduction to Django](#1-introduction-to-django)
    - [Introduction](#introduction)
      - [What is Django?](#what-is-django)
      - [Setup](#setup)
      - [Additional Resources](#additional-resources)
    - [Projects and Apps](#projects-and-apps)
      - [Projects and Apps Overview](#projects-and-apps-overview)
      - [Project Structure](#project-structure)
        - [Django and the Python environment](#django-and-the-python-environment)
        - [What is a project?](#what-is-a-project)
        - [`manage.py`](#managepy)
        - [`startapp`](#startapp)
        - [`makemigrations`](#makemigrations)
        - [`migrate`](#migrate)
        - [`runserver`](#runserver)
        - [`shell`](#shell)
        - [Project package](#project-package)
        - [`settings.py`](#settingspy)
        - [`urls.py`](#urlspy)
        - [`asgi.py`](#asgipy)
        - [`wsgi.py`](#wsgipy)
        - [Critical settings](#critical-settings)
        - [`INSTALLED_APPS`](#installed_apps)
        - [`DATABASES`](#databases)
        - [`DEBUG`](#debug)
        - [`ALLOWED_HOSTS`](#allowed_hosts)
        - [`ROOT_URLCONF`](#root_urlconf)
        - [`STATIC_URL`](#static_url)
        - [Test the installation](#test-the-installation)
      - [Creating Our First Project](#creating-our-first-project)
      - [First Project Contents](#first-project-contents)
        - [`manage.py`](#managepy-1)
        - [`db.sqlite3`](#dbsqlite3)
        - [`chef_stable/asgi.py`](#chef_stableasgipy)
        - [`chef_stable/settings.py`](#chef_stablesettingspy)
        - [`chef_stable/urls.py`](#chef_stableurlspy)
        - [`chef_stable/wsgi.py`](#chef_stablewsgipy)
    - [Admin and Structures](#admin-and-structures)
    - [Web Frameworks and MVT](#web-frameworks-and-mvt)
  - [2. Views](#2-views)
    - [Views](#views)
    - [Requests and URLs](#requests-and-urls)
    - [Creating URLs and Views](#creating-urls-and-views)
  - [3. Models](#3-models)
    - [Models and Migrations](#models-and-migrations)
    - [Models and Forms](#models-and-forms)
    - [Admin](#admin)
    - [Database Configuration](#database-configuration)
  - [4. Templates](#4-templates)
    - [Templates](#templates)
    - [Working with Templates](#working-with-templates)
    - [Debugging and Testing](#debugging-and-testing)
  - [5. Summary and Assessment](#5-summary-and-assessment)


## 1. Introduction to Django

### Introduction

#### What is Django?

- Developers can choose how to build web applications.
  - They can build common features themselves.
  - They can use a web application framework.
    - A framework is a toolkit with common components for application development.
    - It lets teams focus on unique features instead of rebuilding common features.
      - Common features include:
        - user login,
        - authentication,
        - admin dashboards.
- Django is an open-source web development framework.
  - It is written in Python.
  - Current Django documentation describes it as high-level and focused on rapid development.
  - Current Django documentation emphasizes clean, pragmatic design.
  - Django was first created for a newspaper publisher web application.
    - This origin makes it strong for:
      - text-heavy projects,
      - media-heavy projects,
      - high-traffic projects.
  - Its open-source nature helped it:
    - grow quickly,
    - adapt to many web applications.
- Django integrates with many tools.
  - It integrates through Python libraries.
  - A successful web framework must be:
    - robust,
    - secure,
    - adaptable,
    - scalable.
  - Django supports these needs with:
    - templates,
    - libraries,
    - APIs (application programming interfaces).
- Django is used across many industries.
  - It is popular in:
    - publishing,
    - eCommerce,
    - health care,
    - finance,
    - transport,
    - travel,
    - social media.
  - It is used for:
    - machine learning,
    - artificial intelligence,
    - scalable web applications,
    - SaaS (Software as a Service) applications,
    - OTT (over-the-top) media platforms,
    - shopping,
    - event management,
    - news and publishing.
- Django separates application features well.
  - This helps organizations combine Django with other frameworks.
  - Developers can build a Django back end and connect it to a front end through an API.
  - Teams can choose front-end frameworks such as:
    - React,
    - React Native.
- Django supports powerful back-end features.
  - It supports:
    - email notifications,
    - data analysis tools,
    - admin dashboards,
    - online marketplace tools,
    - booking-system tools.
- Django can support machine learning applications.
  - Developers can expose machine learning algorithms through:
    - APIs,
    - RPCs (remote procedure calls),
    - WebSockets.
  - Django can handle many API endpoints.
    - Each endpoint can connect to several machine learning models.
  - Django supports fast model integration and deployment.
- Django is popular for scalable web applications.
  - Many applications start small and grow quickly.
  - Social media applications may need rapid growth in:
    - memory,
    - resources.
  - Instagram from Meta is given as an example.
  - Django is useful when the final user-base size is unknown.
  - Traffic management must be fast and efficient for scalability.
  - Django is popular for:
    - social media apps,
    - magazines,
    - blogs.
- Django is used for Software as a Service applications.
  - SaaS platforms may provide:
    - data storage,
    - app stores,
    - version control systems.
  - Django is popular for cloud storage applications.
  - Current Django documentation defines asynchronous views with `async def`.
  - Asynchronous views:
    - can run non-blocking operations,
    - perform best with ASGI (Asynchronous Server Gateway Interface),
    - help applications run services concurrently,
    - avoid waiting for each service in a queue.
  - Concurrent service handling can improve application performance.
- Django is used for OTT media platforms.
  - OTT platforms provide streaming services for:
    - audio,
    - video.
  - OTT platforms have grown in popularity.
  - Django is often used to support OTT needs.
- Django is not limited to these examples.
  - It is generally considered more suitable for large projects.
  - It provides good fault tolerance.
  - It is free because it is open source.
    - This can reduce company costs.
  - It is popular because it has:
    - ease of adaptation,
    - robustness,
    - a supportive open-source community,
    - comprehensive documentation,
    - security.
- Django helps developers avoid reinventing the wheel.
  - It helps teams use established tools and reduce rebuilding of common functionality.
  - This section presents Django as a favored framework for real-world web applications.

#### Setup

- Python & `venv`; I will use `uv`, following the setup in [`../README.md`](../README.md)
- Django as dependency in the `venv`.
- VSCode + Python extension + SQLite.viewer extension.

#### Additional Resources

- [Django Official Website](https://www.djangoproject.com/start/overview/)
- [Django Official Documentation](https://docs.djangoproject.com/en/4.1/)

### Projects and Apps

#### Projects and Apps Overview

- Website structure depends on complexity.
  - A basic website contains:
    - HTML (HyperText Markup Language) for page structure,
    - CSS (Cascading Style Sheets) for look and style,
    - JavaScript for client-side interaction.
  - A simple static website may only need:
    - CSS folders,
    - JavaScript folders,
    - image folders.
  - A project structure should make files easy to update.
- Dynamic web applications need more structure than static websites.
  - They may need to hold state.
  - They may need to access data.
  - They may need to store data.
  - A framework lets developers focus on project-specific functionality instead of repeated setup tasks.
- Django provides a structured way to build web applications.
  - It was created by developers who followed best practices.
  - It helps organize development around projects and apps.
  - It lets developers work from a predictable structure.
- Dynamic web applications usually involve several core concepts.
  - HTTP (HyperText Transfer Protocol) is used to get, send, and render web content.
  - Every web action is tied to an HTTP request.
  - Each request points to a URL (Uniform Resource Locator).
  - A web server gets the requested page and returns it through HTTP.
  - Django includes a Python development server.
    - It saves setup time.
    - It avoids manual server configuration during development.
  - The web is stateless.
    - It does not store information for future reference by itself.
  - A database stores and retrieves website data.
    - Form submissions often need to be saved.
    - Saved data can be retrieved and rendered later.
- A Django project represents the entire web application.
  - Django commands auto-generate the project structure.
  - The generated structure contains application-wide configuration and settings.
  - The project organizes Python files and folders.
  - This lets developers focus on code instead of configuration.
- A Django app is a submodule of a project.
  - It usually implements functionality for a specific purpose.
  - It can be self-contained.
  - It can be reused in multiple projects.
  - This supports the DRY (don't repeat yourself) principle.
    - Write functionality once.
    - Reuse it many times.
- A Django web application is a project that contains apps.
  - A social media application can be the project.
  - Its features can be separate apps, such as:
    - news feed,
    - comments,
    - friends list,
    - user page.
- Django can generate app files automatically.
  - The `startapp` command creates a self-contained app directory.
  - The generated directory contains associated app files.
  - The app lives inside the project structure.
- Django must know which apps belong to the project.
  - Apps must be added to the `INSTALLED_APPS` setting.
  - Django uses installed apps for configuration and introspection.
  - The application registry stores metadata for each installed app.
  - The metadata lives in an app config instance.
- Django apps can include several framework parts.
  - Common parts include:
    - models,
    - views,
    - templates,
    - template tags,
    - static files,
    - URLs,
    - middleware.
- App design can be subjective.
  - Developers spend a lot of time working with apps.
  - Apps contain the project's different parts.
  - Different developers may choose different app boundaries.
  - A good starting rule is to make each app feature-targeted.
  - An app should usually do one thing well.
- This course uses one project with one app.
  - The section introduces Django projects and apps.
  - It explains how they give developers a structure to work from.

![Django Project Structure](./assets/django_project.png)

![Django Project: Create](./assets/django_project_create.png)

![Django Apps](./assets/django_apps.png)

![Django Projects and Apps](./assets/django_projects_and_apps.png)

![Django Apps: Create](./assets/django_apps_create.png)

```bash
# Create a Django project.
django-admin startproject project_name

# Move into the generated project directory.
cd project_name

# Create an app inside the project.
python manage.py startapp app_name

# Run the local development server.
python manage.py runserver
```

#### Project Structure

##### Django and the Python environment

- Python recommends isolated environments for application dependencies.
  - A virtual environment keeps libraries separate for a specific application.
  - Python's standard library includes the `venv` module for this purpose.
- Installing Django adds the `django-admin` command-line utility.
  - The utility is installed in the system path for the active Python environment.
  - It is located in the environment's scripts folder.
- The `django-admin` utility performs Django administrative tasks.
  - It can create projects and apps.
  - It can run migrations to create database tables that match data models.
  - It can run the development server.

##### What is a project?

- A modular, extensible, and scalable web application needs a structure for its submodules.
- A Django project is a Python package.
  - It contains database configuration.
  - It contains settings used by Django apps.
  - It contains other Django-specific project settings.

Create a project with `django-admin startproject`:

```powershell
(djenv) C:\djenv> django-admin startproject demoproject
```

The `startproject` command uses Django's default project template. It creates this structure:

```text
C:\djenv\demoproject
|   manage.py
\---demoproject\
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

If you start Visual Studio Code in this folder, the file structure appears in its explorer.

![Django Installed Apps](./assets/django_installed_apps.png)

- The outer `demoproject` folder is created in the Python environment folder.
- It contains:
  - `manage.py`,
  - an inner `demoproject` folder.
- The inner folder contains project package files.

##### `manage.py`

- The `manage.py` script has the same role as `django-admin` for the current project.
- It is useful when working on a single project because it automatically uses that project's settings.
- If you have multiple projects, use `django-admin` and specify the settings explicitly.

General usage:

```bash
python manage.py <command>
```

##### `startapp`

- A Django project can contain one or more apps.
- An app is represented by a folder with a specific file structure.
- Use `startapp` to create an app.

```bash
python manage.py startapp <app_name>
```

You will explore the structure of an app later.

##### `makemigrations`

- Django manages database operations with the Object-Relational Mapping (ORM) technique.
- A migration records how the database table structure should match the data model declared in an app.
- Run this command whenever a new model is declared or an existing model changes.

```bash
python manage.py makemigrations
```

##### `migrate`

- The `migrate` command synchronizes the database state with the declared models and migrations.

```bash
python manage.py migrate
```

The console or terminal displays migration output when the command runs.

![Django Migrate](./assets/django_migrate.png)

##### `runserver`

- The `runserver` command starts Django's built-in development server.
- By default, it runs on the local machine at IP (Internet Protocol) address `127.0.0.1` and port `8000`.
- Do not use the development server in production.

```bash
python manage.py runserver
```

##### `shell`

- The `shell` command opens an interactive Python shell inside the project.
- It is useful for quick interactive operations.
- Django prefers IPython when it is installed.

```bash
python manage.py shell
```

##### Project package

The `django-admin startproject` command creates an outer folder and an inner package folder with the same name:

```bash
django-admin startproject demoproject
```

- The outer `demoproject` folder contains the project files.
- The inner `demoproject` folder is a Python package.
- Python recognizes a folder as a package when it contains `__init__.py`.
- The default project package also contains:
  - `settings.py`,
  - `urls.py`,
  - `asgi.py`,
  - `wsgi.py`.

##### `settings.py`

- Django stores project configuration in `settings.py`.
- The `django-admin` utility and `manage.py` script use these settings while performing administrative tasks.
- The `startproject` template assigns default values that can be changed later.

##### `urls.py`

- The `urls.py` file contains `urlpatterns`.
- Each browser request points to a URL (Uniform Resource Locator).
- Django matches the requested URL pattern and routes the request to the mapped view.
- The default `urls.py` maps the project's admin site.

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```

##### `asgi.py`

- The `asgi.py` file is used by servers that follow the ASGI (Asynchronous Server Gateway Interface) standard.
- ASGI-compatible servers can serve asynchronous Django applications.

##### `wsgi.py`

- The `wsgi.py` file is used by servers that follow the WSGI (Web Server Gateway Interface) standard.
- It is the entry point for WSGI-compatible servers that serve traditional Django applications.

##### Critical settings

The `settings.py` file defines attributes that influence how the Django application works.

##### `INSTALLED_APPS`

- `INSTALLED_APPS` is a list of strings.
- Each string identifies an app available to the project.
- The `startproject` template includes several Django apps by default.
- Add a new app to this list after creating it.

Create an app:

```bash
python manage.py startapp demoapp
```

Register the app in `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    "demoapp",
]
```

##### `DATABASES`

- `DATABASES` is a dictionary.
- It defines one or more database connections for the current Django application.
- Django uses SQLite by default.
- The default SQLite database file is usually `db.sqlite3` in the project root.

Example SQLite configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

You can use another database instead of SQLite. Example MySQL configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "database_name",
        "USER": "database_user",
        "PASSWORD": "database_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

- MySQL commonly uses port `3306`.
- Django's development server commonly uses port `8000`.

##### `DEBUG`

- `DEBUG = True` enables debug mode during development.
- Debug mode lets the development server pick up code changes.
- It lets output refresh without restarting the server manually.
- Disable debug mode in production.

```python
DEBUG = True
```

##### `ALLOWED_HOSTS`

- `ALLOWED_HOSTS` is a list of strings.
- Each string represents a host or domain where the Django site can be served.
- It is empty by default in a new project.
- Add a host when the site must be externally visible.

```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

##### `ROOT_URLCONF`

- `ROOT_URLCONF` points to the module that contains the project's URL patterns.
- In this project, it points to the project package's `urls.py` file.

```python
ROOT_URLCONF = "demoproject.urls"
```

##### `STATIC_URL`

- `STATIC_URL` points to the URL prefix used for static files.
- Static files include:
  - JavaScript code,
  - CSS files,
  - images.
- It is usually set to `"static/"`.

```python
STATIC_URL = "static/"
```

##### Test the installation

After creating the project, verify it from the project's parent folder.

```bash
python manage.py runserver
```

- The development server starts at `http://127.0.0.1:8000/`.
- Open that address in a browser.
- If the Django welcome page appears, the project was created successfully.

In this reading, you learned how to create a Django project, inspect its file structure, and verify the installation.

#### Creating Our First Project

- This section builds on Django projects, apps, and core project files.
  - It shows how to create a first Django project.
  - It uses the terminal and Visual Studio Code (VS Code).
  - It introduces common CLI (command-line interface) commands.
    - Commands create the project.
    - Commands launch the development server.
- A virtual environment is recommended for Django projects.
  - It isolates project dependencies from other Python or Django projects.
  - It prevents package-version conflicts.
  - It keeps the interpreter, libraries, and scripts tied to one project.
  - It can be omitted, but this is not recommended.
- Django includes an integrated development server.
  - The server supports local development.
  - It lets the application handle a request-response relationship with a client.
  - It is a development tool, not a production server.
- Creating a Django project follows a sequence.
  - Create a project directory.
  - Create and activate a virtual environment.
  - Install Django.
  - Verify the Django installation.
  - Create the Django project.
  - Run the Django development server.
- A Django project is an organizational unit.
  - It contains settings.
  - It contains database information.
  - It can be stored anywhere on the development computer.
  - Best practice is to keep it in a subfolder with other Django applications.
- The terminal workflow creates the project workspace.
  - Open a new terminal in VS Code.
  - Create a directory with the make-directory command.
  - Move into that directory with the change-directory command.
  - Create a virtual environment with Python's `venv` module.
  - Activate the virtual environment.
  - The activated environment appears in the terminal prompt.
- Django is installed inside the activated virtual environment.
  - Current Django documentation recommends installing with `python -m pip`.
  - Current Django documentation verifies installation with `python -m django --version`.
  - The original section mentioned Django version 4.1, but the installed version depends on the current environment.
- A Django project is created with Django's command-line tools.
  - Use `django-admin startproject`.
  - The example project name is `chef_stable`.
  - Django creates the project directory and supporting Django-specific files.
- The generated `manage.py` file is important.
  - It is created automatically with the project.
  - It works like `django-admin`.
  - It uses the current project's settings.
  - It is commonly used to run project-specific commands.
- The development server is launched with `manage.py`.
  - Running the server generates a local URL.
  - On macOS, the URL can usually be clicked from the terminal.
  - On Windows, the URL may need to be copied into the browser.
  - Press `Ctrl+C` in the terminal to stop the server.
- Virtual environments and development servers are larger topics.
  - The course will cover them later.
  - This section focuses on creating the first Django project with terminal, VS Code, and Django command-line tools.

This first project is in [`lab/01-django-demo`](./lab/01-django-demo).

```bash
# Create a project directory.
cd .../backend_django_guide
cd 03_Django/lab
mkdir 01-django-demo

# Move into the project directory.
cd 01-django-demo

# Create a virtual environment
python -m venv tutorial-env
# Activate the virtual environment on macOS/Linux.
source tutorial-env/bin/activate
# Activate the virtual environment on Windows PowerShell.
tutorial-env\Scripts\Activate.ps1
# Install Django in the activated virtual environment.
python -m pip install Django

# Alternatively, I used the uv env created in the root of this repository.
cd .../backend_django_guide
uv sync
.venv\Scripts\Activate.ps1

# Verify the installed Django version.
python -m django --version

# Create the Django project.
cd .../backend_django_guide/03_Django/lab/01-django-demo
django-admin startproject chef_stable
# This creates an outer and inner chef_stable folder with the project files.
# 01-django-demo/chef_stable
#   manage.py
#   chef_stable/
#     asgi.py
#     settings.py
#     urls.py
#     wsgi.py
#     __init__.py

# Move into the generated project directory.
cd chef_stable

# Run the Django development server (but first run once migrate to create the database file).
python manage.py migrate
python manage.py runserver  # It defaults to 127.0.0.1:8000, but maybe the port is taken
# In that case, specify the port explicitly:
python manage.py runserver 127.0.0.1:8001
# Stop the development server with Ctrl+C in the terminal.
```

![Django Default Web Page](./assets/django_default_web.png)

#### First Project Contents

This first project is in [`lab/01-django-demo`](./lab/01-django-demo).

Its contents include these files:

- `manage.py`
- `db.sqlite3` (created after running `migrate`)
- `chef_stable/asgi.py`
- `chef_stable/settings.py`
- `chef_stable/urls.py`
- `chef_stable/wsgi.py`

In the following, the content with comments of each file is shown and explained.

##### `manage.py`

Location: [`lab/01-django-demo/chef_stable/manage.py`](./lab/01-django-demo/chef_stable/manage.py)

```python
#!/usr/bin/env python
# This file is Django's command-line entry point for this project.
# You use it for commands such as:
# - python manage.py runserver
# - python manage.py migrate
# - python manage.py createsuperuser

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Tell Django which settings module belongs to this project.
    # The value uses Python's dotted import path:
    # package_name.module_name
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chef_stable.settings")

    try:
        # Import Django's command runner.
        # This function reads sys.argv and dispatches the requested command.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django cannot be imported, the most common causes are:
        # - Django is not installed.
        # - The virtual environment is not active.
        # - The Python path is not configured correctly.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command passed in the terminal.
    # For example, with "python manage.py runserver",
    # sys.argv contains the "runserver" command.
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    # Only run main() when this file is executed directly.
    main()
```

##### `db.sqlite3`

Location: `lab/01-django-demo/chef_stable/db.sqlite3`

`db.sqlite3` is not shown as a code block because it is a binary SQLite database file, not a plain-text Python file.

It is created after running:

```shell
python manage.py migrate
```

At this stage, it stores the database tables for Django's built-in apps, including admin, authentication, sessions, and content types. The database location is configured in `settings.py`:

```python
DATABASES = {
    "default": {
        # Use SQLite for the first local development project.
        "ENGINE": "django.db.backends.sqlite3",

        # Store the database file at BASE_DIR / "db.sqlite3".
        # BASE_DIR points to the folder that contains manage.py.
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

##### `chef_stable/asgi.py`

Location: [`lab/01-django-demo/chef_stable/chef_stable/asgi.py`](./lab/01-django-demo/chef_stable/chef_stable/asgi.py)

```python
"""
ASGI config for chef_stable project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Point Django to this project's settings before the application starts.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chef_stable.settings")

# Create the ASGI application object.
# ASGI is commonly used for asynchronous-capable servers and protocols.
application = get_asgi_application()
```

##### `chef_stable/settings.py`

Location: [`lab/01-django-demo/chef_stable/chef_stable/settings.py`](./lab/01-django-demo/chef_stable/chef_stable/settings.py)

```python
"""
Django settings for chef_stable project.

Generated by 'django-admin startproject' using Django 5.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is the directory that contains manage.py.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Django uses SECRET_KEY for cryptographic signing.
# In real production projects, store this outside the source code.
SECRET_KEY = "django-insecure-1fc)%s0_vdfv#0raz@b7-)=c+*xrh-alg7apld&$6pqg)vr-ya"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG=True shows detailed error pages, which are useful during learning.
DEBUG = True

# A list of host/domain names this Django site can serve.
# Empty is acceptable for the local development server.
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Enables the built-in Django admin site.
    "django.contrib.admin",

    # Provides users, groups, permissions, and authentication.
    "django.contrib.auth",

    # Tracks content types for installed models.
    "django.contrib.contenttypes",

    # Enables database-backed sessions.
    "django.contrib.sessions",

    # Enables temporary one-time messages, often used after form actions.
    "django.contrib.messages",

    # Enables serving and collecting static files such as CSS and JavaScript.
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    # Adds several security protections to requests and responses.
    "django.middleware.security.SecurityMiddleware",

    # Connects browser sessions to Django's session framework.
    "django.contrib.sessions.middleware.SessionMiddleware",

    # Handles common request/response behavior such as URL normalization.
    "django.middleware.common.CommonMiddleware",

    # Protects forms against cross-site request forgery attacks.
    "django.middleware.csrf.CsrfViewMiddleware",

    # Associates requests with logged-in users.
    "django.contrib.auth.middleware.AuthenticationMiddleware",

    # Enables the messages framework for request/response cycles.
    "django.contrib.messages.middleware.MessageMiddleware",

    # Helps prevent clickjacking by controlling iframe embedding.
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# The root URL configuration module.
# Django starts URL matching in chef_stable/urls.py.
ROOT_URLCONF = "chef_stable.urls"

TEMPLATES = [
    {
        # Use Django's built-in template engine.
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # Project-level template directories can be listed here.
        "DIRS": [],

        # Allow Django to find templates inside installed apps.
        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                # Adds the request object to template contexts.
                "django.template.context_processors.request",

                # Adds user and permission data to template contexts.
                "django.contrib.auth.context_processors.auth",

                # Adds messages to template contexts.
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# The WSGI application path for deployment servers.
WSGI_APPLICATION = "chef_stable.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        # Use SQLite, a small file-based database, for local development.
        "ENGINE": "django.db.backends.sqlite3",

        # Store the database file in the same directory as manage.py.
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        # Prevent passwords that are too similar to user information.
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        # Enforce a minimum password length.
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        # Reject commonly used passwords.
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        # Reject passwords that are entirely numeric.
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

# Default language for this project.
LANGUAGE_CODE = "en-us"

# Default time zone for date/time handling.
TIME_ZONE = "UTC"

# Enable Django's translation system.
USE_I18N = True

# Store datetimes as time-zone-aware values.
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# URL prefix used when referencing static files.
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# Use 64-bit integer primary keys for models by default.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

##### `chef_stable/urls.py`

Location: [`lab/01-django-demo/chef_stable/chef_stable/urls.py`](./lab/01-django-demo/chef_stable/chef_stable/urls.py)

```python
"""
URL configuration for chef_stable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

# urlpatterns is the main list of URL patterns for the project.
# Django checks these patterns from top to bottom.
urlpatterns = [
    # Send requests for /admin/ to Django's built-in admin site.
    path("admin/", admin.site.urls),
]
```

##### `chef_stable/wsgi.py`

Location: [`lab/01-django-demo/chef_stable/chef_stable/wsgi.py`](./lab/01-django-demo/chef_stable/chef_stable/wsgi.py)

```python
"""
WSGI config for chef_stable project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Point Django to this project's settings before the application starts.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chef_stable.settings")

# Create the WSGI application object.
# WSGI is the traditional Python standard used by many production web servers.
application = get_wsgi_application()
```


### Admin and Structures

### Web Frameworks and MVT

## 2. Views

### Views

### Requests and URLs

### Creating URLs and Views

## 3. Models

### Models and Migrations

### Models and Forms

### Admin

### Database Configuration

## 4. Templates

### Templates

### Working with Templates

### Debugging and Testing

## 5. Summary and Assessment
