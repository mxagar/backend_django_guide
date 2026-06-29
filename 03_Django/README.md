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
6. [Flask SQLAlchemy Data Modelling](https://www.udacity.com/course/sql-and-data-modeling-for-the-web--cd0046)
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
      - [Django Admin and manage.py Commands](#django-admin-and-managepy-commands)
        - [`django-admin`](#django-admin)
        - [`manage.py`](#managepy-2)
        - [Choosing between `django-admin` and `manage.py`](#choosing-between-django-admin-and-managepy)
        - [Running the development server](#running-the-development-server)
      - [App Structures](#app-structures)
        - [Creating an app](#creating-an-app)
        - [`views.py`](#viewspy)
        - [App-level `urls.py`](#app-level-urlspy)
        - [Project-level `urls.py`](#project-level-urlspy)
        - [`models.py`](#modelspy)
        - [`tests.py`](#testspy)
        - [Registering the app in `settings.py`](#registering-the-app-in-settingspy)
        - [Testing the app route](#testing-the-app-route)
        - [Other app files](#other-app-files)
        - [Application to chef\_stable](#application-to-chef_stable)
      - [Re-Usability of Apps](#re-usability-of-apps)
        - [Ways to share a reusable app](#ways-to-share-a-reusable-app)
        - [What makes an app reusable?](#what-makes-an-app-reusable)
      - [Summary: Create a Django Project and App](#summary-create-a-django-project-and-app)
    - [Web Frameworks and MVT](#web-frameworks-and-mvt)
      - [What is a Web Framework?](#what-is-a-web-framework)
      - [Model-View-Template (MVT) Overview](#model-view-template-mvt-overview)
        - [Web framework](#web-framework)
        - [MVC architecture](#mvc-architecture)
        - [MVT architecture](#mvt-architecture)
        - [URL dispatcher](#url-dispatcher)
        - [View](#view)
        - [Model](#model)
        - [Template](#template)
      - [MVT Example](#mvt-example)
        - [1. Create the project and app](#1-create-the-project-and-app)
        - [2. Connect the URLs](#2-connect-the-urls)
        - [3. Example with only a view](#3-example-with-only-a-view)
        - [4. Example with model and view](#4-example-with-model-and-view)
        - [5. Example with model, view, and template](#5-example-with-model-view-and-template)
        - [What the example shows](#what-the-example-shows)
      - [Additional Resources](#additional-resources-1)
  - [2. Views](#2-views)
    - [Views](#views)
      - [Introduction to Views](#introduction-to-views)
      - [Creating Views and Mapping to URLs](#creating-views-and-mapping-to-urls)
      - [View Logic](#view-logic)
        - [What a view does](#what-a-view-does)
        - [GET and POST methods](#get-and-post-methods)
        - [Rendering a template](#rendering-a-template)
        - [Function-based views](#function-based-views)
        - [Class-based views](#class-based-views)
        - [Generic views](#generic-views)
      - [Creating Views and View Logic](#creating-views-and-view-logic)
      - [Exercise: Create Views and Map to URLs](#exercise-create-views-and-map-to-urls)
    - [Requests and URLs](#requests-and-urls)
      - [HTTP Requests](#http-requests)
      - [Request and Response Objects](#request-and-response-objects)
        - [`HttpRequest` object](#httprequest-object)
        - [`HttpResponse` object](#httpresponse-object)
      - [Creating Requests and Responses](#creating-requests-and-responses)
      - [Understanding URLs](#understanding-urls)
      - [Parameters](#parameters)
        - [Path parameters](#path-parameters)
        - [Path converters](#path-converters)
        - [Query parameters](#query-parameters)
        - [Body parameters](#body-parameters)
        - [`csrf_token`](#csrf_token)
      - [Mapping URLs with Parameters](#mapping-urls-with-parameters)
      - [Exercise: Mapping URLs with Parameters](#exercise-mapping-urls-with-parameters)
      - [Additional Resources](#additional-resources-2)
    - [Creating URLs and Views](#creating-urls-and-views)
      - [Regular Expressions in URLs](#regular-expressions-in-urls)
      - [URL Namespacing and Views](#url-namespacing-and-views)
        - [Named URLs](#named-urls)
        - [`reverse()`](#reverse)
        - [Application namespace](#application-namespace)
        - [Instance namespace](#instance-namespace)
        - [Using namespaces in views](#using-namespaces-in-views)
        - [Using namespaces in templates](#using-namespaces-in-templates)
      - [Exercise: Creating URLs and Mapping to Views](#exercise-creating-urls-and-mapping-to-views)
      - [Error Handling](#error-handling)
      - [Handling Errors in Views](#handling-errors-in-views)
      - [Demo: Handling Errors in Views](#demo-handling-errors-in-views)
      - [Class-based Views](#class-based-views-1)
  - [3. Models](#3-models)
    - [Models and Migrations](#models-and-migrations)
      - [Models](#models)
      - [Model Relationships](#model-relationships)
      - [Creating Models](#creating-models)
      - [Migrations](#migrations)
      - [Note about Database Connection](#note-about-database-connection)
      - [How to Use Migrations](#how-to-use-migrations)
      - [Excurs: Registering Models in admin.py](#excurs-registering-models-in-adminpy)
      - [Example: Working with Migrations](#example-working-with-migrations)
      - [A History of Changes](#a-history-of-changes)
      - [Excurs: What are Database Indices?](#excurs-what-are-database-indices)
      - [Exercise: Models and Migrations](#exercise-models-and-migrations)
      - [Models and Foreign Keys](#models-and-foreign-keys)
      - [Exercise: Models and Foreign Keys](#exercise-models-and-foreign-keys)
      - [ORM: Object Relationship Mapping](#orm-object-relationship-mapping)
        - [What Is ORM?](#what-is-orm)
        - [Django Models And ORM](#django-models-and-orm)
        - [QuerySet Example](#queryset-example)
        - [Open The Django Shell](#open-the-django-shell)
        - [Create A Model Object With `save()`](#create-a-model-object-with-save)
        - [Add A Model Object With `objects.create()`](#add-a-model-object-with-objectscreate)
        - [Create Related `Vehicle` Objects](#create-related-vehicle-objects)
        - [Fetch Model Objects](#fetch-model-objects)
        - [Filter Model Objects](#filter-model-objects)
        - [Access Related Objects](#access-related-objects)
        - [Update A Model Object](#update-a-model-object)
        - [Delete A Model Object](#delete-a-model-object)
      - [Using ORM](#using-orm)
      - [Additional Resources](#additional-resources-3)
    - [Models and Forms](#models-and-forms)
      - [Forms](#forms)
      - [Django Forms](#django-forms)
      - [Django Fields](#django-fields)
        - [Models And Database Tables](#models-and-database-tables)
        - [Table Names](#table-names)
        - [Model Fields And ModelForms](#model-fields-and-modelforms)
        - [Field Properties](#field-properties)
        - [Field Types](#field-types)
        - [Relationship Fields](#relationship-fields)
        - [`ForeignKey`](#foreignkey)
        - [`on_delete=models.CASCADE`](#on_deletemodelscascade)
        - [`on_delete=models.PROTECT`](#on_deletemodelsprotect)
        - [`on_delete=models.RESTRICT`](#on_deletemodelsrestrict)
        - [`OneToOneField`](#onetoonefield)
        - [`ManyToManyField`](#manytomanyfield)
      - [Form API](#form-api)
        - [HTML Form](#html-form)
        - [Django Form](#django-form)
        - [Django Form Fields](#django-form-fields)
        - [Rendering A Form Object In The Shell](#rendering-a-form-object-in-the-shell)
        - [Form Template](#form-template)
        - [Form Rendering Variations](#form-rendering-variations)
        - [Reading Form Contents](#reading-form-contents)
      - [Creating Forms](#creating-forms)
      - [Model Form](#model-form)
      - [Exercise: Working with Forms](#exercise-working-with-forms)
      - [Additional Resources](#additional-resources-4)
    - [Admin](#admin)
      - [Django Admin](#django-admin-1)
      - [Managing Users in Django Admin](#managing-users-in-django-admin)
        - [Superuser and Permissions](#superuser-and-permissions)
        - [Security Risks with the Default User Admin](#security-risks-with-the-default-user-admin)
        - [Customizing the User Admin](#customizing-the-user-admin)
        - [Making Fields Read-Only](#making-fields-read-only)
        - [Restricting a Field to Superusers Only](#restricting-a-field-to-superusers-only)
        - [Registering and Customizing a Custom Model](#registering-and-customizing-a-custom-model)
        - [Customizing the Model List Display](#customizing-the-model-list-display)
      - [Adding Groups and Users](#adding-groups-and-users)
      - [Permissions](#permissions)
      - [Enforcing Permissions](#enforcing-permissions)
        - [Model Permissions in the Admin Interface](#model-permissions-in-the-admin-interface)
        - [Enforcing Permissions at the View Level](#enforcing-permissions-at-the-view-level)
        - [Enforcing Permissions in Templates](#enforcing-permissions-in-templates)
        - [Enforcing Permissions in URL Patterns](#enforcing-permissions-in-url-patterns)
      - [Users and Permissions](#users-and-permissions)
      - [Exercise: Using Django Admin](#exercise-using-django-admin)
      - [Additional Resources](#additional-resources-5)
    - [Database Configuration](#database-configuration)
      - [Database Options](#database-options)
      - [Configuring MySQL Connection](#configuring-mysql-connection)
        - [Why MySQL over SQLite](#why-mysql-over-sqlite)
        - [Install MySQL Server](#install-mysql-server)
        - [Install the mysqlclient Driver](#install-the-mysqlclient-driver)
        - [Create Project](#create-project)
        - [Configure Django to Use MySQL](#configure-django-to-use-mysql)
        - [Apply Migrations](#apply-migrations)
        - [View MySQL Data in VS Code](#view-mysql-data-in-vs-code)
      - [Setting Up a MySQL Connection](#setting-up-a-mysql-connection)
        - [Install MySQL on macOS](#install-mysql-on-macos)
        - [Create a Dedicated Database User](#create-a-dedicated-database-user)
        - [Run makemigrations Before migrate](#run-makemigrations-before-migrate)
      - [Extra: Configuring PostgreSQL Connection](#extra-configuring-postgresql-connection)
        - [Install PostgreSQL](#install-postgresql)
          - [Windows](#windows)
          - [macOS](#macos)
          - [Linux (Ubuntu / Debian)](#linux-ubuntu--debian)
        - [Verify the Installation](#verify-the-installation)
        - [Create a Database and User](#create-a-database-and-user)
        - [Install the Python Driver](#install-the-python-driver)
        - [Configure Django to Use PostgreSQL](#configure-django-to-use-postgresql)
        - [Apply Migrations](#apply-migrations-1)
        - [View PostgreSQL Data in VS Code](#view-postgresql-data-in-vs-code)
      - [Exercise: Connecting to a Database](#exercise-connecting-to-a-database)
      - [Additional Resources](#additional-resources-6)
  - [4. Templates](#4-templates)
    - [Templates](#templates)
      - [Templates](#templates-1)
        - [Django Template Engine and DTL](#django-template-engine-and-dtl)
        - [Template Engine Configuration](#template-engine-configuration)
        - [Template Inheritance](#template-inheritance)
      - [Template Examples](#template-examples)
        - [HTML Response](#html-response)
        - [Rendering a Template](#rendering-a-template-1)
        - [Variable Tag](#variable-tag)
        - [If and For Tags](#if-and-for-tags)
        - [Filters](#filters)
        - [Built-in Filter Reference](#built-in-filter-reference)
        - [Custom Filters](#custom-filters)
      - [Creating Templates](#creating-templates)
      - [Exercise: Creating Templates](#exercise-creating-templates)
    - [Working with Templates](#working-with-templates)
      - [Working with Template Language](#working-with-template-language)
        - [Variables](#variables)
        - [Tags](#tags)
        - [Filters](#filters-1)
        - [Comments](#comments)
      - [Template Language and Variable Interpolation](#template-language-and-variable-interpolation)
        - [Template Engine Overview](#template-engine-overview)
        - [Variable Interpolation via `render()`](#variable-interpolation-via-render)
        - [`for` Loop Extras](#for-loop-extras)
        - [Additional Tags](#additional-tags)
        - [Additional Filters](#additional-filters)
      - [Mapping Model Objects to a Template](#mapping-model-objects-to-a-template)
      - [Exercise: Creating Dynamic Templates](#exercise-creating-dynamic-templates)
      - [Template Inheritance](#template-inheritance-1)
      - [More on Template Inheritance](#more-on-template-inheritance)
        - [Page Layout and the `{% block %}` Tag](#page-layout-and-the--block--tag)
        - [Building `base.html`](#building-basehtml)
        - [Adding Views and URL Patterns](#adding-views-and-url-patterns)
        - [Writing Child Templates](#writing-child-templates)
        - [Serving Static Files](#serving-static-files)
      - [Working with Template Inheritance](#working-with-template-inheritance)
      - [Exercise: Working with Templates](#exercise-working-with-templates)
    - [Debugging and Testing](#debugging-and-testing)
      - [Debugging Django Applications](#debugging-django-applications)
      - [Testing in Django](#testing-in-django)
      - [Sub-Classing Generic Views](#sub-classing-generic-views)
        - [Function-Based vs Class-Based Views](#function-based-vs-class-based-views)
        - [Generic Views for CRUD Operations](#generic-views-for-crud-operations)
        - [CreateView](#createview)
        - [ListView](#listview)
        - [DetailView](#detailview)
        - [UpdateView](#updateview)
        - [DeleteView](#deleteview)
      - [Additional Resources](#additional-resources-7)
  - [5. Summary and Project](#5-summary-and-project)
    - [Project Goals](#project-goals)
      - [Purpose of the Assessments](#purpose-of-the-assessments)
      - [Graded Quiz](#graded-quiz)
      - [Little Lemon Django Project](#little-lemon-django-project)
    - [Project](#project)
      - [Solution](#solution)
        - [`restaurant/models.py`](#restaurantmodelspy)
        - [`restaurant/admin.py`](#restaurantadminpy)
        - [`restaurant/views.py`](#restaurantviewspy)
        - [`restaurant/urls.py`](#restauranturlspy)
        - [`restaurant/templates/menu.html`](#restauranttemplatesmenuhtml)
        - [`restaurant/templates/menu_item.html`](#restauranttemplatesmenu_itemhtml)
        - [`restaurant/templates/partials/_footer.html`](#restauranttemplatespartials_footerhtml)
        - [`restaurant/templates/base.html` -- footer include](#restauranttemplatesbasehtml----footer-include)
        - [Shell Commands and Adding Menu Items](#shell-commands-and-adding-menu-items)
  - [Extra: Authentication and Authorization](#extra-authentication-and-authorization)
    - [Setup](#setup-1)
    - [The User Model](#the-user-model)
    - [Authentication: `authenticate()`, `login()`, `logout()`](#authentication-authenticate-login-logout)
    - [Restricting Access to Views](#restricting-access-to-views)
      - [Class-Based Views](#class-based-views-2)
      - [Custom Test with `@user_passes_test`](#custom-test-with-user_passes_test)
    - [Permissions](#permissions-1)
      - [`@permission_required` Decorator](#permission_required-decorator)
      - [Custom Permissions](#custom-permissions)
    - [Groups](#groups)
    - [Built-in Auth Views and URLs](#built-in-auth-views-and-urls)
    - [Built-in Auth Forms](#built-in-auth-forms)
    - [Password Management](#password-management)
    - [Authentication in Templates](#authentication-in-templates)
    - [Authentication Backends](#authentication-backends)
    - [Password Strength Measurement](#password-strength-measurement)
  - [Extra: Security](#extra-security)
    - [OWASP Top 10 and Django Coverage](#owasp-top-10-and-django-coverage)
    - [Cross-Site Scripting (XSS)](#cross-site-scripting-xss)
    - [Cross-Site Request Forgery (CSRF)](#cross-site-request-forgery-csrf)
    - [SQL Injection](#sql-injection)
    - [Clickjacking (`X-Frame-Options`)](#clickjacking-x-frame-options)
    - [HTTPS and `SecurityMiddleware`](#https-and-securitymiddleware)
    - [Host Header Validation](#host-header-validation)
    - [Session Security](#session-security)
    - [Secret Key](#secret-key)
    - [File Upload Security](#file-upload-security)
    - [`check --deploy`](#check---deploy)
  - [Extra: Caching](#extra-caching)
    - [Cache Backends](#cache-backends)
    - [Multiple Caches](#multiple-caches)
    - [Per-Site Caching (Middleware)](#per-site-caching-middleware)
    - [Per-View Caching (`@cache_page`)](#per-view-caching-cache_page)
    - [Template Fragment Caching](#template-fragment-caching)
    - [Low-Level Cache API](#low-level-cache-api)
    - [Cache Versioning](#cache-versioning)
    - [Cache Control and Vary Headers](#cache-control-and-vary-headers)
    - [Cache Invalidation](#cache-invalidation)
  - [Extra: Logging](#extra-logging)
    - [The Four Components](#the-four-components)
    - [Log Levels](#log-levels)
    - [Configuring `LOGGING` in `settings.py`](#configuring-logging-in-settingspy)
    - [Django's Built-in Loggers](#djangos-built-in-loggers)
    - [Handlers](#handlers)
    - [Filters](#filters-2)
    - [Formatters](#formatters)
    - [Logging in Your Own Code](#logging-in-your-own-code)
    - [Context Variables with `LoggerAdapter`](#context-variables-with-loggeradapter)
    - [Security Considerations](#security-considerations)
  - [Extra: Emails](#extra-emails)
    - [Key Settings](#key-settings)
    - [`send_mail()` -- Quick One-Shot](#send_mail----quick-one-shot)
    - [`send_mass_mail()` -- Efficient Batch Sending](#send_mass_mail----efficient-batch-sending)
    - [`EmailMessage` -- Full Control](#emailmessage----full-control)
    - [`EmailMultiAlternatives` -- HTML + Plain Text](#emailmultialternatives----html--plain-text)
    - [Template-Based Emails](#template-based-emails)
    - [Shared Connections](#shared-connections)
    - [Admin \& Manager Shortcuts](#admin--manager-shortcuts)
    - [Email Backends](#email-backends)
    - [Testing Emails](#testing-emails)
    - [Header Injection Prevention](#header-injection-prevention)
    - [Custom Backend](#custom-backend)
  - [Extra: Tasks](#extra-tasks)
    - [Architecture](#architecture)
    - [Defining Tasks](#defining-tasks)
    - [Task Decorator Parameters](#task-decorator-parameters)
    - [Backends \& `TASKS` Setting](#backends--tasks-setting)
    - [Enqueueing Tasks](#enqueueing-tasks)
    - [Transaction Safety](#transaction-safety)
    - [Task Results](#task-results)
    - [Workers](#workers)
    - [Serialization Constraints](#serialization-constraints)
    - [Django Tasks vs Celery](#django-tasks-vs-celery)
    - [Redis Backend (`django-tasks-rq`)](#redis-backend-django-tasks-rq)
      - [Running Redis -- Same Machine vs Separate Machine](#running-redis----same-machine-vs-separate-machine)
      - [Option A -- Redis directly on the machine](#option-a----redis-directly-on-the-machine)
      - [Option B -- Docker Compose (recommended for dev and single-server prod)](#option-b----docker-compose-recommended-for-dev-and-single-server-prod)


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
python manage.py runserver 8080
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
python manage.py runserver 8080
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

#### Django Admin and manage.py Commands

- Django provides command-line tools for common project administration tasks.
  - These tasks include:
    - creating a project,
    - creating apps,
    - running the development server,
    - managing database migrations,
    - opening an interactive Django shell.
- The two main command-line entry points are:
  - `django-admin`,
  - `manage.py`.

##### `django-admin`

- `django-admin` is Django's general command-line utility.
- It is installed when Django is installed in the Python environment.
- It should be available from the terminal when:
  - the virtual environment is activated,
  - Django is installed in that environment.
- It is useful for commands that do not yet belong to a specific project.
  - The most common example is creating a new project.

```bash
django-admin startproject <project_name>
```

- This creates:
  - a project directory,
  - a `manage.py` file,
  - an inner project package that contains files such as:
    - `settings.py`,
    - `urls.py`,
    - `asgi.py`,
    - `wsgi.py`.
- If only the project name is given, Django creates a directory with that project name.
- If a destination is provided, Django creates the project files in that destination.
- A common workflow is to use `.` as the destination.
  - This means "use the current directory".
  - It avoids creating an extra outer folder with the same name as the project.

```bash
django-admin startproject <project_name> .
```

##### `manage.py`

- `manage.py` is created automatically inside each Django project.
- It is a project-specific wrapper around Django's command-line tools.
- It sets the `DJANGO_SETTINGS_MODULE` environment variable for the project.
  - This tells Django which `settings.py` file to use.
- For day-to-day work inside a single project, developers usually use `manage.py`.

General usage:

```bash
python manage.py <command>
```

Common commands:

```bash
python manage.py startapp <app_name>
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8080
python manage.py shell
```

##### Choosing between `django-admin` and `manage.py`

- Use `django-admin` when:
  - creating a new project,
  - working before a `manage.py` file exists,
  - explicitly switching between different settings files.
- Use `manage.py` when:
  - working inside an existing project,
  - running commands that should use that project's settings automatically.
- Most commands can be run with either tool.
  - The main difference is that `manage.py` already knows the current project's settings.

##### Running the development server

- The `runserver` command starts Django's lightweight development server.
- By default, it runs at:
  - IP address: `127.0.0.1`,
  - port: `8000`.

```bash
python manage.py runserver
```

- You can provide a different port:

```bash
python manage.py runserver 8080
```

- You can also provide an IP address and port:

```bash
python manage.py runserver 127.0.0.1:8080
```

- The development server is useful for local development and testing.
- It should not be used in production.
  - It has not been designed for production security or performance.
- The development server automatically reloads when Python code changes.
  - Some changes, such as adding new files, may require manually restarting the server.

#### App Structures

- A Django project is the complete web application.
- A Django app is a smaller submodule inside the project.
  - Each app usually focuses on one area of functionality.
  - Apps can communicate with each other inside the same project.
  - Apps can also be reused across different Django projects.

For example, a trading organization website could use separate apps for:

- customer data,
- suppliers,
- stock management.

In this course, examples usually use one app inside one project. In real projects, Django often works as a multi-app framework.

##### Creating an app

- `django-admin startproject` creates the project structure.
- `python manage.py startapp` creates an app structure inside the project.

Example:

```powershell
(djenv) C:\djenv\demoproject> python manage.py startapp demoapp
```

- This creates a new folder named `demoapp`.
- The folder contains default Python files for common app responsibilities.

Example structure:

```text
C:\djenv\demoproject
|   db.sqlite3
|   manage.py
|
+---demoapp
|   |   admin.py
|   |   apps.py
|   |   models.py
|   |   tests.py
|   |   views.py
|   |   __init__.py
|   |
|   \---migrations
|           __init__.py
|
\---demoproject
    |   asgi.py
    |   settings.py
    |   urls.py
    |   wsgi.py
    |   __init__.py
```

##### `views.py`

- A view is a function or class that handles a web request and returns a web response.
- Django calls a view after the URL dispatcher matches the request URL to a URL pattern.
- The auto-created `views.py` file is empty at the beginning.

Example view:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the index view of Demoapp.")
```

##### App-level `urls.py`

- The project package already has a `urls.py` file for project-level URL routing.
- An app can also have its own `urls.py` file.
- New app folders do not include `urls.py` automatically.
  - Create it manually when the app needs its own URL routes.

Create `demoapp/urls.py`:

```python
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
]
```

##### Project-level `urls.py`

- The project-level `urls.py` connects project URLs to app URLs.
- Use `include()` to delegate a URL path to an app's URL configuration.

Update `demoproject/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("demo/", include("demoapp.urls")),
    path("admin/", admin.site.urls),
]
```

- With this setup, a request to `/demo/` is routed to `demoapp.urls`.
- `demoapp.urls` then routes the request to the `index` view.

##### `models.py`

- `models.py` contains the data models for the app.
- A model is a Python class based on Django's model system.
- Models define the structure of database-backed data.
- The file is empty by default.
- Leave it unchanged until the app needs database models.

##### `tests.py`

- `tests.py` contains automated tests for the app.
- It is created automatically.
- It can stay unchanged until you start writing tests.

##### Registering the app in `settings.py`

- To activate the app in the project, add it to `INSTALLED_APPS`.
- `INSTALLED_APPS` is located in the project package's `settings.py` file.

Example:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "demoapp",
]
```

##### Testing the app route

- After creating the app, adding a view, connecting URLs, and updating `INSTALLED_APPS`, run the development server.

```bash
python manage.py runserver
```

- Then visit:

```text
http://localhost:8000/demo/
```

- If everything is connected correctly, the browser shows the response from the `index` view.

##### Other app files

- Django apps can contain more files than the default structure.
- Common extra files include:
  - `forms.py`,
  - `serializers.py`.
- These files are added when the app needs the related functionality.

##### Application to chef_stable

Create the `demoapp` app inside the `chef_stable` project:

```bash
.venv\Scripts\Activate.ps1
cd 03_Django/lab/01-django-demo/chef_stable
python manage.py startapp demoapp
```

Update the project to use the new app:

- Update the `demoapp/views.py` file with the example view.
- Create the `demoapp/urls.py` file with the example URL patterns.
- Update the project-level `urls.py` to include the app's URLs.
- Add `demoapp` to `INSTALLED_APPS` in `settings.py`.

Run the development server and test the app route:

```bash
python manage.py runserver 127.0.0.1:8001
# Browser: http://127.0.0.1:8001/demo/
# Shows: Hello, world. This is the index view of Demoapp.
```

#### Re-Usability of Apps

- A Django app is reusable because it is a Python package.
- The app does not have to permanently live inside one project folder.
- Django can use an app as long as:
  - Python can import it,
  - the app is listed in `INSTALLED_APPS`,
  - its models, migrations, views, URLs, templates, and static files are organized in a project-independent way.

In small learning projects, apps are often created directly inside the project:

```text
demoproject/
|   manage.py
|
+---demoapp
|   |   apps.py
|   |   models.py
|   |   views.py
|   |   urls.py
|   |   __init__.py
|
\---demoproject
    |   settings.py
    |   urls.py
```

This is convenient while learning, but it can make the app feel tied to that one project.

For reuse, the app can be moved into its own package or repository:

```text
django-demoapp/
|   pyproject.toml
|
\---demoapp
    |   apps.py
    |   models.py
    |   views.py
    |   urls.py
    |   __init__.py
    |
    \---migrations
            __init__.py
```

Another Django project can then install it and register it:

```bash
pip install django-demoapp
```

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "demoapp",
]
```

The important idea is that Django does not care whether the app was created inside the current project. It only needs the app to be importable by Python and configured in the project settings.

##### Ways to share a reusable app

- Publish or install it as a Python package.
  - This is the most common approach for public or widely reused Django apps.
  - The app can be installed with `pip`.
  - Versioning is handled through package versions.
- Keep it in a separate internal Git repository.
  - This works well for organization-specific apps.
  - Projects can install it directly from Git.
- Add it as a Git submodule.
  - This can work when you want the app source code checked out inside each project repository.
  - The main project points to a specific commit of the app repository.
  - This gives precise control over which app version each project uses.

Example with a Git submodule:

```bash
git submodule add <repository-url> demoapp
git submodule update --init --recursive
```

Then the project can register the app as usual:

```python
INSTALLED_APPS = [
    "demoapp",
]
```

Git submodules are useful, but they add extra workflow steps. Developers must remember to initialize, update, and commit submodule references. For many teams, installing the app as a normal Python dependency is simpler.

##### What makes an app reusable?

- It has one clear responsibility.
- It avoids hard-coded project-specific paths.
- It avoids depending on one project's URL structure.
- It includes migrations for its models.
- It documents any required settings.
- It can be added to another project's `INSTALLED_APPS`.
- It exposes clear integration points, such as:
  - URL patterns,
  - views,
  - models,
  - forms,
  - templates,
  - static files.

#### Summary: Create a Django Project and App

Use this checklist when creating a new Django project with one app.

1. Create and enter a project folder.

```powershell
mkdir my_django_project
cd my_django_project
```

2. Create and activate a virtual environment.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install Django.

```bash
pip install django
```

4. Create the Django project in the current folder.

```bash
django-admin startproject config .
```

- `config` is the project package.
- `.` means "create the project files in the current directory".
- This avoids creating an extra outer folder.

The project now has a structure like this:

```text
my_django_project/
|   manage.py
|
\---config/
    |   settings.py
    |   urls.py
    |   asgi.py
    |   wsgi.py
    |   __init__.py
```

5. Create an app.

```bash
python manage.py startapp demoapp
```

The project now also contains:

```text
demoapp/
|   admin.py
|   apps.py
|   models.py
|   tests.py
|   views.py
|   __init__.py
|
\---migrations/
    |   __init__.py
```

6. Add a view in `demoapp/views.py`.

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the index view of Demoapp.")
```

7. Create `demoapp/urls.py`.

```python
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
]
```

8. Connect the app URLs in the project-level `config/urls.py`.

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("demo/", include("demoapp.urls")),
    path("admin/", admin.site.urls),
]
```

- `path("demo/", include("demoapp.urls"))` maps `/demo/` to the app's URL configuration.
- The app's `urls.py` then maps the empty path `""` to the `index` view.

9. Register the app in `config/settings.py`.

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "demoapp",
]
```

10. Apply the initial migrations.

```bash
python manage.py migrate
```

11. Run the development server.

```bash
python manage.py runserver
```

12. Open the app route in the browser.

```text
http://127.0.0.1:8000/demo/
```

Expected result:

```text
Hello, world. This is the index view of Demoapp.
```

The request flow is:

```text
Browser URL -> project urls.py -> app urls.py -> view -> HTTP response
```

### Web Frameworks and MVT

#### What is a Web Framework?

- A web framework is a toolkit for building web applications with a clear structure.
  - It makes development easier.
  - It keeps application code organized.
  - It supports reuse through existing components and patterns.
- Static websites may only need:
  - HTML,
  - CSS,
  - JavaScript.
- Dynamic websites usually need a back end when they include:
  - user accounts,
  - e-commerce,
  - payments,
  - forms,
  - security,
  - database storage.
- The front end is the part the user interacts with in the browser.
- The back end runs on a server and manages application logic, data, and database access.
- Django is a high-level Python web framework.
  - It is free and open source.
  - It supports rapid development.
  - It encourages clean, pragmatic design.
  - It helps developers avoid rebuilding common web features from scratch.
- Django is useful because it provides:
  - speed,
  - built-in features,
  - security support,
  - scalability.
- Built-in Django features include:
  - user authentication,
  - content administration,
  - sitemaps,
  - RSS feeds.
- Three-tier architecture splits an application into three logical parts.
  - The presentation tier contains the user interface.
  - The application tier contains the back-end logic.
  - The data tier stores and retrieves data.
- These tiers are logical, not necessarily physical.
  - All three can run on the same server.
  - They can also be separated across different systems.
- In a Django web application, Django usually acts as the application tier between the browser-facing interface and the database.

![Three-Tier Architecture](./assets/tiers.png)

#### Model-View-Template (MVT) Overview

##### Web framework

- A software framework is a standard, reusable platform for building applications faster.
- A web framework, or web application framework, provides common functionality for building:
  - web applications,
  - APIs (application programming interfaces),
  - web services.
- A web framework gives developers built-in support for everyday web development tasks.
  - It can help connect an application to a database.
  - It can handle session management.
  - It can integrate with templating tools to render dynamic web pages.

##### MVC architecture

- Many web frameworks use the MVC (Model-View-Controller) architecture.
- MVC separates a web application into three layers:
  - Model,
  - View,
  - Controller.

The following diagram shows how these layers work together.

![Diagram for model-view-controller architecture layers](./assets/mvc.png)

- In MVC, the controller intercepts user requests.
- The controller coordinates with the model and view layers.
- The model is responsible for:
  - data definitions,
  - processing logic,
  - interaction with the back-end database.
- The view is the presentation layer.
  - It handles placement and formatting of the result.
  - It sends the result back through the controller.

##### MVT architecture

- Django uses MTV (Model-Template-View), often described in course material as MVT (Model-View-Template).
- MVT is a variation of the MVC pattern.
- In Django's version:
  - the model is the **data layer**,
  - the view contains the **request-handling and processing logic**,
  - the template is the **presentation layer**.

![Diagram for model-view-template architecture layers](./assets/mvt.png)

A Django application uses these main components:

- URL dispatcher,
- view,
- model,
- template.

##### URL dispatcher

- Django's URL dispatcher performs a controller-like role.
- The project-level `urls.py` file defines URL patterns.
- Each URL pattern maps a URL path to a view.
- App-level URL patterns can also be included in the project-level `urls.py`.

Example app-level `urls.py`:

```python
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
]
```

- When Django receives a request, it compares the request URL against the available URL patterns.
- When a pattern matches, Django routes the request to the associated view.

##### View

- A Django view is a callable that receives a request and returns a response.
- A view can be:
  - a user-defined function,
  - a class-based view.
- A view can read data from the request.
  - This can include path parameters, query parameters, and request body data.
- A view can interact with models to perform CRUD (create, read, update, delete) operations.
- View definitions are usually placed in an app's `views.py` file.

Example `index` view:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

##### Model

- A model is a Python class that represents application data.
- An app can have one or more model classes.
- Models are conventionally placed in the app's `models.py` file.
- Django migrations use model definitions to create matching database tables.
- Django's ORM (Object-Relational Mapper) lets developers perform CRUD operations with Python objects instead of writing SQL directly.

##### Template

- A template is an HTML file that can contain Django Template Language blocks.
- Templates are usually placed in a `templates` folder.
- Template files commonly use the `.html` extension.
- A view can pass context data to a template.
- Django's template processor combines:
  - static HTML,
  - Django Template Language,
  - context data from the view.
- The view returns the rendered result as the HTTP response.

The MVT request-response flow is:

```text
Request -> URL dispatcher -> view -> model, if needed -> template, if needed -> response
```

#### MVT Example

Three-step MVT demonstration:

- first, a view returns plain text,
- then, a view reads data from a model,
- finally, a view renders the model data through a template.

The example is implemented in this repository at:

- lab project: [`03_Django/lab/01-django-demo/chef_stable`](./lab/01-django-demo/chef_stable),
- project package: `chef_stable`,
- app package: `little_lemon`.

##### 1. Create the project and app

The lab already contains the Django project. The `little_lemon` app was added inside the existing `chef_stable` project so it stays separate from the earlier `demoapp` exercise.

Register the app in [`chef_stable/settings.py`](./lab/01-django-demo/chef_stable/chef_stable/settings.py):

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "demoapp",
    "little_lemon",
]
```

##### 2. Connect the URLs

The project-level URL configuration includes the app's routes.

[`chef_stable/urls.py`](./lab/01-django-demo/chef_stable/chef_stable/urls.py):

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("little-lemon/", include("little_lemon.urls")),
    path("demo/", include("demoapp.urls")),
    path("", include("demoapp.urls")),
    path("admin/", admin.site.urls),
]
```

Create the app-level URL configuration.

[`little_lemon/urls.py`](./lab/01-django-demo/chef_stable/little_lemon/urls.py):

```python
from django.urls import path

from . import views


urlpatterns = [
    path("hello/", views.hello, name="little_lemon_hello"),
    path("menu/<int:item_id>/", views.menu_item, name="little_lemon_menu_item"),
    path("menu-card/<int:item_id>/", views.menu_card, name="little_lemon_menu_card"),
]
```

##### 3. Example with only a view

The first view returns plain text directly to the browser.

[`little_lemon/views.py`](./lab/01-django-demo/chef_stable/little_lemon/views.py):

```python
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello World")
```

Run the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/little-lemon/hello/
```

Expected response:

```text
Hello World
```

##### 4. Example with model and view

The model represents a database table. Each model field becomes a database column.

[`little_lemon/models.py`](./lab/01-django-demo/chef_stable/little_lemon/models.py):

```python
from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
```

The lab includes a migration that creates the table and inserts two example rows.

[`little_lemon/migrations/0001_initial.py`](./lab/01-django-demo/chef_stable/little_lemon/migrations/0001_initial.py)

Apply the migration:

```bash
python manage.py migrate
```

Verification note from this workspace:

- `python manage.py check` passed.
- `python manage.py makemigrations --check --dry-run` reported no model changes.
- `python manage.py migrate little_lemon` failed locally with `django.db.utils.OperationalError: disk I/O error`.
  - The failed transaction left a `db.sqlite3-journal` file next to `db.sqlite3`.
  - Close any running Django/Python process that may be holding the SQLite database open.
  - Then rerun `python manage.py migrate`.
  - If the local lab database remains broken, recreate the local SQLite database for the lab and rerun migrations.

Update `little_lemon/views.py` so a view can retrieve one menu item by ID:

```python
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import MenuItem


def hello(request):
    return HttpResponse("Hello World")


def menu_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return HttpResponse(f"{item.name}: {item.description}.")
```

Open:

```text
http://127.0.0.1:8000/little-lemon/menu/1/
```

Expected response:

```text
Pasta: Type of Italian cuisine.
```

Changing the URL from `/little-lemon/menu/1/` to `/little-lemon/menu/2/` fetches a different database row and returns different text.

##### 5. Example with model, view, and template

Create a template folder inside the app:

```text
little_lemon/
\---templates/
    \---little_lemon/
            menu_card.html
```

[`little_lemon/templates/little_lemon/menu_card.html`](./lab/01-django-demo/chef_stable/little_lemon/templates/little_lemon/menu_card.html):

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ item.name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 2rem;
        }

        .menu-card {
            border: 1px solid #ddd;
            padding: 1rem;
            max-width: 24rem;
        }
    </style>
</head>
<body>
    <article class="menu-card">
        <h1>{{ item.name }}</h1>
        <p>{{ item.description }}</p>
    </article>
</body>
</html>
```

Update `little_lemon/views.py` to render the template:

```python
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import MenuItem


def hello(request):
    return HttpResponse("Hello World")


def menu_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return HttpResponse(f"{item.name}: {item.description}.")


def menu_card(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, "little_lemon/menu_card.html", {"item": item})
```

Open:

```text
http://127.0.0.1:8000/little-lemon/menu-card/1/
```

This time, Django still retrieves `Pasta` from the database, but the response is rendered through HTML and CSS from the template.

##### What the example shows

```text
URL -> view only -> plain text response
URL -> view + model -> database-backed text response
URL -> view + model + template -> styled HTML response
```

The core MVT idea is that Django separates:

- data in the model,
- request and response logic in the view,
- presentation and styling in the template.

#### Additional Resources

- [Writing your first Django app -- official documentation](https://docs.djangoproject.com/en/4.1/)
- [MVT Framework -- Django](https://docs.djangoproject.com/en/4.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)
- [How to structure your Django project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

## 2. Views

### Views

#### Introduction to Views

- Static websites can serve fixed files directly from a web server.
- Dynamic websites often need logic that retrieves or creates data before returning a response.
- In Django, a view contains the logic for handling a web request and returning a web response.
  - A simple view is a Python function.
  - The first parameter is an `HttpRequest` object, usually named `request`.
  - The view must return an `HttpResponse` object or another valid Django response.
- A view can do more than return plain HTML.
  - It can process forms.
  - It can send emails.
  - It can retrieve data from a database.
  - It can transform data.
  - It can render templates.
- View functions are usually placed in an app's `views.py` file.
  - Django does not require this filename.
  - The convention makes the project easier for other developers to understand.
- Creating a view is not enough by itself.
  - The view must be mapped to a URL.
  - Mapping a URL to a view is called routing.
  - App-level routes are commonly defined in the app's `urls.py` file.

```python
# views.py
from django.http import HttpResponse


def home(request):
    content = "<html><body><h1>Welcome to Little Lemon!</h1></body></html>"
    return HttpResponse(content)
```

```python
# urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
]
```

- In `path("", views.home, name="home")`:
  - `""` is the URL route for the app's root path.
  - `views.home` is the view function Django calls.
  - `"home"` is the route name, which can be used later to refer to this URL.

#### Creating Views and Mapping to URLs

- A Django URL configuration is often called a URLconf.
- URLconf code usually lives in `urls.py`.
- Django creates a project-level `urls.py` file by default.
- It is also best practice to create an app-level `urls.py` file.
  - App-level URL files keep each app's routes grouped together.
  - The project-level URL file connects the project to each app's URL file.
- A request is first checked against the project-level `urlpatterns`.
- `include()` tells Django to continue matching URLs in another URLconf.
- `path()` maps a URL route to a view.
  - The first argument is the route string.
  - The second argument is the view or included URLconf.
  - The optional `name` argument gives the route a reusable name.

![URL Pipeline](./assets/url_pipeline.png)

Create a homepage view in the app's `views.py` file:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Little Lemon restaurant.")
```

Create an app-level `urls.py` file:

```python
from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
]
```

Connect the app-level URLconf from the project-level `urls.py` file:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("myapp.urls")),
    path("admin/", admin.site.urls),
]
```

Run the development server:

```bash
python manage.py runserver
```

Request flow:

```text
Browser -> project urls.py -> app urls.py -> view function -> HttpResponse
```

With the route set to `""`, opening the local project root displays:

```text
Welcome to the Little Lemon restaurant.
```

#### View Logic

The view plays a central role in Django's MVT (Model-View-Template) architecture.

- The URL dispatcher calls the view that matches the requested URL pattern.
- The view receives request data through an `HttpRequest` object.
- The view applies application logic.
- The view can interact with:
  - models, to read or write database-backed data,
  - templates, to format the response as HTML.
- The view returns an `HttpResponse` or another valid Django response object.

##### What a view does

A view usually coordinates the request-response work for one route.

- It can read data from the request.
- It can fetch one or more model objects.
- It can create, update, or delete model objects.
- It can prepare context data for a template.
- It sends an appropriate response back to the client.

##### GET and POST methods

HTTP methods help the view decide what kind of action the client is requesting.

- `GET` is commonly used to request or read data.
- `POST` is commonly used to submit data that may create or update server-side state.

```python
from django.http import HttpResponse


def myview(request):
    if request.method == "GET":
        return HttpResponse("response to GET request")

    if request.method == "POST":
        return HttpResponse("response to POST request")

    return HttpResponse("method not supported", status=405)
```

Request data can be read from `request.GET` or `request.POST`.

```python
from django.http import HttpResponse


def myview(request):
    if request.method == "GET":
        value = request.GET.get("key")
        # Use value to read or filter model data.
        return HttpResponse(f"GET value: {value}")

    if request.method == "POST":
        value = request.POST.get("key")
        # Use value to create or update model data.
        return HttpResponse(f"POST value: {value}")

    return HttpResponse("method not supported", status=405)
```

##### Rendering a template

A browser usually expects an HTML response. A view can use `render()` to combine a template with context data and return an `HttpResponse`.

```python
from django.shortcuts import render


def myview(request):
    context = {}

    if request.method == "GET":
        # Read model data and add it to context.
        context["message"] = "Data loaded with GET."

    if request.method == "POST":
        # Process submitted data and add the result to context.
        context["message"] = "Data submitted with POST."

    return render(request, "mytemplate.html", context)
```

##### Function-based views

The examples above are function-based views.

- A function-based view is a regular Python function.
- It receives `request` as its first argument.
- It can use conditional logic to handle different HTTP methods.
- It is direct and useful for learning the fundamentals.
- It can become repetitive when many views use similar GET and POST patterns.

##### Class-based views

Django also supports class-based views. A class-based view can separate HTTP method logic into methods such as `get()` and `post()`.

```python
from django.http import HttpResponse
from django.views import View


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("response to GET request")

    def post(self, request, *args, **kwargs):
        return HttpResponse("response to POST request")
```

Map a class-based view to a URL with `as_view()`:

```python
from django.urls import path

from .views import MyView


urlpatterns = [
    path("my-view/", MyView.as_view(), name="my_view"),
]
```

##### Generic views

Django provides generic class-based views in `django.views.generic`.

- Generic views implement common web application patterns.
- They are ready-made class-based views.
- They reduce repeated view logic.
- They are useful when a view follows a standard shape.
- Examples include:
  - `TemplateView`,
  - `CreateView`,
  - `ListView`,
  - `DetailView`,
  - `UpdateView`.
- They can render templates, show lists, show detail pages, create records, and update records.
- They usually require configuration such as:
  - `model`,
  - `template_name`,
  - `context_object_name`.

For example, a `ListView` can replace a function-based view that fetches all objects and renders them in a template.

Manual function-based version:

```python
from django.shortcuts import render

from .models import MenuItem


def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(
        request,
        "little_lemon/menu_list.html",
        {"menu_items": menu_items},
    )
```

Generic class-based version:

```python
from django.views.generic import ListView

from .models import MenuItem


class MenuItemListView(ListView):
    model = MenuItem
    template_name = "little_lemon/menu_list.html"
    context_object_name = "menu_items"
```

Map the generic view to a URL with `as_view()`:

```python
from django.urls import path

from .views import MenuItemListView


urlpatterns = [
    path("menu/", MenuItemListView.as_view(), name="menu_list"),
]
```

In this example, `ListView` handles the repeated workflow:

- get objects from the model,
- prepare context data,
- render a template,
- return an HTTP response.

The tradeoff is:

- function-based views are explicit and easier while learning,
- generic views are shorter and reduce repetition,
- generic views can feel less obvious at first because Django performs more work internally.

Function-based views are the best starting point in this introductory section. Class-based views and generic views become useful as projects grow and repeated view patterns appear.

#### Creating Views and View Logic

- A view function can return text or HTML by returning an `HttpResponse`.
- A view function does not become visible in the browser by itself.
  - It must be mapped to a URL.
  - The URL mapping is defined in a `urls.py` file.
- The first argument to `path()` is the URL suffix.
  - For example, `path("say-hello/", views.hello)` maps the `/say-hello/` URL suffix.
- If the browser opens a URL that is not mapped, Django returns a `404 Page not found` response.
- View logic can use normal Python code.
  - For example, a view can import `datetime` and return the current year.
- A view can return simple HTML markup.
  - Later sections use templates for larger, cleaner HTML pages.

Example `views.py`:

```python
from datetime import date

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello World")


def homepage(request):
    return HttpResponse("Welcome to Little Lemon")


def display_date(request):
    date_joined = date.today().year
    return HttpResponse(str(date_joined))


def menu(request):
    content = """
    <h1 style="color: #495e57;">Little Lemon Menu</h1>
    <p>Falafel</p>
    <p>Pasta</p>
    <p>Salad</p>
    """
    return HttpResponse(content)
```

Example `urls.py`:

```python
from django.urls import path

from . import views


urlpatterns = [
    path("say-hello/", views.hello, name="hello"),
    path("homepage/", views.homepage, name="homepage"),
    path("display-date/", views.display_date, name="display_date"),
    path("menu/", views.menu, name="menu"),
]
```

Example URLs:

```text
http://127.0.0.1:8000/say-hello/
http://127.0.0.1:8000/homepage/
http://127.0.0.1:8000/display-date/
http://127.0.0.1:8000/menu/
```

#### Exercise: Create Views and Map to URLs

Folder: [`lab/02-django-views/`](./lab/02-django-views/).

Completed files:

- [`myapp/views.py`](./lab/02-django-views/myproject/myapp/views.py)
  - Imports `HttpResponse`.
  - Defines the `home(request)` view.
  - Returns:

```html
<h1> Welcome to Little Lemon! </h1>
```

- [`myapp/urls.py`](./lab/02-django-views/myproject/myapp/urls.py)
  - Imports `path`.
  - Imports the app's `views`.
  - Maps the app root route to `views.home`.

```python
urlpatterns = [
    path("", views.home, name="home"),
]
```

- [`myproject/urls.py`](./lab/02-django-views/myproject/myproject/urls.py)
  - Imports `include`.
  - Includes `myapp.urls` at the project root.

```python
urlpatterns = [
    path("", include("myapp.urls")),
    path("admin/", admin.site.urls),
]
```

- [`myproject/settings.py`](./lab/02-django-views/myproject/myproject/settings.py)
  - Registers the app by adding `myapp.apps.MyappConfig` to `INSTALLED_APPS`.

Verification:

```bash
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

Run the project from `lab/02-django-views/myproject`:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

Expected page content:

```text
Welcome to Little Lemon!
```

### Requests and URLs

#### HTTP Requests

- HTTP (Hypertext Transfer Protocol) is the main protocol browsers use to communicate with web servers.
- HTTP transfers web resources such as:
  - HTML documents,
  - images,
  - stylesheets,
  - other files.
- HTTP is request-response based.
  - A client, usually a browser, sends an HTTP request.
  - A server sends an HTTP response.
- An HTTP request contains:
  - method,
  - path,
  - version,
  - headers,
  - optional body content.
- Common HTTP methods include:
  - `GET`, to retrieve a resource,
  - `POST`, to send data to the server,
  - `PUT`, to update an existing resource,
  - `DELETE`, to remove a resource.
- The path identifies where the requested resource is located on the server.
- Headers contain extra information about the request or client.
  - Examples include server information, port, method type, and content type.
- An HTTP response has a similar structure.
  - It includes headers.
  - It may include a response body, such as HTML, an image, or another resource.
  - It includes a status code and status message.
- HTTP status codes are grouped by purpose.
  - `100-199`: informational responses.
    - Example: `100 Continue`.
  - `200-299`: successful responses.
    - Example: `200 OK`.
  - `300-399`: redirection responses.
    - Example: `301 Moved Permanently`.
    - Example: `302 Found`.
  - `400-499`: client error responses.
    - `400 Bad Request` means the client sent bad data.
    - `401 Unauthorized` means authentication is required.
    - `403 Forbidden` means the request is valid, but the server refuses it.
    - `404 Not Found` means the requested resource was not found.
  - `500-599`: server error responses.
    - Example: `500 Internal Server Error`.
- `200 OK` can mean different things depending on the method.
  - For `GET`, the resource was found and returned.
  - For `POST` or `PUT`, submitted data was received successfully.
  - For `DELETE`, the resource was deleted successfully.
- HTTPS is the secure version of HTTP.
  - It uses encryption to protect data sent between client and server.
  - The browser lock icon usually indicates HTTPS.
  - The request-response pattern stays the same, but the content is protected during transfer.

Example HTTP request:

```http
# Request line: method path version
GET /menu/ HTTP/1.1

# Headers: extra information about the request
Host: littlelemon.example
User-Agent: Mozilla/5.0
Accept: text/html

# Body: empty for this GET request
```

Example HTTP response:

```http
# Status line: version status-code status-message
HTTP/1.1 200 OK

# Headers: extra information about the response
Content-Type: text/html; charset=utf-8
Content-Length: 46

# Body: content returned to the client
<h1>Welcome to the Little Lemon menu!</h1>
```

#### Request and Response Objects

A web application follows a request-response cycle.

- A browser sends a request to the server.
- Django receives the request from the server context.
- Django's URL dispatcher matches the request URL to a view.
- Django passes an `HttpRequest` object to the view as the first argument.
- The view creates and returns an `HttpResponse` object.

Django defines these classes in `django.http`:

- `HttpRequest`, which represents incoming request data.
- `HttpResponse`, which represents outgoing response data.

##### `HttpRequest` object

The `HttpRequest` object gives the view access to request metadata and submitted data.

Common request attributes:

- `request.method`
  - The HTTP method used by the client.
  - Common values include `"GET"`, `"POST"`, `"PUT"`, and `"DELETE"`.
- `request.GET`
  - A dictionary-like object for query-string parameters.
- `request.POST`
  - A dictionary-like object for submitted form data.
- `request.COOKIES`
  - A dictionary of cookie names and values sent by the browser.
- `request.FILES`
  - Uploaded files from multipart form submissions.
- `request.user`
  - The current user object when authentication middleware is enabled.
  - Unauthenticated users are represented by `AnonymousUser`.
- `request.headers`
  - A case-insensitive mapping of HTTP request headers.

Example method check:

```python
if request.method == "GET":
    do_something()
elif request.method == "POST":
    do_something_else()
```

Example request data access:

```python
search_term = request.GET.get("q")
submitted_name = request.POST.get("name")

if "User-Agent" in request.headers:
    user_agent = request.headers["User-Agent"]
```

Example authentication check:

```python
if request.user.is_authenticated:
    # Do something for logged-in users.
    ...
else:
    # Do something for anonymous users.
    ...
```

##### `HttpResponse` object

Unlike `HttpRequest`, which Django creates from the incoming request, `HttpResponse` is usually created inside the view.

Simple response:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")
```

Template response with `render()`:

```python
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "demoapp/index.html", context)
```

The `render()` shortcut combines three common steps:

- find and load a template,
- fill the template with context data,
- return an `HttpResponse` containing the rendered HTML.

The full signature is:

```python
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

Arguments:

- `request`
  - The current `HttpRequest` object.
  - Required.
- `template_name`
  - The template file Django should load.
  - Required.
  - Example: `"demoapp/index.html"`.
- `context`
  - A dictionary of data passed into the template.
  - Optional.
- `content_type`
  - The response MIME type.
  - Optional.
  - Defaults to `"text/html"`.
- `status`
  - The HTTP status code for the response.
  - Optional.
  - Defaults to `200`.
- `using`
  - The template engine name.
  - Optional.
  - Useful only when a project has multiple template engines.

Example view:

```python
from django.shortcuts import render


def menu(request):
    context = {
        "restaurant": "Little Lemon",
        "items": ["Pasta", "Falafel", "Salad"],
    }
    return render(request, "demoapp/menu.html", context)
```

Example template:

```html
<h1>{{ restaurant }}</h1>

<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

Mental model:

```text
request + template + context -> rendered HTML response
```

Useful response attributes and methods:

- `status_code`
  - The HTTP status code for the response.
- `content`
  - The response body as bytes.
- `response["Header-Name"]`
  - Reads a response header.
- `response["Header-Name"] = "value"`
  - Sets a response header.
- `set_cookie()`
  - Adds a cookie to the response.
- `write()`
  - Writes content to the response like a file-like object.

Example with response metadata:

```python
from django.http import HttpResponse


def index(request):
    path = request.path
    method = request.method
    content = f"""
    <center>
        <h2>Testing Django Request Response Objects</h2>
        <p>Request path: {path}</p>
        <p>Request method: {method}</p>
    </center>
    """
    response = HttpResponse(content)
    response["X-Demo"] = "request-response"
    return response
```

Start the server and visit:

```text
http://localhost:8000/demo/
```

![HTTP Response Demo](./assets/http_response_demo.png)

This example shows how a view can read data from `HttpRequest` and return formatted content with `HttpResponse`.

#### Creating Requests and Responses

- Django's request-response cycle starts when a user enters a URL in the browser.
- The web server passes the request to Django.
- Django checks the URL patterns in `urls.py`.
- When a URL pattern matches, Django calls the associated view.
- The view receives an `HttpRequest` object as its first argument.
- The view creates and returns an `HttpResponse` object.
- Django sends the response back to the client.
- `request.path` shows the requested path.
  - Example: `/main/home/`.
  - If the URL configuration changes, the displayed path changes too.
- `HttpResponse` can be returned directly or assigned to a variable before returning.
- Request attributes can be displayed by reading values from the `request` object.
  - Useful examples include:
    - `request.scheme`,
    - `request.method`,
    - `request.path`,
    - `request.path_info`,
    - `request.headers.get("User-Agent")`,
    - `request.META.get("REMOTE_ADDR")`.
- Response headers can be added to the `HttpResponse` object.
- Request and response objects are especially important when working with:
  - `GET` and `POST` methods,
  - forms,
  - databases,
  - other data-driven Django features.

Example view:

```python
from django.http import HttpResponse


def home(request):
    path = request.path
    method = request.method
    scheme = request.scheme
    path_info = request.path_info
    user_agent = request.headers.get("User-Agent", "Unknown")
    remote_address = request.META.get("REMOTE_ADDR", "Unknown")

    message = f"""
    <h1>Request information</h1>
    <p>Path: {path}</p>
    <p>Method: {method}</p>
    <p>Scheme: {scheme}</p>
    <p>Path info: {path_info}</p>
    <p>User agent: {user_agent}</p>
    <p>Remote address: {remote_address}</p>
    """

    response = HttpResponse(
        message,
        content_type="text/html; charset=utf-8",
    )
    response.headers["Age"] = "20"
    return response
```

Example URL mapping:

```python
from django.urls import path

from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
]
```

If this app is included under `main/` at the project level, visit:

```text
http://127.0.0.1:8000/main/home/
```

The browser displays request information generated from the `HttpRequest` object, and the response includes the custom `Age` header.

#### Understanding URLs

- A URL (Uniform Resource Locator) is the address of a specific web resource.
  - The resource can be a web page, image, document, metadata file, or another file sent over HTTP.
  - Each URL points to a specific location on the web or on a local server.
- A URL is built from several parts.
  - The scheme identifies the protocol.
  - The subdomain appears before the main domain.
  - The domain identifies the website or organization.
  - The path identifies the resource location.
  - Query parameters provide extra information.
- The scheme is also called the protocol.
  - Common schemes are `http` and `https`.
  - HTTP (Hypertext Transfer Protocol) sends and receives web resources.
  - HTTPS is the secure version of HTTP.
    - It encrypts transferred data.
    - Browsers often show HTTPS with a lock icon.
- The domain name usually has two main parts.
  - The second-level domain often identifies the organization or site name.
  - The top-level domain identifies a category or country.
    - `.com` often indicates a commercial site.
    - `.org` often indicates an organization.
    - `.ie` indicates Ireland.
- The path, also called the page path or file path, points to a resource.
  - Paths can point to web pages, images, documents, or other files.
  - Resources can be local to a server or hosted externally.
- Query strings begin with `?`.
  - They contain key-value pairs.
  - Multiple parameters are separated with `&`.
  - Django can read query string values from `request.GET`.
- Django URL patterns can also capture parts of the path.
  - Example: `path("articles/<int:year>/", views.year_archive)`.
  - The captured value is passed to the view for processing.
- URL design means intentionally creating clear, useful URLs.
  - Good URL design depends on the website content and application structure.
  - Django developers need to understand URL parts to design routes well.

Example URL:

```text
https://www.littlelemon.com/menu/items/?category=pasta&page=2
|___|   |__| |______________| |_________| |_____________________|
scheme  sub  domain          path        query string
```

Parts:

```text
scheme: https
subdomain: www
second-level domain: littlelemon
top-level domain: com
path: /menu/items/
query string: ?category=pasta&page=2
query parameters:
  category = pasta
  page = 2
```

#### Parameters

Parameters let the client send extra data to a Django view. A view always receives the `request` object, and it can also receive additional values from the URL or request body.

This section covers three common parameter types:

- path parameters,
- query parameters,
- body parameters.

These parameters are often connected to HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.

##### Path parameters

Path parameters are values embedded directly in the URL path.

Example URL:

```text
http://localhost:8000/getuser/John/1/
```

In this URL:

- `John` is the `name` parameter,
- `1` is the `id` parameter.

Define the route in the app-level `urls.py` file:

```python
path("getuser/<str:name>/<int:id>/", views.pathview, name="pathview")
```

Define the view in `views.py`:

```python
from django.http import HttpResponse


def pathview(request, name, id):
    return HttpResponse(f"Name: {name} UserID: {id}")
```

The names inside the URL pattern must match the view function parameters:

- `<str:name>` maps to `name`,
- `<int:id>` maps to `id`.

##### Path converters

Django treats values inside angle brackets as path parameters.

Common path converters:

- `str`
  - Matches any non-empty string except the path separator `/`.
  - This is the default converter.
- `int`
  - Matches zero or a positive integer.
  - Returns an `int`.
  - Example: `customer/<int:id>/`.
- `slug`
  - Matches ASCII letters, numbers, hyphens, and underscores.
- `uuid`
  - Matches a formatted UUID.
  - Returns a `UUID` instance.
  - Example: `075194d3-6885-417e-a8a8-6c931e272f00`.
- `path`
  - Matches a non-empty string.
  - Includes the path separator `/`.

There is no built-in `date` or `float` path converter in Django.

If a route needs one of those types, create a custom converter and register it in the URL configuration.

Example custom converters:

```python
# converters.py
from datetime import date


class DateConverter:
    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        year, month, day = map(int, value.split("-"))
        return date(year, month, day)

    def to_url(self, value):
        return value.isoformat()


class FloatConverter:
    regex = r"\d+(?:\.\d+)?"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)
```

Register the converters before using them in `urlpatterns`:

```python
# urls.py
from django.urls import path, register_converter

from . import converters, views

register_converter(converters.DateConverter, "date")
register_converter(converters.FloatConverter, "float")

urlpatterns = [
    path("sales/<date:day>/", views.sales_by_day, name="sales_by_day"),
    path("products/under/<float:price>/", views.products_under_price, name="products_under_price"),
]
```

Then Django passes converted Python values to the view:

```python
def sales_by_day(request, day):
    # day is a datetime.date object.
    ...


def products_under_price(request, price):
    # price is a float.
    ...
```

##### Query parameters

Query parameters are key-value pairs added after the URL path.

Example URL:

```text
http://localhost:8000/myapp/getuser/?name=John&id=1
```

A query string:

- starts with `?`,
- uses `key=value` pairs,
- separates multiple pairs with `&`.

Django's URL dispatcher does not parse query parameters into view arguments. The view reads them from `request.GET`.

Define the route:

```python
path("getuser/", views.qryview, name="qryview")
```

Define the view:

```python
from django.http import HttpResponse


def qryview(request):
    name = request.GET.get("name")
    id = request.GET.get("id")
    return HttpResponse(f"Name: {name} UserID: {id}")
```

##### Body parameters

Body parameters are submitted in the request body, usually through an HTML form.

- HTML forms often send body data with `POST`.
- `POST` data is not shown in the URL.
- Django reads submitted form values from `request.POST`.

Create `form.html` in the templates folder:

```html
<form action="/myapp/getform/" method="post">
    {% csrf_token %}
    <p>Name: <input type="text" name="name"></p>
    <p>UserID: <input type="text" name="id"></p>
    <input type="submit">
</form>
```

The `{% csrf_token %}` tag helps protect against cross-site request forgery attacks.

Create a view to display the form:

```python
from django.shortcuts import render


def showform(request):
    return render(request, "form.html")
```

Add the route:

```python
path("showform/", views.showform, name="showform")
```

Visit:

```text
http://localhost:8000/myapp/showform/
```

![URL displaying the form to the user](./assets/show_form.png)

When the form is submitted, it sends a `POST` request to:

```text
http://localhost:8000/myapp/getform/
```

Add the route:

```python
path("getform/", views.getform, name="getform")
```

Handle the submitted form data:

```python
from django.http import HttpResponse


def getform(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        return HttpResponse(f"Name: {name} UserID: {id}")

    return HttpResponse("Submit the form with POST.")
```

Complete the form and submit it. The `getform()` function returns the data as its response.

![Return data display with the response](./assets/get_form.png)

In real applications, submitted data is often processed further, such as by saving it to a database. This is explored later with models, forms, and database connections.

##### `csrf_token`

`{% csrf_token %}` is a Django template tag used inside HTML forms that submit data with `POST`.

It helps protect the application against CSRF attacks. CSRF means Cross-Site Request Forgery. In this kind of attack, a malicious website tries to make a user's browser send a request to another website where the user is already logged in.

For example, imagine a user is logged in to a Django site in one browser tab. If they visit a malicious page in another tab, that page might try to submit a hidden form to the Django site. Without CSRF protection, the Django site might treat that request as if the user intentionally submitted it.

The template tag:

```html
{% csrf_token %}
```

is rendered by Django as a hidden input field:

```html
<input type="hidden" name="csrfmiddlewaretoken" value="generated-token-value">
```

When the form is submitted:

- the browser sends the hidden token with the form data,
- Django checks whether the token is valid,
- if the token is missing or invalid, Django rejects the request, usually with `403 Forbidden`.

Use `{% csrf_token %}` in Django templates for forms that use `method="post"`:

```html
<form action="/myapp/getform/" method="post">
    {% csrf_token %}
    <p>Name: <input type="text" name="name"></p>
    <input type="submit">
</form>
```

The short rule is: if a Django form changes or submits data with `POST`, include `{% csrf_token %}`.

#### Mapping URLs with Parameters

- URL parameters let Django capture part of the URL and pass it to a view.
  - The captured value becomes an argument after `request`.
  - This is useful when the URL itself identifies what data the view should process.
- Django captures path parameters with angle brackets inside `path()`.
  - Example: `<str:dish>` captures one URL segment as a string.
  - `str` is the path converter.
  - `dish` is the parameter name passed to the view.
- The parameter name in `urls.py` must match the view function argument.
  - `path("dishes/<str:dish>/", views.menu_items)` passes `dish` to `menu_items(request, dish)`.
  - If the URL is `/dishes/pasta/`, Django calls the view with `dish="pasta"`.
- Path converters can restrict and convert captured values.
  - `str` captures text without `/`.
  - `int` captures numbers and passes them to the view as integers.
  - An `int` parameter is often used to pass a database primary key to a view.
- URL parameters are useful for:
  - selecting dictionary values,
  - fetching database records,
  - grouping related content,
  - sending search, sorting, or filtering information to the view logic.

```python
# urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("dishes/<str:dish>/", views.menu_items, name="menu_items"),
]
```

```python
# views.py
from django.http import HttpResponse


def menu_items(request, dish):
    items = {
        "pasta": "Pasta is a type of noodle made from unleavened dough.",
        "falafel": "Falafel is a deep-fried ball made from ground chickpeas.",
        "cheesecake": "Cheesecake is a sweet dessert with a soft cheese filling.",
    }

    description = items.get(dish, "This item is not on the menu.")
    return HttpResponse(f"<h1>{dish}</h1><p>{description}</p>")
```

```text
http://127.0.0.1:8000/dishes/pasta/
```

In this example, Django captures `pasta` from the URL, passes it to the `dish` argument, looks it up in the `items` dictionary, and returns the matching description in the response.

#### Exercise: Mapping URLs with Parameters

Folder: [`lab/03-django-urls/`](./lab/03-django-urls/).

- Completed the exercise in `lab/03-django-urls/myproject`.
- Updated the app-level `myapp/urls.py`.
  - Kept the existing home route.
  - Added `path("drinks/<str:drink_name>", views.drinks, name="drinks")`.
  - The `<str:drink_name>` path converter captures the drink name from the URL.
- Updated `myapp/views.py`.
  - Added a `drinks(request, drink_name)` view.
  - Created a `drink` dictionary with:
    - `mocha`,
    - `tea`,
    - `lemonade`,
    - `espresso` as the optional extra item.
  - Used the captured `drink_name` value to look up the matching dictionary description.
  - Returned an `HttpResponse` with the drink name as an `<h2>` heading and the drink description after it.
- Verified the project with Django.
  - `python manage.py check` passed when run with the repository virtual environment.
  - The required URLs returned `200` responses:
    - `/drinks/mocha`,
    - `/drinks/tea`,
    - `/drinks/lemonade`.
  - The optional extra URL `/drinks/espresso` also returned a `200` response.

[`url.py`](./lab/03-django-urls/myproject/myapp/urls.py):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
]
```

[`views.py`](./lab/03-django-urls/myproject/myapp/views.py):

```python
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)
```

#### Additional Resources

- [Creating views - official documentation](https://docs.djangoproject.com/en/4.0/topics/http/views/)
- [Class-based views - Official](https://docs.djangoproject.com/en/4.0/topics/class-based-views/)
- [The render() function in Django](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#render)
- [Getting query parameters from a request in Django](https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters)
- [The HTTP server responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Creating URLs and Views

#### Regular Expressions in URLs

- Regular expressions, often called RegEx, define patterns for matching text.
  - They are used for validation, extraction, searching, grouping, and replacement.
  - In Django URL routing, they can validate the shape of a URL before a view is called.
- Django normally uses `path()` and path converters for readable URL patterns.
  - Example: `path("menu_item/<int:item_id>/", views.menu_item)`.
  - This is usually clearer than a regular expression.
- Django also provides `re_path()` for URL patterns that need regular expressions.
  - Import it from `django.urls`.
  - Use it when the route needs more specific matching than `path()` provides.
  - Captured regex groups are passed to the view as strings.
- A static path only matches one exact URL.
  - `path("menu_item/10/", views.menu_item)` matches `/menu_item/10/`.
  - It does not match `/menu_item/1/` or `/menu_item/99/`.
- A regex path can match a family of URLs with the same structure.
  - `r"^menu_item/([0-9]{2})/$"` matches exactly two digits.
  - Examples include `/menu_item/10/`, `/menu_item/25/`, and `/menu_item/99/`.
- Common regex symbols include:
  - `^` anchors the match to the start of the string.
  - `$` anchors the match to the end of the string.
  - `[0-9]` matches one digit from `0` to `9`.
  - `{2}` requires exactly two occurrences of the previous pattern.
  - `()` creates a captured group.
  - `(?P<name>pattern)` creates a named captured group.
- Raw strings are commonly used for regex routes.
  - Prefixing the string with `r` helps Python treat backslashes as regex characters.
  - Example: `r"^menu_item/(?P<item_id>[0-9]{2})/$"`.
- Prefer named groups when the captured value should become a named view argument.
  - Named groups make the route easier to connect to the view signature.
  - Example: `(?P<item_id>[0-9]{2})` maps to `item_id` in the view.
- Regular expressions are powerful but can become hard to read.
  - Use `path()` and converters for common cases.
  - Use `re_path()` when the URL format needs precise validation.

```python
# urls.py
from django.urls import path, re_path

from . import views


urlpatterns = [
    # Static route: only matches /menu_item/10/.
    path("menu_item/10/", views.menu_item_static, name="menu_item_static"),

    # Regex route: matches /menu_item/10/, /menu_item/25/, /menu_item/99/, etc.
    re_path(
        r"^menu_item/(?P<item_id>[0-9]{2})/$",
        views.menu_item_by_id,
        name="menu_item_by_id",
    ),
]
```

```python
# views.py
from django.http import HttpResponse


def menu_item_static(request):
    return HttpResponse("<h1>Menu item 10</h1>")


def menu_item_by_id(request, item_id):
    # re_path() passes captured values as strings.
    return HttpResponse(f"<h1>Menu item {item_id}</h1>")
```

#### URL Namespacing and Views

This reading explains named URLs in a Django URL configuration, also called a URLconf. It also explains how namespaces help Django resolve URL names when more than one app uses the same route name.

##### Named URLs

Each app can have a `urls.py` file that defines URL patterns for that app.

Each pattern is usually created with `django.urls.path()`.

The common arguments are:

- the URL path string,
- the view function mapped to that URL,
- the optional `name` argument.

Example app-level URLconf:

```python
# demoapp/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
]
```

The app-level URLconf is included in the project-level `urlpatterns`.

```python
# demoproject/urls.py
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("demoapp.urls")),
]
```

When a request comes in, Django compares the requested URL with the URL patterns and calls the matching view.

Hard-coded URL strings can work, but they make a project harder to maintain as it grows.

Example hard-coded form action:

```html
<form action="/demoapp/login/" method="post">
    <!-- form fields -->
</form>
```

If the URL pattern changes later, every hard-coded reference must be updated manually.

##### `reverse()`

Django can build a URL from the route name instead of relying on a hard-coded path.

Start the Django shell:

```bash
python manage.py shell
```

Use `reverse()` to return the URL path mapped to a named URL:

```pycon
>>> from django.urls import reverse
>>> reverse("index")
'/demo/'
```

The problem appears when more than one app defines the same URL name, such as `index` or `login`. This is where namespaces become useful.

##### Application namespace

An application namespace is created by defining `app_name` in the app's `urls.py` file.

```python
# demoapp/urls.py
from django.urls import path

from . import views

# This is the namespace, which contains the URL names defined in this app.
app_name = "demoapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
]
```

The `app_name` identifies the URLs that belong to this app.

To reverse a URL inside a namespace, use this format:

```text
namespace:url_name
```

Example:

```pycon
>>> reverse("demoapp:index")
'/demo/'
```

Now add another app, such as `newapp`, with its own `index` view and its own application namespace.

```python
# newapp/urls.py
from django.urls import path

from . import views


app_name = "newapp"

urlpatterns = [
    path("", views.index, name="index"),
]
```

Include both apps in the project-level URLconf:

```python
# demoproject/urls.py
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("demoapp.urls")),
    path("newdemo/", include("newapp.urls")),
]
```

Now Django can distinguish between the two routes even though both apps use the name `index`.

```pycon
>>> reverse("demoapp:index")
'/demo/'
>>> reverse("newapp:index")
'/newdemo/'
```

##### Instance namespace

An instance namespace is set with the `namespace` argument in `include()`.

This is useful when the same app URLconf is included more than once in the same project.

```python
# demoproject/urls.py
from django.urls import include, path


urlpatterns = [
    path("demo/", include("demoapp.urls", namespace="demoapp")),
]
```

In this example, `demoapp` is the instance namespace used to resolve namespaced URLs.

##### Using namespaces in views

A view can use a namespaced URL when it needs to redirect to another view.

Example with `HttpResponsePermanentRedirect`:

```python
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


def myview(request):
    login_url = reverse("demoapp:login")
    return HttpResponsePermanentRedirect(login_url)
```

This avoids hard-coding the login URL in the view.

Django also provides the `redirect()` shortcut, which can redirect directly to a named URL:

```python
from django.shortcuts import redirect


def myview(request):
    return redirect("demoapp:login")
```

##### Using namespaces in templates

An HTML form submits to the URL in its `action` attribute.

Hard-coded example:

```html
<form action="/demoapp/login/" method="post">
    <!-- form fields -->
    <input type="submit">
</form>
```

Instead of hard-coding the path, use Django's `{% url %}` template tag.

Without a namespace:

```html
<form action="{% url 'login' %}" method="post">
    <!-- form fields -->
    <input type="submit">
</form>
```

With a namespace:

```html
<form action="{% url 'demoapp:login' %}" method="post">
    <!-- form fields -->
    <input type="submit">
</form>
```

The namespaced version is safer when multiple apps define a `login` URL.

The browser shows the login form as below:

![Login form browser view with user name and password tabs as well as submit button](./assets/log_in_form.png)

Namespaces help resolve conflicts when multiple apps in the same project use the same URL names.

Some of these ideas connect closely to Django templates. They become clearer once templates are covered in more detail.

#### Exercise: Creating URLs and Mapping to Views

Folder: [`lab/04-django-urls-views/`](./lab/04-django-urls-views/).

This exercise adds four function-based views for the Little Lemon pages and maps them through an app-level URL configuration. The project-level `urls.py` already includes `myapp.urls`, so the app can define its own routes for the home, about, menu, and booking pages.

The completed exercise also applies the additional step from the lab: the `about` view is mapped to `aboutus/` instead of `about/`.

Summary of the completed views:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Little Lemon!")


def about(request):
    return HttpResponse("About us")


def menu(request):
    return HttpResponse("Menu")


def book(request):
    return HttpResponse("Make a booking")
```

Summary of the app-level URL mappings:

```python
from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("aboutus/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),
    path("book/", views.book, name="book"),
]
```

Expected browser paths:

| URL path | View function | Response text |
| --- | --- | --- |
| `/` | `home` | `Welcome to Little Lemon!` |
| `/aboutus/` | `about` | `About us` |
| `/menu/` | `menu` | `Menu` |
| `/book/` | `book` | `Make a booking` |

#### Error Handling

Errors can still happen even after testing and QA. Some errors come from application code, but others come from unreliable networks, missing resources, permission problems, invalid requests, or server failures.

HTTP responses include status codes that describe the result of a request:

- `1xx`: informational responses
- `2xx`: successful responses
- `3xx`: redirects or moved resources
- `4xx`: client-side request problems
- `5xx`: server-side failures

Common client error responses:

| Status code | Meaning | Typical cause |
| --- | --- | --- |
| `400 Bad Request` | The request is invalid. | The request parameters are missing, malformed, or not what the server expects. |
| `401 Unauthorized` | Authentication is required. | The user must log in before the request can be processed. |
| `403 Forbidden` | The request is understood but refused. | The user does not have permission to access the resource. |
| `404 Not Found` | The requested resource does not exist. | The URL path does not match an available resource or route. |

Common server error responses:

| Status code | Meaning | Typical cause |
| --- | --- | --- |
| `500 Internal Server Error` | The server failed while processing the request. | The application crashed, is not running correctly, or timed out while responding. |

Django handles many error cases by raising exceptions and then passing control to an error handling view. Django provides default error views, but a project can customize them so error pages match the style and behavior of the site.

Custom error handlers are configured in the root URL configuration for the project. Setting these variables in an app-level URL configuration has no effect.

```python
handler400 = "myproject.views.bad_request"
handler403 = "myproject.views.permission_denied"
handler404 = "myproject.views.page_not_found"
handler500 = "myproject.views.server_error"
```

The main handler variables are:

| Handler | Default purpose |
| --- | --- |
| `handler400` | Bad request view |
| `handler403` | Permission denied view |
| `handler404` | Page not found view |
| `handler500` | Server error view |

A custom error view accepts the request and returns an appropriate response. Some error views also receive an exception argument.

```python
from django.http import HttpResponseNotFound


def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")
```

Django also provides `HttpResponse` subclasses for common error responses:

| Class | Status code |
| --- | --- |
| `HttpResponseBadRequest` | `400` |
| `HttpResponseForbidden` | `403` |
| `HttpResponseNotFound` | `404` |
| `HttpResponseServerError` | `500` |

Key idea: error handling is not only about fixing broken code. It is also about giving clear, appropriate responses when a request cannot be completed.

#### Handling Errors in Views

In Django, a view receives an `HttpRequest`, runs the needed logic, and returns an `HttpResponse`. Error handling inside a view means returning the right response, raising the right exception, or allowing Django to display a configured error page.

**Returning Error Responses**

Each response has a status code. For example, `404` means the requested resource was not found.

One option is to return a specialized response class such as `HttpResponseNotFound`:

```python
from django.http import HttpResponse, HttpResponseNotFound


def my_view(request):
    if condition:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    return HttpResponse("<h1>Page was found</h1>")
```

You can also return a normal `HttpResponse` and set its status code explicitly:

```python
from django.http import HttpResponse


def my_view(request):
    if condition:
        return HttpResponse("<h1>Page not found</h1>", status=404)

    return HttpResponse("<h1>Page was found</h1>")
```

The specialized response class is clearer because the status code is built into the class name. `HttpResponseNotFound` automatically sends a `404` response.

**Raising `Http404`**

A common cause of a `404` is a user requesting an object that does not exist. In that case, a view can raise `Http404` instead of manually returning a `404` response.

Example: a user requests details for a product by ID. If no product exists with that primary key, the view raises `Http404`.

```python
from django.http import Http404, HttpResponse

from .models import Product


def detail(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return HttpResponse("Product Found")
```

This pattern keeps the view focused on the real business logic: find the object, or report that it does not exist.

**Useful Response Classes**

| Class | Status code | Use case |
| --- | --- | --- |
| `HttpResponseBadRequest` | `400` | Invalid request data |
| `HttpResponseForbidden` | `403` | User lacks permission |
| `HttpResponseNotFound` | `404` | Resource does not exist |
| `HttpResponseServerError` | `500` | Server-side failure |

**Custom Error Pages**

To show a custom page for a `404` error, create a `404.html` template in the project templates folder.

```text
project/
  templates/
    404.html
```

Django uses custom error pages when `DEBUG` is disabled. During development, `DEBUG=True` usually shows a detailed traceback instead.

![Standard 404 error page display on browser](./assets/page_not_found.png)

```python
# settings.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
```

![Page displaying the info that requested resource was not found on the server](./assets/page_not_found_2.png)

**Common Exception Classes**

Django exception classes are defined in `django.core.exceptions`.

| Exception | Meaning |
| --- | --- |
| `ObjectDoesNotExist` | Base exception for model-specific `DoesNotExist` exceptions |
| `EmptyResultSet` | A query does not return any result |
| `FieldDoesNotExist` | A requested model field does not exist |
| `MultipleObjectsReturned` | A query expected one object but returned multiple objects |
| `PermissionDenied` | The user does not have permission to perform the requested action |
| `ViewDoesNotExist` | A requested view cannot be found, often because of an incorrect URLconf mapping |

In addition to Django exceptions, views can also handle standard Python exceptions and database-related exceptions.

**Form Validation Errors**

For `POST` or `PUT` requests, the request body often contains form data. Django forms include built-in validation through fields such as `EmailField`, `FileField`, `IntegerField`, and `MultipleChoiceField`.

The `is_valid()` method returns `True` when the submitted data passes validation. If validation fails, the view can return an error response, re-render the form with errors, or raise an exception when appropriate.

```python
from django.http import Http404


def my_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid():
            # Process the form data.
            pass

        raise Http404("Invalid form data")
```

Key idea: handle errors in views by choosing the response that best matches the situation. Return an error response for direct control, raise an exception when Django should handle the error flow, and use custom templates when the user should see a polished error page.

#### Demo: Handling Errors in Views

This demo applies the previous error-handling ideas to a project-level `404` handler.

- With `DEBUG=True`, Django shows a technical 404 page for unmatched URLs.
- That developer page can include details such as the request method and requested URL.
- With `DEBUG=False`, Django shows the standard user-facing 404 page instead.
- When `DEBUG=False`, `ALLOWED_HOSTS` must contain at least one allowed host.
- The custom `handler404` variable belongs in the root URL configuration, outside the `urlpatterns` list.
- The custom 404 view can live in a project-level `views.py` file.
- A custom 404 view receives both `request` and `exception`.
- The 404 handler responds to URL paths that do not match any configured route.
- Existing routes still render normally; the handler only catches unmatched routes.
- `HttpResponseNotFound` may look the same in the browser as a normal response, but the client receives a real `404` status code.
- The actual status code can be checked in the browser's developer tools, in the Network tab.

Example root URL configuration:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

handler404 = "myproject.views.handler404"
```

Example project-level error view:

```python
from django.http import HttpResponseNotFound


def handler404(request, exception):
    return HttpResponseNotFound("<h1>404: Page not found</h1>")
```

Example production-style settings for testing the custom page:

```python
# settings.py

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

For a learning demo, `ALLOWED_HOSTS = ["*"]` can make local testing quick, but real projects should list the specific hosts they expect.

Good custom error pages should be easy for users to understand, match the site's style, and provide a clear path back to a useful page such as the homepage.

#### Class-based Views

Class-based views, often shortened to CBVs, are Django views written as classes instead of plain functions. They are useful when view logic grows beyond a simple request-and-response function.

Core idea:

- A view still receives an HTTP request and returns an HTTP response.
- A function-based view usually checks `request.method` with `if` or `elif`.
- A class-based view separates HTTP method handling into class methods such as `get()`, `post()`, `put()`, and `delete()`.
- This keeps each request type's logic in its own method.

Example class-based view:

```python
from django.http import HttpResponse
from django.views import View


class MenuView(View):
    def get(self, request):
        return HttpResponse("Show the menu")

    def post(self, request):
        return HttpResponse("Create a menu item")
```

Map a class-based view with `as_view()`:

```python
from django.urls import path

from .views import MenuView


urlpatterns = [
    path("menu/", MenuView.as_view(), name="menu"),
]
```

Why use class-based views:

| Benefit | Meaning |
| --- | --- |
| Method separation | `GET`, `POST`, `PUT`, and `DELETE` logic can live in separate methods. |
| Reuse | Shared behavior can be inherited from parent classes. |
| Organization | Complex view logic can be grouped into a class. |
| Extensibility | Mixins can add focused behavior without rewriting the whole view. |

Class-based views use object-oriented programming ideas:

- **Inheritance** lets one view class reuse behavior from another class.
- **Mixins** are small reusable classes that add a specific capability.
- **Multiple inheritance** lets a view combine behavior from more than one parent class or mixin.

Common reusable actions in class-based and generic views:

| Action | Purpose |
| --- | --- |
| Create | Create a model instance |
| List | Display a queryset |
| Retrieve | Display one model instance |
| Update | Update a model instance |
| Delete | Delete a model instance |

Use mixins carefully. They can reduce duplication, but combining too many mixins can make the view harder to understand.

Key idea: class-based views are best when a view has multiple HTTP behaviors or reusable logic. Function-based views are still a good choice for simple views.

## 3. Models

### Models and Migrations

#### Models

Dynamic web applications need persistent data. Users submit information through the presentation layer, and the application often needs to store, retrieve, update, and delete that data later.

In Django, a **model** is the Python representation of stored data. It is the model part of the Model-View-Template, or MVT, pattern.

Key ideas:

- A model is the single source of truth for a type of data.
- A model usually maps to one database table.
- Each model attribute usually maps to one database field.
- A model is a Python class that subclasses `django.db.models.Model`.
- Django provides a database API so you can work with records using Python instead of writing SQL manually.

Example model:

```python
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
```

Django automatically adds a primary key field named `id` unless you define your own primary key.

Defining a model class does not create the database table by itself. To apply model changes to the database, Django uses migrations.

**SQL Compared With Django Models**

Without a framework, a developer may create database tables directly and write SQL queries such as `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.

With Django models, the same work is done through Python classes and model methods.

| Operation | SQL idea | Django model idea |
| --- | --- | --- |
| Create table | `CREATE TABLE` | Define a model, then run migrations |
| Create record | `INSERT` | Create an object and call `save()` |
| Read record | `SELECT` | Use model manager methods such as `objects.get()` |
| Update record | `UPDATE` | Get an object, change fields, then call `save()` |
| Delete record | `DELETE` | Get an object, then call `delete()` |

Example CRUD operations:

```python
# Create
user = User(first_name="John", last_name="Jones")
user.save()

# Read
user = User.objects.get(id=1)

# Update
user.last_name = "Smith"
user.save()

# Delete
user.delete()
```

The `objects` attribute is Django's default model manager. It provides methods for querying the database, such as `get()`, `filter()`, and `all()`.

Key idea: models let Django developers describe database structure and behavior in Python. They replace much of the manual SQL needed for common CRUD operations, while migrations handle turning model definitions into database tables.

#### Model Relationships

Model relationships describe how database tables connect to each other.

**Primary and Foreign Keys**

| Term | Meaning |
| --- | --- |
| Primary key | A field whose value uniquely identifies each row in a table. |
| Foreign key | A field in one table that points to the primary key of another table. |

Relationships help:

- avoid repeated data,
- reduce typing errors,
- keep related records consistent,
- protect data integrity when records are changed or deleted.

For example, instead of storing a full product name in every customer purchase row, a `Customer` or `Order` table can store a `product_id` foreign key that points to the matching product.

**Relationship Types**

| Relationship | Django field | Meaning |
| --- | --- | --- |
| One-to-one | `OneToOneField` | One record in model A matches one record in model B. |
| One-to-many | `ForeignKey` | One record in model A can match many records in model B. |
| Many-to-many | `ManyToManyField` | Many records in model A can match many records in model B. |

**`on_delete`**

Relationship fields such as `ForeignKey` and `OneToOneField` require an `on_delete` option. It tells Django what to do when the referenced object is deleted.

| Option | Behavior |
| --- | --- |
| `models.CASCADE` | Delete the related object too. |
| `models.PROTECT` | Prevent deletion of the referenced object. |
| `models.RESTRICT` | Prevent deletion by raising `RestrictedError` when restricted related objects exist. |

**One-To-One**

A one-to-one relationship is useful when one object should have exactly one matching object.

Example: one college has one principal, and one principal belongs to one college.

```python
from django.db import models


class College(models.Model):
    college_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website = models.URLField()


class Principal(models.Model):
    college = models.OneToOneField(College, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
```

After migrations, Django creates a unique relationship from `Principal` to `College`, so each college can be linked to only one principal.

Equivalent SQL shape:

```sql
CREATE TABLE "myapp_college" (
    "college_id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "strength" integer NOT NULL,
    "website" varchar(200) NOT NULL
);

CREATE TABLE "myapp_principal" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "qualification" varchar(50) NOT NULL,
    "email" varchar(50) NOT NULL,
    "college_id" integer NOT NULL UNIQUE
        REFERENCES "myapp_college" ("college_id")
        DEFERRABLE INITIALLY DEFERRED
);
```

**One-To-Many**

A one-to-many relationship is useful when one object can be connected to many objects.

Example: one subject can be taught by many teachers.

```python
from django.db import models


class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
```

After migrations, Django creates a foreign key column on the `Teacher` table that references the `Subject` table.

Equivalent SQL shape:

```sql
CREATE TABLE "myapp_subject" (
    "subject_code" integer NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL,
    "credits" integer NOT NULL
);

CREATE TABLE "myapp_teacher" (
    "teacher_id" integer NOT NULL PRIMARY KEY,
    "qualification" varchar(50) NOT NULL,
    "email" varchar(50) NOT NULL,
    "subject_id" integer NOT NULL
        REFERENCES "myapp_subject" ("subject_code")
        DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "myapp_teacher_subject_id_idx"
    ON "myapp_teacher" ("subject_id");
```

**Many-To-Many**

A many-to-many relationship is useful when many objects on each side can connect to many objects on the other side.

Example: one teacher can teach many subjects, and one subject can be taught by many teachers.

```python
from django.db import models


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()
    teachers = models.ManyToManyField(Teacher)
```

After migrations, Django creates an extra join table between `Subject` and `Teacher`. That join table stores pairs of subject IDs and teacher IDs.

Equivalent SQL shape:

```sql
CREATE TABLE "myapp_teacher" (
    "teacher_id" integer NOT NULL PRIMARY KEY,
    "qualification" varchar(50) NOT NULL,
    "email" varchar(50) NOT NULL
);

CREATE TABLE "myapp_subject" (
    "subject_code" integer NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL,
    "credits" integer NOT NULL
);

CREATE TABLE "myapp_subject_teachers" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "subject_id" integer NOT NULL
        REFERENCES "myapp_subject" ("subject_code")
        DEFERRABLE INITIALLY DEFERRED,
    "teacher_id" integer NOT NULL
        REFERENCES "myapp_teacher" ("teacher_id")
        DEFERRABLE INITIALLY DEFERRED
);

CREATE UNIQUE INDEX "myapp_subject_teachers_subject_id_teacher_id_uniq"
    ON "myapp_subject_teachers" ("subject_id", "teacher_id");

CREATE INDEX "myapp_subject_teachers_subject_id_idx"
    ON "myapp_subject_teachers" ("subject_id");

CREATE INDEX "myapp_subject_teachers_teacher_id_idx"
    ON "myapp_subject_teachers" ("teacher_id");
```

Key idea: Django model relationships let Python classes express relational database links. Migrations turn fields such as `OneToOneField`, `ForeignKey`, and `ManyToManyField` into the needed database constraints and join tables.

#### Creating Models

Models are created in an app's `models.py` file. This demo uses a Little Lemon menu example inside an app named `menuapp`.

**Create the Model**

A model class inherits from `models.Model`. Each class attribute defines a database field.

```python
# menuapp/models.py
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
```

Field examples from the demo:

| Field | Use |
| --- | --- |
| `CharField(max_length=100)` | Stores text values such as item names and cuisine types. |
| `IntegerField()` | Stores whole numbers such as a price. |

The `__str__()` method controls how model objects display in the shell, admin, and query results. Without it, Django shows generic labels such as `Menu object (1)`.

**Register the App**

Before Django can use the model, the app must be listed in `INSTALLED_APPS`.

```python
# settings.py

INSTALLED_APPS = [
    # ...
    "menuapp",
]
```

If the app is not installed, importing the model in the Django shell can fail because Django has not loaded the app into the project.

**Create and Apply Migrations**

After defining the model, create a migration and apply it:

```bash
python manage.py makemigrations
python manage.py migrate
# Then, start the server, if desired:
python manage.py runserver 8080
```

`makemigrations` creates a Python migration file that describes the database changes. `migrate` applies those changes to the database, creating the table and columns.

**Use the Django Shell**

Open the Django shell:

```bash
python manage.py shell
```

Import the model:

```python
from menuapp.models import Menu
```

Check existing records:

```python
Menu.objects.all()
```

At first, this returns an empty `QuerySet` if no menu items exist.

**Create Records**

Create a menu item:

```python
menu_item = Menu.objects.create(
    name="Pasta",
    cuisine="Italian",
    price=10,
)
```

`objects.create()` creates and saves the record in one step.

You can then query again:

```python
Menu.objects.all()
```

**Update Records**

Retrieve a record, change an attribute, and save it:

```python
menu_item = Menu.objects.get(pk=1)
menu_item.cuisine = "Mediterranean"
menu_item.save()
```

This works like normal Python object manipulation, but `save()` persists the change to the database.

**Other Ways to Work With Data**

The demo uses the Django shell to show how model operations work internally. Later, the same data can also be viewed and updated through the Django admin interface.

Key idea: creating a model is only the first step. To use it fully, add the app to `INSTALLED_APPS`, run migrations, then interact with records through Django's model manager, usually `objects`.

#### Migrations

Django models describe the intended database schema in Python. When a model changes, a **migration** records the operations needed to bring the actual database schema into sync.

For example, adding a `city` field to a model requires adding a matching column to its database table. Django generates and applies the required schema change, so developers usually do not need to write an `ALTER TABLE` statement manually.

**Migration Workflow**

1. Change a model by adding, renaming, or removing fields or models.
2. Generate a migration file:

```bash
python manage.py makemigrations
```

3. Review the generated migration in the app's `migrations/` directory.
4. Apply pending migrations to the database:

```bash
python manage.py migrate
```

Migration files are Python files that describe ordered database operations. They should be committed to version control so every developer and deployment environment can apply the same schema changes.

**Schema Change Example**

Suppose the application needs to store each user's city. First, add the field to the Django model:

```python
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
```

Then generate and apply the migration:

```bash
# Generate and apply the migration
python manage.py makemigrations  # Automatically creates a file <seq_num>_<descriptive_name>.py
python manage.py migrate
```

Conceptually, Django performs a database operation similar to this SQL:

```sql
ALTER TABLE app_user
ADD COLUMN city VARCHAR(100) NOT NULL DEFAULT '';
```

The exact SQL varies by database backend. To inspect the SQL Django plans to run for a migration, use:

```bash
# Check the SQL applied in the background for a specific migration
# 0002 refers to the migration file created for the city field change: 0002_add_city.py
python manage.py sqlmigrate app 0002
```

**ORM and SQL Data Operations**

Migrations change the database **schema**. After the schema exists, Django's ORM reads and changes the **data** stored in it.

Create a user:

```python
# Django ORM
User.objects.create(name="Ada", city="London")
```

```sql
-- Equivalent SQL
INSERT INTO app_user (name, city)
VALUES ('Ada', 'London');
```

Query users from London:

```python
# Django ORM
User.objects.filter(city="London")
```

```sql
-- Equivalent SQL
SELECT *
FROM app_user
WHERE city = 'London';
```

Update Ada's city:

```python
# Django ORM
User.objects.filter(name="Ada").update(city="Paris")
```

```sql
-- Equivalent SQL
UPDATE app_user
SET city = 'Paris'
WHERE name = 'Ada';
```

**Why Use Migrations?**

| Benefit | Explanation |
| --- | --- |
| Schema synchronization | Keeps the database structure aligned with Django models. |
| Version history | Records how the schema changed over time. |
| Team consistency | Lets each developer update their local database with the same operations. |
| Easier maintenance | Keeps schema changes in the codebase instead of relying on manually executed SQL. |

Think of migrations as version control for the database schema: models describe the desired structure, migration files record the changes, and `migrate` applies them.

#### Note about Database Connection

- Django gets its database connection settings from the `DATABASES` dictionary in `settings.py`.
  - The `"default"` entry is the main database connection used by the project.
  - The `"ENGINE"` value tells Django which database backend to use.
  - The `"NAME"` value identifies the database name or database file.
- A new Django project uses SQLite by default.
  - SQLite stores the whole database in one local file.
  - The default database file is usually named `db.sqlite3`.
  - With the default project setup, Django creates this file at `BASE_DIR / "db.sqlite3"`.
  - `BASE_DIR` points to the folder that contains `manage.py`.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

- The SQLite database file is created when migrations are applied.
  - Running `migrate` creates the database file if it does not already exist.
  - It also creates the tables required by installed Django apps.
  - Built-in apps can create tables for admin, authentication, sessions, and content types.

```bash
python manage.py migrate
# Then, start the server, if desired:
python manage.py runserver 8080
```

- Other databases use the same `DATABASES` setting but require connection details.
  - MySQL commonly uses `django.db.backends.mysql`.
  - PostgreSQL commonly uses `django.db.backends.postgresql`.
  - Server-based databases usually need a database name, user, password, host, and port.

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

- Key idea: migrations create or update the schema inside the database that `settings.py` points to.
  - For SQLite, Django can create the local `db.sqlite3` file automatically.
  - For MySQL or PostgreSQL, the database server and database usually need to exist before Django can connect and run migrations.

#### How to Use Migrations

Django's migration system turns model changes into versioned database-schema operations.

| Command | Purpose |
| --- | --- |
| `makemigrations` | Detect model changes and create migration files. |
| `migrate` | Apply or unapply migrations. |
| `showmigrations` | Show which migrations are applied or pending. |
| `sqlmigrate` | Display the SQL for a migration without executing it. |

**Apply Initial Migrations**

A new Django project includes apps such as `auth`, `admin`, and `sessions` in `INSTALLED_APPS`. Apply their existing migrations to create the required database tables:

```bash
python manage.py migrate
```

**Create an App and Model**

Create an app:

```bash
python manage.py startapp myapp
```

Add the app to `INSTALLED_APPS`, then define a model in `myapp/models.py`:

```python
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
```

**Create a Migration**

Generate a migration after changing a model:

```bash
# Generate a migration for the new Person model
# Automatically creates a file <seq_num>_<descriptive_name>.py
python manage.py makemigrations myapp
# To specify a custom name for the migration, use:
python manage.py makemigrations myapp --name initial_person
```

Example output:

```text
Migrations for 'myapp':
  myapp/migrations/0001_initial.py
    + Create model Person
```

Django creates a migration file containing operations similar to:

```python
class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(primary_key=True)),
                ("name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
            ],
        ),
    ]
```

Review generated migrations before applying them, especially after renaming or deleting fields.

**Inspect and Apply the Migration**

Inspect the SQL without changing the database:

```bash
# Check the SQL applied in the background for a specific migration
# 0001 refers to the migration file created for the initial Person model: 0001_initial.py
python manage.py sqlmigrate myapp 0001
```

The output will contain backend-specific SQL similar to:

```sql
CREATE TABLE "myapp_person" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(20) NOT NULL,
    "email" varchar(254) NOT NULL,
    "phone" varchar(20) NOT NULL
);
```

`sqlmigrate` is optional. Run it before `migrate` when you want to review the generated SQL; it can also be run afterward because it only reads the migration file.

Apply the migration:

```bash
# Apply the migration to create the Person table in the database
python manage.py migrate
```

**Change an Existing Model**

Add another field:

```python
class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # New field added after the initial migration
    age = models.PositiveIntegerField(null=True, blank=True)
```

Create the next migration:

```bash
# Automatically creates a file <seq_num>_<descriptive_name>.py
python manage.py makemigrations myapp
# To specify a custom name for the migration, use:
# python manage.py makemigrations myapp --name add_age_to_person
```

This produces a new migration such as `0002_person_age.py`. Existing migration files remain unchanged, preserving the schema history.

**Check Migration Status**

```bash
python manage.py showmigrations myapp
```

Example output:

```text
myapp
 [X] 0001_initial
 [ ] 0002_person_age
```

- `[X]` means the migration is applied.
- `[ ]` means the migration is pending.

Apply pending migrations with `python manage.py migrate`.

**Move Back to an Earlier Migration**

Target an earlier migration to unapply every later migration for that app:

```bash
python manage.py migrate myapp 0001
```

To unapply every migration for the app:

```bash
python manage.py migrate myapp zero
```

Rolling back a migration can remove columns or tables and may destroy data. Check the migration operations and create a backup before doing this with important databases.

**Recommended Workflow**

```bash
python manage.py makemigrations myapp
python manage.py showmigrations myapp
python manage.py sqlmigrate myapp 0002  # Optional inspection
python manage.py migrate
# Then, start the server, if desired:
python manage.py runserver 8080
```

Commit model changes and their generated migration files together so every environment can reproduce the same database schema.

#### Excurs: Registering Models in admin.py

- Optional: Register a model in `admin.py` when it should be manageable through the Django Admin interface.
  - The admin interface lets authorized users create, view, update, and delete model records in the browser.
  - Registered models appear in the `/admin/` site after the admin app is enabled and a superuser can log in.
- Admin registration is not required for database table creation.
  - Tables are created from models and migrations.
  - The app must be listed in `INSTALLED_APPS`.
  - The migrations must be created with `makemigrations` and applied with `migrate`.
- Admin registration is not required for normal ORM queries.
  - Code can use `Drinks.objects.all()` or `Drinks.objects.create(...)` without registering `Drinks` in `admin.py`.
  - Registration only affects whether the model appears in Django Admin.

```python
from django.contrib import admin

from .models import Drinks


admin.site.register(Drinks)
```

- Key distinction:
  - Need a database table: define the model and run migrations.
  - Need to query the model in Python: define the model and use the ORM.
  - Need browser-based admin management: register the model in `admin.py`.

#### Example: Working with Migrations

Before creating migrations, ensure the app is listed in `INSTALLED_APPS`. Django only detects model changes from installed apps.

**Creating and Applying Changes**

The two core commands have different responsibilities:

```bash
python manage.py makemigrations myapp
python manage.py migrate
# Then, start the server, if desired:
python manage.py runserver 8080
```

- `makemigrations` compares the current models with the recorded migration state and creates new migration files. It does not change the database.
- `migrate` executes pending migration operations and changes the database schema.

Each detected change creates another migration in the app's `migrations/` directory:

```text
myapp/migrations/
├── 0001_initial.py
├── 0002_rename_course_menuitem_category.py
└── 0003_rename_name_menuitem_item_name.py
```

These files form an ordered history. The filenames describe the operations, while each migration's `dependencies` define its actual position in the history.

**Renaming Fields**

When a field name changes, Django may ask whether it was renamed:

```text
Was menuitem.course renamed to menuitem.category (a CharField)? [y/N]
```

Confirming creates a `RenameField` operation that preserves existing column data. Rejecting it may cause Django to treat the change as deleting one field and adding another, which can lose data.

Always review rename prompts and the generated migration before applying it.

**Checking Progress**

Use `showmigrations` to compare migration files with the migrations recorded as applied in the database:

```bash
python manage.py showmigrations myapp
```

```text
myapp
 [X] 0001_initial
 [X] 0002_rename_course_menuitem_category
 [ ] 0003_rename_name_menuitem_item_name
```

`[X]` means applied; `[ ]` means pending.

**Previewing and Reversing Migrations**

Before moving an app back to an earlier migration, preview the operations:

```bash
python manage.py migrate myapp 0001 --plan
```

The command lists which later migrations Django would unapply without changing the database. Remove `--plan` to perform the rollback:

```bash
python manage.py migrate myapp 0001
```

Rolling back changes the database schema, but it does not rewrite the current model classes. Update the models separately if the code must match the older schema.

**Inspecting Generated SQL**

Use `sqlmigrate` to inspect the backend-specific SQL represented by one migration:

```bash
python manage.py sqlmigrate myapp 0003
```

For a field rename, the output may include an `ALTER TABLE` statement. This command only displays SQL; it does not apply or unapply the migration.

Key idea: model edits describe the desired schema, `makemigrations` records the transition, and `migrate` moves the database through that versioned history.

#### A History of Changes

- Django migrations provide a versioned history of database-schema changes.
  - Models describe the desired database structure in Python code.
  - Migration files record how the database schema should change over time.
  - The database can then be updated without manually writing repeated SQL statements.
- Migration history is useful because web application requirements often change in small steps.
  - A model may need a new field.
  - A field may need to be renamed.
  - A model or table may need to be removed.
  - The same schema changes may need to run on several databases or environments.
- Migrations support Django's DRY (don't repeat yourself) principle.
  - Developers make the change once in the model.
  - Django generates a migration from that model change.
  - The migration can be shared through version control and applied consistently.
- Migration files live inside each app's `migrations/` folder.
  - Files use an ordered numeric prefix such as `0001`, `0002`, and `0003`.
  - File names often describe the operation, such as an initial model creation or a field rename.
  - Existing migration files remain as the schema history for the app.

```text
myapp/
  migrations/
    0001_initial.py
    0002_add_customer_city.py
    0003_rename_name_customer_full_name.py
```

- `makemigrations` creates migration files from model changes.
  - It detects changes in installed apps.
  - It writes Python migration files.
  - It does not change the database by itself.
- `migrate` applies unapplied migrations to the database.
  - It synchronizes the database schema with the migration history.
  - It can apply migrations for all apps.
  - It can also target a specific app.

```bash
python manage.py makemigrations myapp
python manage.py migrate
```

- `showmigrations` displays which migrations Django knows about.
  - `[X]` means the migration has already been applied.
  - `[ ]` means the migration exists but is still pending.

```bash
python manage.py showmigrations myapp
```

```text
myapp
 [X] 0001_initial
 [X] 0002_add_customer_city
 [ ] 0003_rename_name_customer_full_name
```

- Django tracks applied migrations in the `django_migrations` database table.
  - `id` stores an auto-incremented row identifier.
  - `app` stores the app that owns the migration.
  - `name` stores the migration file name without `.py`.
  - `applied` stores the timestamp when the migration was applied.
  - Django checks this table before running migrations.
  - Already-applied migrations are not applied again to the same database.
- Migration files are Python files with a `Migration` class.
  - `dependencies` list migrations that must run first.
  - `operations` list schema actions Django should perform.

```python
class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="city",
            field=models.CharField(max_length=100, default=""),
        ),
    ]
```

- Common migration operations describe database-schema changes.
  - `CreateModel` creates a model and its database table.
  - `DeleteModel` deletes a model and drops its database table.
  - `AddField` adds a model field and database column.
  - `AlterField` changes a field definition and matching database column.
  - `AddIndex` creates a database index.
- `sqlmigrate` shows the SQL for a specific migration without applying it.
  - It helps inspect what Django plans to run.
  - The exact SQL can differ by database backend.

```bash
python manage.py sqlmigrate myapp 0003
```

- Key idea: migrations are Django's database-schema timeline.
  - Models describe the intended structure.
  - Migration files record each schema change.
  - The `django_migrations` table records which changes have already been applied.

#### Excurs: What are Database Indices?

  - A database index is a helper structure that makes lookups faster.
  - It works like an index at the back of a book.
    - Without an index, the database may need to scan many rows.
    - With an index, the database can often jump to matching rows more quickly.
  - Indexes are useful for columns that are often used in filtering, sorting, or joins.
  - `AddIndex` is the Django migration operation that creates an index in the database.
  - Indexes have a tradeoff.
    - They can make read queries faster.
    - They use extra storage.
    - They can make inserts, updates, and deletes slightly slower because the index must also be updated.

```python
class Customer(models.Model):
    email = models.EmailField()

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
        ]
```

```python
migrations.AddIndex(
    model_name="customer",
    index=models.Index(fields=["email"], name="customer_email_idx"),
)
```

#### Exercise: Models and Migrations

Folder: [`lab/05-django-models/`](./lab/05-django-models/)

- Completed the model and migration-file parts of the lab.
  - Created a `Drinks` model in `myapp/models.py`.
  - Added the required `price` field.
  - Created the initial `drink` field first, then renamed it to `drink_name`.
  - Registered the `Drinks` model in `myapp/admin.py`.
  - Added the missing `migrations/__init__.py` file.
  - Created `0001_initial.py` for the initial `Drinks` table.
  - Created `0002_rename_drink_drinks_drink_name.py` for the field rename.
- Verified the migration state without applying the database changes.
  - `python manage.py makemigrations --check --dry-run` reported `No changes detected`.
  - `python manage.py showmigrations myapp` showed both app migrations as pending.
  - Applying migrations with SQLite failed in this lab folder with `disk I/O error`, so no final `db.sqlite3` artifact was kept.

Solution code for `models.py` before the initial migration:

```python
from django.db import models


# Create your models here.
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
```

Solution code for `models.py` before the second migration:

```python
from django.db import models


# Create your models here.
class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
```

Solution code for `admin.py`:

```python
from django.contrib import admin

from .models import Drinks


# Register your models here.
admin.site.register(Drinks)
```

Commands to perform the migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Commands used to verify the migration files in this lab:

```bash
python manage.py makemigrations --check --dry-run
python manage.py showmigrations myapp
```

#### Models and Foreign Keys

- A foreign key creates a relationship between two database tables.
  - In Django, `models.ForeignKey` defines a many-to-one relationship.
  - Many records in one model can point to one record in another model.
  - The foreign key is stored as a database column containing the related row's primary key.
- The Little Lemon menu example uses categories and menu items.
  - One cuisine category can contain many menu items.
  - Each menu item belongs to one category.
  - This is a one-to-many relationship from category to menu items.
- The example needs two models.
  - `MenuCategory` stores category names such as Italian, Greek, and Turkish.
  - `Menu` stores menu item names, prices, and a reference to a category.
- `ForeignKey` needs the related model and an `on_delete` rule.
  - The related model tells Django which table to connect to.
  - `on_delete=models.PROTECT` prevents deleting a category while menu items still reference it.
  - `null=True` and `default=None` allow existing or empty menu rows to have no category during setup.
- The database stores the relationship through an ID column.
  - A menu item can store the ID of its related category.
  - If Greek has ID `2`, a Greek salad row can reference category ID `2`.
  - Django uses the ID internally while the ORM lets Python code work with related objects.
- `related_name` names the reverse relationship in the ORM.
  - It does not change the database column into readable category text.
  - It lets a category access its related menu items through a clearer attribute.
  - For example, `category.menu_items.all()` can return all menu items in that category.
- The models must still follow the normal migration workflow.
  - Add or change the models in `models.py`.
  - Register models in `admin.py` only if they should appear in Django Admin.
  - Run `makemigrations` to create migration files.
  - Run `migrate` to apply the schema changes to the database.

File: `myapp/models.py`

```python
from django.db import models


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.menu_category_name


class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(
        # Connect each Menu row to one MenuCategory row.
        MenuCategory,

        # Prevent deleting a category while menu items still reference it.
        on_delete=models.PROTECT,

        # Allow the category field to be empty in the database.
        null=True,

        # Use no category as the default value when one is not provided.
        default=None,

        # Give MenuCategory a clear reverse lookup: category.menu_items.all().
        related_name="menu_items",
    )

    def __str__(self):
        return self.menu_item


# Example MenuCategory instance:
# greek = MenuCategory.objects.create(menu_category_name="Greek")
#
# Example Menu instance linked to that category:
# Menu.objects.create(menu_item="Greek salad", price=12, category=greek)
```

File: `myapp/admin.py`

```python
from django.contrib import admin

from .models import Menu, MenuCategory


admin.site.register(Menu)
admin.site.register(MenuCategory)
```

Run from the project folder that contains `manage.py`:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Exercise: Models and Foreign Keys

Folder: [`lab/06-django-foreign-keys/`](./lab/06-django-foreign-keys/)

- Completed the model and migration-file parts of the lab.
  - Created a `DrinksCategory` model for drink categories.
  - Created a `Drinks` model for individual drinks.
  - Added a `ForeignKey` from `Drinks` to `DrinksCategory`.
  - Used `on_delete=models.PROTECT` to prevent deleting a category that still has drinks.
  - Registered both models in `admin.py`.
  - Added `migrations/__init__.py`.
  - Created `0001_initial.py`, which creates both database tables and the foreign key relationship.
- Verified the migration state without applying the database changes.
  - `python manage.py makemigrations --check --dry-run` reported `No changes detected`.
  - `python manage.py showmigrations myapp` showed `0001_initial` as pending.
  - `python manage.py migrate` failed in this lab folder with a SQLite `disk I/O error`, so the migration should be run manually from a normal terminal.

File: `myapp/models.py`

```python
from django.db import models

# Create your models here.
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)
```

File: `myapp/admin.py`

```python
from django.contrib import admin
from .models import Drinks
from .models import DrinksCategory

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
```

Run from the project folder that contains `manage.py`:

```bash
cd 03_Django/lab/06-django-foreign-keys/myproject

python3 manage.py makemigrations

python3 manage.py migrate
```

Use the Django shell to create example records:

```bash
# Open the Django shell from the folder that contains manage.py.
python manage.py shell
```

```python
# Import both models.
from myapp.models import Drinks, DrinksCategory

# Create and save a drink category.
cat = DrinksCategory(category_name="coffee")
cat.save()

# Retrieve the category so it can be used as a foreign key.
fk = DrinksCategory.objects.get(pk=1)

# Create and save a drink linked to the category.
drink = Drinks(drink="mocha", price=7, category_id=fk)
drink.save()

# Optional checks.
DrinksCategory.objects.all()
Drinks.objects.all()
```

#### ORM: Object Relationship Mapping

##### What Is ORM?

Object Relational Mapping (ORM) lets object-oriented code interact with a relational database.

- Python applications work with objects.
  - Objects can contain non-scalar values and relationships.
  - They are not always represented directly as primitive values such as integers and strings.
- Relational databases store data in tables.
  - Tables are made of rows and columns.
  - Column values are usually scalar database types such as integers, strings, dates, and booleans.
- The program needs a translation layer between Python objects and database tables.
  - ORM maps Python classes to database tables.
  - ORM maps class attributes to database fields.
  - ORM lets developers perform database operations without writing raw Structured Query Language (SQL) for every query.

With ORM, developers can focus more on application logic and less on repetitive database-access code.

##### Django Models And ORM

Django has its own ORM layer.

- Each Django model is a Python class that subclasses `django.db.models.Model`.
- Each model attribute usually represents a database field.
- Django migrations propagate model definitions into database tables.
- Models help developers perform CRUD operations.
  - Create records.
  - Read records.
  - Update records.
  - Delete records.

To retrieve objects from the database, Django uses a model manager, usually available as `objects`, to construct a `QuerySet`.

##### QuerySet Example

The following example uses an app named `demoapp`.

File: `demoapp/models.py`

```python
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)


class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="vehicles",
    )
```

This creates two related tables:

- `Customer`
  - Stores customer records.
- `Vehicle`
  - Stores vehicle records.
  - References `Customer` with a foreign key.
  - Creates a one-to-many relationship because one customer can have many vehicles.

Apply migrations so Django creates the corresponding database tables.

##### Open The Django Shell

Open the interactive Django shell from the project folder that contains `manage.py`.

The command is the same idea on Windows, macOS, and Linux.

```bash
python manage.py shell
```

##### Create A Model Object With `save()`

Create an object of the `Customer` class and save it to the database.

```python
from demoapp.models import Customer

c = Customer(name="Henry")
c.save()
```

The `save()` method creates a row in the mapped `Customer` table.

##### Add A Model Object With `objects.create()`

`Customer.objects` is the model manager.

- The manager exposes the query API for the model.
- It can create, retrieve, update, and delete database records.
- `objects.create()` creates and saves a row in one step.
- In SQL terms, it performs an `INSERT`.

```python
Customer.objects.create(name="Hameed")
```

##### Create Related `Vehicle` Objects

The `Vehicle.customer` field expects a `Customer` object because it is a `ForeignKey`.

Fetch the customer with primary key `2`.

```python
from demoapp.models import Customer, Vehicle

c = Customer.objects.get(pk=2)
c.name
```

Expected value:

```text
'Hameed'
```

Use that customer object as the `customer` value on new vehicles.

```python
v = Vehicle(name="Honda", customer=c)
v.save()

v = Vehicle(name="Toyota", customer=c)
v.save()
```

Add two vehicles for the customer named `Henry`.

```python
c = Customer.objects.get(name="Henry")

Vehicle.objects.create(name="Ford", customer=c)
Vehicle.objects.create(name="Nissan", customer=c)
```

##### Fetch Model Objects

A `QuerySet` represents a collection of database objects.

- It usually represents a `SELECT` query.
- It can be filtered before Django evaluates it.
- It can be iterated over like a normal Python collection.

Use `all()` to fetch every object for a model.

```python
model.objects.all()
```

Example:

```python
lst = Customer.objects.all()
[c.name for c in lst]
```

Expected result:

```text
['Henry', 'Hameed']
```

##### Filter Model Objects

Use `filter()` to retrieve objects that match criteria.

- In SQL terms, this is similar to adding a `WHERE` clause.
- Django field lookups use double underscores, such as `name__startswith`.

```python
model.objects.filter(criteria)
```

Example:

```python
mydata = Customer.objects.filter(name__startswith="H")
```

##### Access Related Objects

`Vehicle` objects can access their related `Customer` objects through the foreign key attribute.

```python
lst = Vehicle.objects.all()

for v in lst:
    print(v.name, ":", v.customer.name)
```

Expected output:

```text
Honda : Hameed
Toyota : Hameed
Ford : Henry
Nissan : Henry
```

##### Update A Model Object

To update a record:

- Fetch the object.
- Change an attribute.
- Call `save()`.

```python
c = Customer.objects.get(name="Henry")
c.name = "Helen"
c.save()
```

##### Delete A Model Object

Use `delete()` to remove the database row represented by an object.

```python
c = Customer.objects.get(pk=4)
c.delete()
```

Example return value:

```text
(1, {'demoapp.Customer': 1})
```

Key idea: Django's ORM and `QuerySet` API let developers perform CRUD operations on database tables through Python objects instead of writing raw SQL queries.

#### Using ORM

- This section adds a Little Lemon reservation example to the earlier ORM overview.
  - The earlier section already covered ORM basics, managers, `QuerySet`, `all()`, `get()`, `filter()`, `save()`, and `delete()`.
  - The new focus here is how QuerySet API calls map to common SQL-style query logic.
- Django's QuerySet API supports several kinds of operations.
  - Methods that return new querysets, such as `filter()`.
  - Operators that return new querysets, such as combining querysets with `&`.
  - Methods that return something other than a queryset, such as `get()`.
- The Little Lemon example uses a `Customer` model for restaurant reservations.
  - `name` stores the customer name.
  - `reservation_day` stores the day of the reservation.
  - `seats` stores the number of requested seats.
  - The model has already been migrated and the database already contains entries.
- `get()` retrieves one matching object instead of returning a queryset.
  - It is useful when the query should match exactly one row.
  - It is similar to selecting a specific row in Structured Query Language (SQL).
  - `Customer.objects.get(id=4)` returns the customer with ID `4`.
- `filter()` returns a new queryset.
  - It is useful when zero, one, or many rows may match.
  - It is similar to adding a SQL `WHERE` clause.
  - `Customer.objects.filter(reservation_day="Saturday")` returns Saturday reservations.
- Chained `filter()` calls combine conditions with SQL-style `AND` logic.
  - Each filter narrows the previous queryset.
  - The result contains only rows that satisfy every condition.
  - `Customer.objects.filter(reservation_day="Friday").filter(seats=4)` returns Friday reservations for four seats.
- The QuerySet API is broad.
  - Simple lookup methods are only the beginning.
  - More advanced queries can use additional queryset methods, operators, and lookup expressions.

File: `myapp/models.py`

```python
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()
```

Run from the project folder that contains `manage.py`:

```bash
# Open the Django shell.
python3 manage.py shell
```

Use the Django shell to query reservation data:

```python
# Import the model before querying it.
from myapp.models import Customer

# Return one object with the exact ID.
Customer.objects.get(id=4)

# Return all Saturday reservations as a QuerySet.
Customer.objects.filter(reservation_day="Saturday")

# Return only Friday reservations for four seats.
Customer.objects.filter(reservation_day="Friday").filter(seats=4)
```

#### Additional Resources

- [Models - official documentation](https://docs.djangoproject.com/en/4.1/topics/db/models/)
- [Migrations - official documentation](https://docs.djangoproject.com/en/4.1/topics/migrations/)
- [Other Model Instance methods (including the String Dunder method)](https://docs.djangoproject.com/en/dev/ref/models/instances/#model-instance-methods)
- [Using Models - Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
- [Detailed overview of Migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/)
- [Migration operations](https://docs.djangoproject.com/en/4.1/ref/migration-operations/)
- [Understanding ORM](https://docs.djangoproject.com/en/4.1/ref/models/class/)

### Models and Forms

#### Forms

- Web applications often need to collect data from end users.
  - Login and authentication forms collect user credentials.
  - Registration forms collect new account details.
  - Shopping and ordering forms collect order information.
- HTML forms send user input to the server for processing.
  - Form fields can include text inputs, checkboxes, and submit buttons.
  - Submitted form data is handled by server-side code.
  - In Django, common form submissions use a `POST` request with data in the request body.
- A basic HTML form uses `action` and `method`.
  - `action` defines which view receives the submitted form.
  - `method="post"` sends the form data in the request body.
  - A text input can collect a user's name.
  - A submit input can display a button such as `Send name`.
- Handwritten HTML forms can become hard to maintain.
  - Large forms can contain many fields and conditional flows.
  - Field `name` and `id` attributes must match what the backend expects.
  - Mismatches between the form and server-side code can cause processing errors.
- Django provides a `Form` class to define expected form fields in Python.
  - The class represents the data expected in the request.
  - Django can render the matching form fields as HTML.
  - Field definitions can include validation rules such as `max_length`.
  - The form class helps keep input names and backend processing aligned.
- A Django form renders fields, labels, and validation-related attributes.
  - It does not automatically render the surrounding `<form>` tag.
  - It does not automatically render the submit button.
  - The template must include the `<form>` element and place the rendered fields inside it.
- The form class is connected to `{{ form }}` through the view.
  - `forms.py` defines the form class.
  - `views.py` creates a form instance.
  - The view passes the form instance into the template context.
  - The template renders the context variable with `{{ form }}`.
- Form classes make changes easier to manage.
  - Developers update the Python class instead of manually syncing many HTML inputs.
  - Forms can benefit from object-oriented programming patterns.
  - Complex forms can be split into smaller subclasses when needed.
- Django can also generate forms from models.
  - Submitted data often needs to be persisted in a database.
  - Models define the database structure for stored information.
  - Model-backed forms help align collected input with fields that need to be saved.
  - This reduces errors caused by form fields and database fields drifting apart.
  - Model form code is commonly placed in `forms.py`.

File: `templates/order.html`

```html
<!-- Basic HTML form that sends a POST request to the order view. -->
<form action="/order/" method="post">
    <label for="your_name">Your name:</label>
    <input id="your_name" type="text" name="your_name">
    <input type="submit" value="Send name">
</form>
```

File: `forms.py`

```python
from django import forms


class NameForm(forms.Form):
    # CharField represents a text input and validates max_length.
    your_name = forms.CharField(max_length=100)
```

File: `views.py`

```python
from django.shortcuts import render

from .forms import NameForm


def order(request):
    # Create a form instance from the form class.
    form = NameForm()

    # Pass the form instance into the template context as "form".
    return render(request, "order.html", {"form": form})
```

Rendered field HTML and template usage in `templates/order.html`:

```html
<!-- Django renders fields such as labels and inputs. -->
<label for="id_your_name">Your name:</label>
<input type="text" name="your_name" maxlength="100" required id="id_your_name">

<!-- The surrounding form tag and submit button still belong in the template. -->
<form action="/order/" method="post">
    {% csrf_token %} <!--  Django's protection against CSRF (Cross-Site Request Forgery) attacks -->
    {{ form }}
    <input type="submit" value="Send name">
</form>
```

File: `forms.py`

```python
from django.forms import ModelForm

from myapp.models import Customer


class CustomerForm(ModelForm):
    # ModelForm generates form fields from selected model fields.
    class Meta:
        model = Customer
        fields = ["name", "email", "address"]
```

#### Django Forms

- Django forms use form fields to represent expected input types.
  - HTML forms collect input with elements such as text inputs, radio buttons, drop-down lists, and checkboxes.
  - Django's `Form` class defines the expected attributes that build and process a form.
  - Form fields are the building blocks inside a Django form class.
  - Each field helps define both the expected data type and the rendered HTML input.
- Different form fields handle different kinds of data.
  - `CharField` accepts string input and usually renders as a text input.
  - `EmailField` accepts email-formatted input and usually renders as an email input.
  - `IntegerField` accepts only integers and usually renders as a number input.
  - `MultipleChoiceField` lets users choose multiple options.
  - `FileField` lets users upload a file.
  - `DateField` can collect date values, often with a date-friendly widget.
  - `ChoiceField` lets users choose one value from predefined options.
- Form fields accept common arguments.
  - `required` controls whether the field must have a value.
    - Fields are required by default.
    - Use `required=False` to make a field optional.
  - `label` changes the label shown for the field.
  - `initial` sets a default initial value.
  - `help_text` adds descriptive guidance for the user.
- Widgets control how a form field is rendered in HTML.
  - A field defines the kind of data Django should accept.
  - A widget defines the HTML representation of that field.
  - `forms.Textarea` can render a `CharField` as a multi-line text area.
  - Widget attributes such as `attrs={"rows": 5}` can customize the generated HTML.
  - `forms.RadioSelect` can render choices as radio buttons instead of a drop-down list.
- Django form fields include basic validation.
  - `EmailField` rejects values that do not look like valid email addresses.
  - Field-specific validation helps catch incorrect input before backend processing continues.
  - Choosing the right field type is essential because each form has different data requirements.
- The Little Lemon examples show common form needs.
  - A customer form can collect a name and age.
  - A reservation form can collect a reservation date.
  - A menu preference form can collect a favorite dish.
  - Feedback and survey-style forms may need different field types and widgets.

File: `forms.py`

```python
from django import forms


FAVORITE_DISH_CHOICES = [
    ("pasta", "Pasta"),
    ("falafel", "Falafel"),
    ("cheesecake", "Cheesecake"),
]


class CustomerForm(forms.Form):
    # CharField accepts string input.
    name = forms.CharField(max_length=200, label="Customer name")

    # IntegerField accepts whole numbers.
    age = forms.IntegerField(required=False, help_text="Optional customer age.")

    # CharField can render as a multi-line textarea by overriding the widget.
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 5}),
    )

    # EmailField validates that the input looks like an email address.
    email = forms.EmailField(label="Enter an email address")

    # DateField can use a date-friendly HTML widget.
    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    # ChoiceField renders as a drop-down by default.
    favorite_dish = forms.ChoiceField(choices=FAVORITE_DISH_CHOICES)

    # The same choices can be rendered as radio buttons with RadioSelect.
    favorite_dish_radio = forms.ChoiceField(
        choices=FAVORITE_DISH_CHOICES,
        widget=forms.RadioSelect,
    )
```

#### Django Fields

##### Models And Database Tables

A Django model is a Python class that maps to a database table through Django's Object Relational Mapping (ORM) layer.

- Each model class usually subclasses `django.db.models.Model`.
- Each model attribute usually maps to a database table field.
- The Django ORM stores and retrieves data by using model methods instead of raw Structured Query Language (SQL).
- A model class is usually defined in the app's `models.py` file.

File: `myapp/models.py`

```python
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
```

After the app is added to `INSTALLED_APPS` and migrations are applied, Django creates a table for the model.

Example SQL shape:

```sql
CREATE TABLE myapp_person (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);
```

The `first_name` and `last_name` class attributes correspond to fields in the database table.

##### Table Names

Django automatically names model tables with the pattern `appname_modelname`.

- A `Person` model in an app named `myapp` becomes `myapp_person`.
- You can override the table name with `db_table` inside the model's `Meta` class.

```python
class Student(CommonInfo):
    # ...

    class Meta(CommonInfo.Meta):
        db_table = "student_info"
```

##### Model Fields And ModelForms

Choose a model field type that matches the data stored in the database column.

- Model field types are defined in `django.db.models`.
- Django can use model field information to generate forms through `ModelForm`.
- The field type helps Django choose the corresponding form field and widget.
  - For example, a model `CharField` can become a text input in a generated form.

##### Field Properties

A field can define common options in addition to field-specific options.

`primary_key`

- `primary_key=False` is the default.
- `primary_key=True` makes the field the table's primary key.
- If no primary key is defined, Django automatically adds an auto-incrementing primary key field.
- Only one field can be the primary key.

`default`

- `default` supplies a value when a new object is created.
- The default can be a fixed value or a callable.

```python
class Person(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80, default="Mumbai")
```

`unique`

- `unique=True` requires every row to have a different value for that field.
- This constraint is enforced by the database.

```python
tax_code = models.CharField(
    max_length=20,
    unique=True,
)
```

`choices`

- `choices` limits a field to predefined values.
- It is commonly rendered as a drop-down in forms.
- Each choice is a two-item pair.
  - The first value is stored in the database.
  - The second value is displayed to the user.

```python
SEMESTER_CHOICES = (
    ("1", "Civil"),
    ("2", "Electrical"),
    ("3", "Mechanical"),
    ("4", "CompSci"),
)


class Student(models.Model):
    semester = models.CharField(
        max_length=20,
        choices=SEMESTER_CHOICES,
        default="1",
    )
```

##### Field Types

The `django.db.models` module has many field types.

`CharField`

- Stores short string data.
- Requires `max_length`.
- Use `TextField` for longer text.

`IntegerField`

- Stores integer values.
- Related integer fields include `BigIntegerField`, `SmallIntegerField`, and auto-incrementing ID fields.

`FloatField` and `DecimalField`

- `FloatField` stores floating-point numbers.
- `DecimalField` stores fixed-precision decimal numbers.

```python
class Student(models.Model):
    grade = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
```

`DateTimeField` and `DateField`

- `DateTimeField` stores date and time values.
- `DateField` stores date-only values.

`EmailField`

- Stores email text.
- Adds built-in email validation.

`FileField`

- Stores uploaded file information.
- Uses `upload_to` to define the upload path.

`ImageField`

- Extends file handling for uploaded images.
- Validates that the uploaded file is an image.

`URLField`

- Stores URL text.
- Adds built-in URL validation.

##### Relationship Fields

Database models can have several relationship types.

- One-to-one.
- One-to-many.
- Many-to-many.

Django provides relationship fields for these model relationships.

##### `ForeignKey`

`ForeignKey` establishes a one-to-many relationship between two models.

- It requires the related model.
- It requires `on_delete` to define what happens when the referenced object is deleted.
- A common example is one customer having many vehicles.

```python
class Customer(models.Model):
    name = models.CharField(max_length=255)


class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="vehicles",
    )
```

`on_delete` controls deletion behavior.

- `models.CASCADE` deletes dependent objects when the referenced object is deleted.
- `models.PROTECT` prevents deletion of the referenced object while dependent objects still reference it.
- `models.RESTRICT` prevents deletion by raising `RestrictedError`, with special handling for objects deleted in the same operation through cascading relationships.

##### `on_delete=models.CASCADE`

Use `CASCADE` when dependent objects should be deleted with the referenced object.

- If a `Vehicle` belongs to a `Customer`, deleting the customer deletes the related vehicles.

##### `on_delete=models.PROTECT`

Use `PROTECT` when the referenced object must not be deleted while related objects exist.

- If a customer has vehicles, the customer cannot be deleted.
- Django raises `ProtectedError` when deletion is blocked.

##### `on_delete=models.RESTRICT`

Use `RESTRICT` when deletion should be blocked with `RestrictedError`, except in allowed cascading delete scenarios.

```python
class Artist(models.Model):
    name = models.CharField(max_length=10)


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)
```

Create example instances:

```python
artist1 = Artist.objects.create(name="Danny")
artist2 = Artist.objects.create(name="John")
album1 = Album.objects.create(artist=artist1)
album2 = Album.objects.create(artist=artist2)
song1 = Song.objects.create(artist=artist1, album=album1)
song2 = Song.objects.create(artist=artist1, album=album2)
```

In this setup:

- `artist1` can be deleted safely in the example scenario.
- Deleting `artist2` can raise `RestrictedError` because of the restricted album relationship.

##### `OneToOneField`

`OneToOneField` establishes a one-to-one relationship between two models.

- A `ForeignKey` with `unique=True` behaves similarly.
- The reverse side of a `OneToOneField` returns a single object.
- Example: one college can have only one principal, and one person can be principal of only one college.

```python
class College(models.Model):
    college_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website = models.URLField()


class Principal(models.Model):
    college = models.OneToOneField(
        College,
        on_delete=models.CASCADE,
    )
    qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
```

##### `ManyToManyField`

`ManyToManyField` establishes a many-to-many relationship between two models.

- Multiple objects of one model can relate to multiple objects of another model.
- Example: one subject can be taught by many teachers, and one teacher can teach many subjects.

```python
class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()
    teachers = models.ManyToManyField(Teacher)
```

Key idea: Django model fields define table columns, validation rules, form behavior, and relationships between database tables.

#### Form API

##### HTML Form

Almost every web application collects data from users with forms.

- A form is a document where users enter responses into labeled fields.
- Common examples include registration forms, travel booking forms, and job application forms.
- HTML forms use the `<form>` tag and input elements such as text inputs, radio buttons, checkboxes, dropdowns, and lists.

```html
<form action="/form/" method="POST">
    <label for="name">Name of Applicant</label>
    <input type="text" id="name" name="name">

    <label for="add">Address</label>
    <input type="text" id="add" name="add">

    <label for="post">Post</label>
    <select id="post" name="post">
        <option value="Manager">Manager</option>
        <option value="Cashier">Cashier</option>
        <option value="Operator">Operator</option>
    </select>

    <input type="submit" value="Submit">
</form>
```

HTML has limited validation support by itself, so applications often need additional validation before or after form submission.

##### Django Form

Django includes a `Form` class in the `django.forms` module.

- A user-defined form class subclasses `forms.Form`.
- Form attributes are field objects.
- Field objects define expected input and validation.
- Django form fields render to corresponding HTML form elements.
  - `forms.CharField` usually renders as a text input.
  - `forms.ChoiceField` usually renders as a `<select>` element.

File: `myapp/forms.py`

```python
from django import forms


class ApplicationForm(forms.Form):
    pass
```

The application form from the HTML example can be represented as a Django form class.

File: `myapp/forms.py`

```python
from django import forms


class ApplicationForm(forms.Form):
    name = forms.CharField(label="Name of Applicant", max_length=50)
    address = forms.CharField(label="Address", max_length=100)
    posts = (
        ("Manager", "Manager"),
        ("Cashier", "Cashier"),
        ("Operator", "Operator"),
    )
    field = forms.ChoiceField(choices=posts)
```

By convention, user-defined form classes are stored in a `forms.py` file inside the app package.

##### Django Form Fields

Django provides many form field types.

- `CharField` renders as an HTML text input.
  - Use `widget=forms.Textarea` for longer multiline text.
- `IntegerField` accepts only integer numbers.
  - Use `min_value` and `max_value` to restrict the allowed range.
- `FloatField` validates floating-point numbers.
  - `DecimalField` validates numbers with a specified number of decimal places.
- `FileField` renders as an HTML file input.
- `ImageField` works like `FileField` but validates that the uploaded file is an image.
  - Pillow must be installed for image validation.
- `EmailField` validates that the input is a valid email address.
- `ChoiceField` renders as a dropdown using a sequence of two-item choices.

```python
first_name = forms.CharField(label="Enter first name", max_length=50)
age = forms.IntegerField(min_value=20, max_value=60)
price = forms.FloatField()
upload = forms.FileField()
email = forms.EmailField(max_length=254)
gender = forms.ChoiceField(choices=GENDER_CHOICES)
```

##### Rendering A Form Object In The Shell

A `Form` instance can render itself as HTML.

Open the Django shell:

```bash
python manage.py shell
```

Create and print a form instance:

```python
from myapp import forms

f = forms.ApplicationForm()
print(f)
```

Example rendered HTML:

```html
<tr>
    <th><label for="id_name">Name of Applicant:</label></th>
    <td>
        <input type="text" name="name" maxlength="50" required id="id_name">
    </td>
</tr>
<tr>
    <th><label for="id_address">Address:</label></th>
    <td>
        <input type="text" name="address" maxlength="100" required id="id_address">
    </td>
</tr>
<tr>
    <th><label for="id_field">Field:</label></th>
    <td>
        <select name="field" id="id_field">
            <option value="Manager">Manager</option>
            <option value="Cashier">Cashier</option>
            <option value="Operator">Operator</option>
        </select>
    </td>
</tr>
```

##### Form Template

A Django form object renders the form fields, but it does not render the surrounding `<form>` tag.

- Add the `<form>` tag in the template.
- Add `{% csrf_token %}` for POST forms.
- Place the form object inside the template where the fields should appear.
- Add a submit button manually.

File: `templates/form.html`

```html
<html>
<body>
    <form action="/form/" method="POST">
        {% csrf_token %}
        <table>
            {{ form }}
        </table>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

File: `views.py`

```python
from django.shortcuts import render

from .forms import ApplicationForm


def index(request):
    form = ApplicationForm()
    return render(request, "form.html", {"form": form})
```

##### Form Rendering Variations

Django can render a form in different HTML layouts.

`{{ form.as_table }}` renders fields as table rows.

```html
<table>
    <tr>
        <th><label for="id_name">Name of Applicant:</label></th>
        <td><input type="text" name="name" maxlength="50" required id="id_name"></td>
    </tr>
    <tr>
        <th><label for="id_address">Address:</label></th>
        <td><input type="text" name="address" maxlength="100" required id="id_address"></td>
    </tr>
    <tr>
        <th><label for="id_field">Field:</label></th>
        <td>
            <select name="field" id="id_field">
                <option value="Manager">Manager</option>
                <option value="Cashier">Cashier</option>
                <option value="Operator">Operator</option>
            </select>
        </td>
    </tr>
</table>
<input type="submit">
```

Output:

![Output display with the name of applicant and address tab as well as field dropdown selection](./assets/form_1.png)

`{{ form.as_p }}` renders fields wrapped in `<p>` tags.

```html
<p>
    <label for="id_name">Name of Applicant:</label>
    <input type="text" name="name" maxlength="50" required id="id_name">
</p>
<p>
    <label for="id_address">Address:</label>
    <input type="text" name="address" maxlength="100" required id="id_address">
</p>
<p>
    <label for="id_field">Field:</label>
    <select name="field" id="id_field">
        <option value="Manager">Manager</option>
        <option value="Cashier">Cashier</option>
        <option value="Operator">Operator</option>
    </select>
</p>
```

The form is displayed in the browser:

![Browser display of the output with name of applicant and address tabs as well as field dropdown selection](./assets/form_2.png)

`{{ form.as_ul }}` renders fields wrapped in `<li>` tags.

```html
<li>
    <label for="id_name">Name of Applicant:</label>
    <input type="text" name="name" maxlength="50" required id="id_name">
</li>
<li>
    <label for="id_address">Address:</label>
    <input type="text" name="address" maxlength="100" required id="id_address">
</li>
<li>
    <label for="id_field">Field:</label>
    <select name="field" id="id_field">
        <option value="Manager">Manager</option>
        <option value="Cashier">Cashier</option>
        <option value="Operator">Operator</option>
    </select>
</li>
<input type="submit">
```

The form renders in the browser:

![Browser display of the output with bullets before the name of applicant and address tabs as well as field dropdown selection](./assets/form_3.png)

`{{ form.as_div }}` renders fields wrapped in `<div>` tags.

```html
<div>
    <label for="id_name">Name of Applicant:</label>
    <input type="text" name="name" maxlength="50" required id="id_name">
</div>
<div>
    <label for="id_address">Address:</label>
    <input type="text" name="address" maxlength="100" required id="id_address">
</div>
<div>
    <label for="id_field">Field:</label>
    <select name="field" id="id_field">
        <option value="Manager">Manager</option>
        <option value="Cashier">Cashier</option>
        <option value="Operator">Operator</option>
    </select>
</div>
<input type="submit">
```

The form renders in the browser:

![Browser display of the form](./assets/form_4.png)

##### Reading Form Contents

The form's `action` attribute points to the URL that receives the submitted data.

- If `action="/form/"`, map a view to the `/form/` URL.
- The view receives the submitted `POST` data.
- The data can be used to create database rows or perform other processing.
- Bind submitted data with `ApplicationForm(request.POST)`.
- Validate submitted data with `form.is_valid()`.
- Access validated values through `form.cleaned_data`.

File: `views.py`

```python
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ApplicationForm


def form(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            post = form.cleaned_data["field"]
            return HttpResponse("Form successfully submitted")

    else:
        form = ApplicationForm()

    return render(request, "form.html", {"form": form})
```

Key idea: Django's Form API defines fields in Python, renders them as HTML, validates submitted data, and exposes cleaned values for backend processing.

#### Creating Forms

- This section mostly repeats the earlier [Form API](#form-api) workflow.
  - The earlier section already covers `forms.Form`, rendering forms in templates, `csrf_token`, `as_p`, validation, and `POST` processing.
  - The new example here is an employee work-entry form for the Little Lemon website.
- The example adds a few new form-building details.
  - `forms.TimeField` collects a time value.
  - `forms.ChoiceField` can use a tuple of choices stored in a constant.
  - `required=False` makes a field optional.
  - `help_text` displays guidance beside a field.
  - Inline styling can be added in the template, though CSS is usually cleaner for larger projects.
- The full setup touches several project files.
  - `forms.py` defines the form class.
  - `views.py` creates a form instance and passes it to the template.
  - `home.html` renders the form with `POST`, `{% csrf_token %}`, and a submit button.
  - App-level `urls.py` maps a path to the view.
  - Project-level `urls.py` includes the app routes.
  - `settings.py` must include the app in `INSTALLED_APPS`.
- Running the development server lets you test the form in the browser.
  - The form displays `first_name`, `last_name`, `shift`, and `time_log` fields.
  - `{{ form.as_p }}` renders form fields wrapped in paragraph tags.
  - Submitting an empty required form shows Django's built-in validation.

File: `myapp/forms.py`

```python
from django import forms


SHIFTS = (
    ("morning", "Morning"),
    ("afternoon", "Afternoon"),
    ("evening", "Evening"),
)


class InputForm(forms.Form):
    # Optional text fields for the employee name.
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)

    # ChoiceField renders a selectable list of predefined shift options.
    shift = forms.ChoiceField(choices=SHIFTS)

    # TimeField validates time input; help_text gives user-facing guidance.
    time_log = forms.TimeField(help_text="Enter the exact time.")
```

File: `myapp/views.py`

```python
from django.shortcuts import render

from .forms import InputForm


def form_view(request):
    # Create a blank form instance for display.
    form = InputForm()

    # Pass the form into the template context.
    context = {"form": form}
    return render(request, "home.html", context)
```

File: `myapp/templates/home.html`

```html
<form method="post" style="background-color: lightyellow;">
    {% csrf_token %}

    <!-- Render fields as paragraph elements. -->
    {{ form.as_p }}

    <input type="submit" value="Submit">
</form>
```

File: `myapp/urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path("form/", views.form_view, name="form_view"),
]
```

File: `myproject/urls.py`

```python
from django.urls import include, path

urlpatterns = [
    path("", include("myapp.urls")),
]
```

File: `settings.py`

```python
INSTALLED_APPS = [
    # ...
    "myapp",
]
```

Run from the project folder that contains `manage.py`:

```bash
python manage.py runserver
```

#### Model Form

- `ModelForm` connects a Django form directly to a Django model.
  - A regular `forms.Form` defines form fields manually.
  - A `ModelForm` generates form fields from a model.
  - It can save valid submitted data directly into the model's database table.
- `ModelForm` is useful when form input should become database records.
  - Example: Little Lemon employees log their work entry times.
  - The form collects a name and time value.
  - The submitted values are saved into a table created from the model.
- Creating a `ModelForm` follows a similar pattern to creating models and forms.
  - Define the model in `models.py`.
  - Define the `ModelForm` in `forms.py`.
  - Use an inner `Meta` class to connect the form to the model.
  - Choose which model fields should appear in the form.
- `fields = "__all__"` includes all editable model fields in the form.
  - This is convenient for learning and small examples.
  - In real applications, explicitly listing fields is often safer because it avoids exposing unintended fields: `["field1", "field2"]`.
- The view must handle both display and submission.
  - For a normal page load, create an empty form instance.
  - For a `POST` request, bind the form to `request.POST`.
  - Use `form.is_valid()` to validate submitted data.
  - Use `form.save()` to create the database row.
- The model should be registered in `admin.py` if it should appear in Django Admin.
  - Registration is not required for saving through `ModelForm`.
  - It is useful for inspecting saved entries in the admin interface.
- Migrations are still required.
  - The model defines the table structure.
  - `makemigrations` creates the migration file.
  - `migrate` creates the database table.
- The template can reuse the same form-rendering approach from previous sections.
  - Use `method="post"`.
  - Include `{% csrf_token %}`.
  - Render the form with `{{ form }}` or `{{ form.as_p }}`.
  - Add a submit button.

File: `myapp/models.py`

```python
from django.db import models


class Logger(models.Model):
    # Store the employee name submitted by the form.
    name = models.CharField(max_length=200)

    # Store the logged entry time submitted by the form.
    time_log = models.TimeField()
```

File: `myapp/forms.py`

```python
from django.forms import ModelForm

from .models import Logger


class LogForm(ModelForm):
    class Meta:
        # Connect this form to the Logger model.
        model = Logger

        # Include all editable fields from Logger in the form.
        fields = "__all__"
```

File: `myapp/admin.py`

```python
from django.contrib import admin

from .models import Logger


admin.site.register(Logger)
```

File: `myapp/views.py`

```python
from django.shortcuts import render

from .forms import LogForm


def form_view(request):
    # Start with an empty form for normal page loads.
    form = LogForm()

    if request.method == "POST":
        # Bind submitted POST data to the ModelForm.
        form = LogForm(request.POST)

        if form.is_valid():
            # Save valid form data as a Logger row in the database.
            form.save()

    return render(request, "home.html", {"form": form})
```

File: `myapp/templates/home.html`

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>
```

Run from the project folder that contains `manage.py`:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8080
```

Example submitted data:

```text
name: Kyle McGregor
time_log: 11:11
```

Key idea: `ModelForm` removes duplication between form definitions and model definitions, then lets validated form data be saved directly to the database.

#### Exercise: Working with Forms

Folder: [`lab/07-django-forms/`](./lab/07-django-forms/)

- Completed the ModelForm lab for the Little Lemon booking form.
  - Created a `Booking` model in `models.py`.
  - Created a `BookingForm` model form in `forms.py`.
  - Registered the `Booking` model in `admin.py`.
  - Enabled the existing `form_view` in `views.py`.
  - Reused the existing `booking.html` template.
  - Left migration commands for manual execution, as requested.
- The booking form stores reservation requests in the database.
  - `first_name` stores the guest's first name.
  - `last_name` stores the guest's last name.
  - `guest_count` stores the number of guests.
  - `reservation_time` uses `auto_now=True`, so Django fills it automatically and it is not shown in the form.
  - `comments` stores extra reservation notes.

File: `myapp/models.py`

```python
from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
```

File: `myapp/forms.py`

```python
from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
```

File: `myapp/admin.py`

```python
from django.contrib import admin
from .models import Booking

# Register your models here.
admin.site.register(Booking)
```

File: `myapp/views.py`

```python
from django.shortcuts import render
from myapp.forms import BookingForm

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)
```

File: `myapp/templates/booking.html`

```html
<p> Booking for Little Lemon ! </p>

<form action = "" method = "post", style="background-color: #E0E0E2;">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>
```

Existing route:

File: `myapp/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.form_view),
]
```

Run these commands manually from the folder that contains `manage.py`:

```bash
cd 03_Django/lab/07-django-forms/myproject
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8080
```

Open the form in the browser:

```text
http://127.0.0.1:8080/booking
```

Example form data from the instructions:

```text
First name: Jason
Last name: Murphy
Guest count: 5
Reservation time: auto-filled by Django because auto_now=True
Comment: Prefer indoors
```

![Exercise 07 Form](./assets/exercise-07-form.png)

![Exercise 07 Results](./assets/exercise-07-results.png)


#### Additional Resources

- [Models - official documentation](https://docs.djangoproject.com/en/4.1/topics/db/models/)
- [Migrations - official documentation](https://docs.djangoproject.com/en/4.1/topics/migrations/)
- [Using Models - Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
- [Detailed overview of Migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/#module-django.db.migrations)
- [Migration operations](https://docs.djangoproject.com/en/4.1/ref/migration-operations/)

### Admin

#### Django Admin

- Django automatically generates a unified admin interface for site administrators to add, edit, and delete content such as users, permissions, and database records.
- The interface is built from model metadata once models are registered - no manual UI code is needed.
- It is intended for site managers only, not for public visitors.
- Enabled by default via `django.contrib.admin` in `INSTALLED_APPS` inside `settings.py`.
- The admin URL path (`/admin`) is pre-configured in the project's URL configuration.
- Before accessing the interface, create a superuser with `python3 manage.py createsuperuser`, which prompts for username, email, and password.
  - Django rejects a username that already exists.
  - Weak passwords trigger a warning but can be accepted by pressing `Y`; use strong passwords in production.
- Access the interface by navigating to `<server-url>/admin` and logging in with the superuser credentials.
- The default interface shows: Authentication (Groups, Users), registered models, and a Recent Actions log.
  - Model entries can be added, edited, or deleted directly through the interface forms.
  - Per-user settings include username, password, personal info, group membership, and individual permissions.
  - A per-user history log tracks changes made through the admin.

```bash
python3 manage.py createsuperuser
# Prompts: Username, Email address, Password (×2)
# Then run the server and open http://127.0.0.1:8000/admin
```

#### Managing Users in Django Admin

Django's authorization and authentication system is provided by `django.contrib.admin`, which is installed by default and visible in `INSTALLED_APPS` inside `settings.py`.

##### Superuser and Permissions

A superuser can add or modify users and groups. After logging in, the admin interface looks like this:

![Admin interface display for superuser login](./assets/django_admin_welcome.png)

Adding users through the interface is straightforward -- follow the on-screen prompts.

A user with no permissions assigned cannot perform any meaningful task. Permissions can be granted:
- Individually, per user.
- Via groups -- create a group with a shared set of permissions and add users to it.

![User Permission Display](./assets/django_admin_groups.png)

A user whose `is_staff` property is `True` can log in to the admin interface.

##### Security Risks with the Default User Admin

Django's default admin has no restrictions on staff users. A staff user can:
- Manage other users.
- Edit their own permissions.
- Grant themselves superuser rights.

The out-of-box implementation does not prevent this.

![Demonstration of example users from Admin superuser page](./assets/django_admin_user_select.png)

##### Customizing the User Admin

To override the default User admin, unregister the built-in one and register a custom subclass of `UserAdmin`.

**Step 1 -- Unregister the default User admin** in `admin.py`:

```python
from django.contrib import admin
from django.contrib.auth.models import User

# Unregister the provided model admin:
admin.site.unregister(User)
```

**Step 2 -- Register a custom UserAdmin** using the `@admin.register()` decorator:

```python
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class NewAdmin(UserAdmin):
    pass
```

At this point the interface looks the same, but you can now add customizations.

##### Making Fields Read-Only

`UserAdmin` exposes a `readonly_fields` list. Fields in this list are shown as disabled in the change form and cannot be edited by anyone.

To prevent `date_joined` from ever being changed after a user is created:

```python
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        "date_joined",
    ]
```

##### Restricting a Field to Superusers Only

To let superusers edit a field (e.g. `username`) but block staff users, override `get_form()` and disable the field conditionally:

```python
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class NewAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True

        return form
```

`get_form()` generates the change form for a model. Checking `request.user.is_superuser` and setting `field.disabled = True` prevents non-superusers from modifying that field.

##### Registering and Customizing a Custom Model

Add a Django app (e.g. `myapp`) and register it in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',
]
```

Define a `Person` model in `myapp/models.py`:

```python
from django.db import models

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
```

Register the model in `myapp/admin.py`:

```python
from django.contrib import admin
from .models import Person

admin.site.register(Person)
```

Log in as the superuser -- `myapp` and its `Person` model now appear in the admin interface.

![Django administration page displaying groups and users for their authentication](./assets/django_admin_user_groups.png)

After adding a `Person` object, the list shows a generic label like "Person object (1)" by default.

![One-person objection adding display](./assets/django_admin_user_groups_add.png)

To show a meaningful label, add `__str__()` to the model:

```python
from django.db import models

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
```

Refreshing the list page now shows each person's name.

![Refreshed view of person adding page](./assets/django_admin_user_groups_add_2.png)

##### Customizing the Model List Display

Replace `admin.site.register()` with a `ModelAdmin` subclass decorated with `@admin.register()`. Use `list_display` to show specific fields as columns:

```python
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
```

The list view now shows `last_name` and `first_name` as clickable columns.

![User display with their clickable names to edit](./assets/django_admin_users.png)

Add `search_fields` to enable a search box that filters results. The lookup `first_name__startswith` matches entries whose first name begins with the search string:

```python
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith",)
```

![User list page with a search tab](./assets/django_admin_users_2.png)

#### Adding Groups and Users

- A `Reservation` model is defined in `models.py` with five fields: customer name, contact details, arrival time, guest count, and notes.
- The app must be listed in `INSTALLED_APPS` in `settings.py` before running migrations.
- Create a superuser with `python manage.py createsuperuser`; always use a strong password in production.
- Register the model in `admin.py` so it appears in the admin panel.
- Access the admin panel at `<server-url>/admin` and log in with the superuser credentials.
  - The panel shows a **Site Administration** section with **Groups** and **Users** links.
  - Registered app models appear in a separate section.
- Add records through the admin UI using the **Add** button for each model.
  - The form reflects the model's fields directly.
  - **Save and add another** resets the form after saving so multiple records can be added quickly.
- By default, model instances display as `Reservation object (n)` in the list; define `__str__` to show a meaningful label instead.
- Click a record in the admin list to open its edit form; options to delete and view history are also available.
- Add a new user via the **Users** --> **Add user** link; Django enforces password strength rules.
  - After saving, set personal info (first name, last name, email) and permissions (active, staff, superuser).
  - Users with the **staff** flag can log in to the admin panel.
  - Individual model-level permissions (view, add, change, delete) can be assigned per user.
  - Users can also be added to **Groups** for shared permission sets.
- Create a group via **Groups** --> **Add group**, give it a name (e.g. `staff`), and assign the desired permissions.
- Changes made in the admin panel are immediately reflected in the underlying database table.

```python
# models.py -- Reservation model with a human-readable __str__
from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    time = models.DateTimeField()
    count = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

# admin.py -- register the model so it appears in the admin panel
from django.contrib import admin
from .models import Reservation

admin.site.register(Reservation)
```

```bash
# Apply migrations, create a superuser, then start the server.
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8080
# Visit http://127.0.0.1:8080/admin
```

#### Permissions

- Django's built-in authentication system handles both authentication (who you are) and authorization (what you can do).
- Every user belongs to one of three classifications:
  - **Superuser** -- top-level administrator; has every permission in the system automatically, including over other users and all model data.
  - **Staff user** -- can log in to the admin interface (`is_staff = True`), but CRUD (create, read, update, delete) permissions on individual models must still be granted explicitly. Superusers are staff by default.
  - **Regular user** -- cannot access the admin site; marked active by default; may be marked inactive if authentication fails or the account is banned.
- Users can be created via the admin panel or the Django shell.
- Django auto-generates four permissions for every model, named with the pattern `<app>.<action>_<model>`:
  - `myapp.add_mymodel`
  - `myapp.change_mymodel`
  - `myapp.delete_mymodel`
  - `myapp.view_mymodel`
- Check whether a user holds a permission with `user.has_perm("<app>.<action>_<model>")`; it returns `True` or `False`.
- If a user lacks the required permission, raise `PermissionDenied` instead of returning the normal response.
- Assigning permissions per user is impractical at scale; use **groups** instead.
  - A group is a named collection of permissions.
  - A user can belong to any number of groups and inherits all permissions from each group.
  - Individual permissions can still be added directly to a user even when they belong to a group.
- To enforce a permission on a view, use the `@permission_required(("<app>.<action>_<model>")` decorator.

```python
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

# Create a user and grant staff status via the shell.
user = User.objects.create_user(username="jean", email="jean@example.com", password="str0ngPass!")
user.is_staff = True
user.save()

# Auto-generated permission names for a model called Reservation in myapp:
# myapp.add_reservation
# myapp.change_reservation
# myapp.delete_reservation
# myapp.view_reservation

# Check a permission in a view and deny access if it is missing.
def my_view(request):
    if not request.user.has_perm("myapp.add_reservation"):
        raise PermissionDenied
    # ... normal view logic

# Enforce a permission with the decorator (raises 403 if not met).
from django.contrib.auth.decorators import permission_required

@permission_required("myapp.add_reservation")
def add_reservation(request):
    ...
```

#### Enforcing Permissions

Django models themselves have no way to enforce permissions because they are unaware of the requesting user. User identity arrives through the request context, so permissions are typically enforced at the view layer, though they can also be checked in templates and URL patterns.

##### Model Permissions in the Admin Interface

The Django Admin interface lets you grant and enforce permissions on model data. By default every user receives Add, Change, View, and Delete permissions on all models.

Custom permissions can be defined on a model's inner `Meta` class and will appear in the user-permission list in the admin panel.

```python
# models.py
from django.db import models

class Product(models.Model):
    ProductID = models.IntegerField()
    name = models.TextField()
    category = models.TextField()

    class Meta:
        permissions = [("can_change_category", "Can change category")]
```

The codename `can_change_category` is referenced in code as `"myapp.can_change_category"`.

![User permission display list](./assets/django_admin_model_permissions.png)

##### Enforcing Permissions at the View Level

When a user is logged in, their details are available as `request.user`. For unauthenticated requests, `request.user` is an `AnonymousUser` instance. There are four common ways to enforce permissions in views.

**1. Raise `PermissionDenied` manually**

Check `request.user.is_anonymous` (a property, not a method) and raise a 403 error directly.

```python
from django.core.exceptions import PermissionDenied

def myview(request):
    if request.user.is_anonymous:
        raise PermissionDenied()
```

**2. `@login_required` decorator**

Redirects unauthenticated users to the login page; only authenticated users can reach the view.

```python
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def myview(request):
    return HttpResponse("Hello World")
```

**3. `@user_passes_test()` decorator**

Takes a callable that receives the user object and returns `True` or `False`. The view is only called when the callable returns `True`. An optional `login_url` argument redirects users who fail the test.

```python
from django.contrib.auth.decorators import user_passes_test

def testpermission(user):
    # is_authenticated is a property in Django 1.10+
    return user.is_authenticated and user.has_perm("myapp.can_change_category")

@user_passes_test(testpermission, login_url="/login/")
def change_ctg(request):
    # Logic for changing the category of a Product instance
    ...
```

**4. `@permission_required()` decorator**

The cleanest option when a single permission gate is needed. Pass `raise_exception=True` to return a 403 response instead of redirecting; combine with `@login_required` to redirect unauthenticated users first.

```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required("myapp.can_change_category", raise_exception=True)
def store_creator(request):
    # Logic for changing the category of a Product instance
    ...
```

**Class-based views -- `PermissionRequiredMixin`**

For class-based views, mix in `PermissionRequiredMixin` and set the `permission_required` attribute. A list can be used to require multiple permissions.

```python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from .models import Product

class ProductListView(PermissionRequiredMixin, ListView):
    permission_required = "myapp.view_product"
    # Require multiple permissions:
    # permission_required = ["myapp.view_product", "myapp.can_change_category"]
    template_name = "product.html"
    model = Product
```

##### Enforcing Permissions in Templates

Django's template language exposes two special context variables: `user` and `perms`. These are injected by the view's context processors.

Check whether the user is authenticated:

```html
<html>
<body>
  {% if user.is_authenticated %}
    {# Rendered only for authenticated users #}
  {% endif %}
</body>
</html>
```

Check a specific permission with `perms.<app>.<codename>`:

```html
<html>
<body>
  {% if perms.myapp.can_change_category %}
    {# Rendered only for users with the can_change_category permission #}
  {% endif %}
</body>
</html>
```

##### Enforcing Permissions in URL Patterns

Decorators can be applied directly in `urlpatterns` using `path()`. This is useful when a URL maps straight to a view that needs a permission gate without modifying the view function itself.

```python
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [
    path("users_only/", login_required(views.myview)),
    path(
        "category/",
        permission_required(
            "myapp.can_change_category", login_url="login"
        )(views.myview),
    ),
]
```

#### Users and Permissions

- Permissions can be managed either through the Django shell or the Django admin web interface.
- `django.contrib.auth` must be in `INSTALLED_APPS`; running `migrate` after adding it creates four default permissions per model: `add`, `change`, `delete`, and `view`.
- Permissions can be scoped per model type or per individual object instance using the `ModelAdmin` class methods.
- Custom permissions are declared in a model's inner `Meta` class alongside the auto-generated ones.
- `User` objects expose two ManyToMany fields for permission management:
  - `user_permissions` -- holds individual `Permission` objects assigned directly to the user.
  - `groups` -- holds `Group` objects; the user inherits all permissions belonging to each group.
- Both fields support the queryset methods `set()`, `add()`, `remove()`, and `clear()` to grant or revoke permissions.
- A user assigned to a group inherits all of that group's permissions automatically; additional individual permissions can still be added on top.

**Managing permissions via the admin interface:**

- Navigate to **Authentication and Authorization --> Groups** to create named groups and assign model-level permissions to them using the available permissions chooser.
- Navigate to **Authentication and Authorization --> Users** to create users, then edit each user to:
  - set personal info (first name, last name, email),
  - set the permission level (active, staff, superuser),
  - assign the user to one or more groups.
- The user list can be filtered by staff status, superuser status, or group membership.
- The admin home page shows a **Recent Actions** panel for a quick audit of recent changes.

```python
# Django shell -- create a user and assign a permission
from django.contrib.auth.models import User, Permission

user = User.objects.create_user("mario", "mario@example.com", "str0ngPass!")
user = User.objects.get(username="mario")

# Add a single permission (codename pattern: <action>_<model>)
perm = Permission.objects.get(codename="change_menu")
user.user_permissions.add(perm)

# Verify auto-generated permissions after migrate (all return True for a superuser)
user.has_perm("myapp.add_mymodel")
user.has_perm("myapp.change_mymodel")
user.has_perm("myapp.delete_mymodel")
user.has_perm("myapp.view_mymodel")
```

#### Exercise: Using Django Admin

Folder: [`lab/08-django-admin/`](./lab/08-django-admin/)

- Created an `Employees` model in `myapp/models.py` with four fields (`first_name`, `last_name`, `role`, `shift`) and a `__str__` returning the employee's first name.
- Registered the model in `myapp/admin.py` so it appears in the admin panel under the `myapp` section.
- `myproject/settings.py` already listed `myapp.apps.MyappConfig` in `INSTALLED_APPS` -- no change needed.
- Ran `makemigrations myapp` and `migrate` to create and apply the `Employees` table.
- Created superuser `admin` / `admin@littlelemon.com` non-interactively via the Django shell.
- **Manual steps via the browser** (server: `python manage.py runserver`, then `http://127.0.0.1:8000/admin`):
  - Logged in with the superuser credentials.
  - Added employee **Priya Giti** (role: Chef, shift: 1) using the **Add Employee** form; the `__str__` method causes the record to display as `Priya` instead of `Employee object (1)`.
  - Created a second user **jason\_chef** (password: `lemonChef@123!`) and granted staff status plus all `admin | log entry` permissions.

`myapp/models.py`

```python
from django.db import models


class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name
```

`myapp/admin.py`

```python
from django.contrib import admin
from .models import Employees

admin.site.register(Employees)
```

```bash
# Run from myproject/ (directory containing manage.py)
python manage.py makemigrations myapp
python manage.py migrate

# Create the superuser non-interactively
python manage.py shell -c "
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@littlelemon.com', 'lemonAdmin@3!')
"

# Command to create a super user via CLI
python3 manage.py createsuperuser

# Start the server and open http://127.0.0.1:8080/admin
python manage.py runserver 8080
```

#### Additional Resources

- [django-admin and manage.py -- official documentation](https://docs.djangoproject.com/en/4.1/ref/django-admin/)
- [Using the Django authentication system](https://docs.djangoproject.com/en/4.1/topics/auth/default/)
- [Django Admin site -- MDN web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)
- [Django Admin-site -- Comprehensive](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)
- [Django permissions -- TestDriven](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

### Database Configuration

#### Database Options

- Django defaults to SQLite, configured automatically in `settings.py` with no extra setup required.
- SQLite is a zero-configuration database: no server process to start or stop, no additional config files needed.
  - Best suited for small projects, rapid prototyping, and local test environments.
  - Not recommended when moving from development to production where scalability matters.
- Django supports multiple databases with minimal configuration: PostgreSQL, MariaDB, MySQL, Oracle, and SQLite.
  - PostgreSQL and MySQL are the most commonly used in production.
- Connecting to MySQL requires four pieces of information: host address, port number, database name, and a database driver.
  - The driver (`mysqlclient`) translates Python ORM queries into SQL and must be installed separately.
- All database connections are configured in the `DATABASES` dict inside `settings.py`.
  - `CONN_MAX_AGE` controls connection lifetime: `0` closes after each request, `None` keeps connections persistent, any integer sets the lifetime in seconds.
- MySQL credentials (name, user, password) can be stored in a separate options file (e.g., `/etc/mysql/my.cnf`) referenced from `settings.py`.
  - Storing credentials outside the Django project directory is a deliberate security measure.
- Django creates tables automatically via migration scripts, but the initial database itself must be created manually before running migrations.
- Security practices: use strong credentials, restrict database access to the application server only, and never expose connection details in source control.

```python
# settings.py -- default SQLite config (auto-generated)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# settings.py -- MySQL config using an options file (recommended for production)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "/etc/mysql/my.cnf",  # credentials stored outside the project
        },
        "CONN_MAX_AGE": 60,  # keep connections alive for 60 seconds
    }
}

# /etc/mysql/my.cnf -- credentials file (outside the Django project)
# [client]
# database = mydb
# user = myuser
# password = mypassword
# host = 127.0.0.1
# port = 3306
```

#### Configuring MySQL Connection

By default, Django uses SQLite for storage and retrieval. However, Django supports these databases:

- PostgreSQL
- MariaDB
- MySQL
- Oracle
- SQLite

This section covers the steps to connect a Django application to MySQL.

##### Why MySQL over SQLite

SQLite has several limitations for production use:
- serverless -- no standalone server process,
- no user management or authentication system,
- limited write concurrency.

MySQL is open-source and addresses these with scalability and built-in authentication. It is well suited for applications that outgrow SQLite.

##### Install MySQL Server

Download the MySQL installer for your OS from the [MySQL Downloads page](https://www.mysql.com/downloads/) and follow the wizard-based installation steps.

After installation, open a terminal and start the MySQL command-line client:

```bash
mysql -u root -p
```

Enter the password set during installation. Once at the MySQL prompt, create a database with UTF-8 support:

```sql
CREATE DATABASE mydatabase CHARACTER SET utf8mb4;
```

To verify, list the available databases:

```sql
SHOW DATABASES;
```

To exit the MySQL client, type:

```text
\q
```

##### Install the mysqlclient Driver

Django recommends the `mysqlclient` driver (a DB API (Database API)-compliant native driver) to interface Python with MySQL. Install it with pip:

```bash
pip install mysqlclient
```

`mysqlclient` requires version 1.4.3 or later and is the preferred choice over the pure-Python `MySQL Connector/Python`.

##### Create Project

```bash
cd 09-django-mysql

# Create a Django project.
django-admin startproject myproject

# Move into the generated project directory.
cd myproject

# Create an app inside the project.
python manage.py startapp myapp
```

##### Configure Django to Use MySQL

Open the project's `settings.py` and replace the default SQLite `DATABASES` entry with the MySQL configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mydatabase",
        "USER": "root",
        "PASSWORD": os.environ.get("MYSQL_ROOT_PASSWORD", ""),
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
        },
    }
}
```

Note that `os.environ.get("MYSQL_PASSWORD", "")` retrieves the MySQL password from an environment variable previously set. If we are working locally, we can set it with `dotenv`; in that case, we need to add to `settings.py` these lines at the top:

```python
import os
from dotenv import load_dotenv
load_dotenv()
```

Key settings:
- `ENGINE` -- specifies the MySQL backend.
- `NAME` -- the database name created in the MySQL client.
- `HOST` -- defaults to `127.0.0.1` (localhost); `PORT` defaults to `3306`.
- `OPTIONS.init_command` -- sets strict SQL mode to prevent silent data truncation on insertion.
- `OPTIONS.charset` -- sets the connection character set; `utf8mb4` is recommended.

Additional optional `OPTIONS` keys:

| Key | Description |
|-----|-------------|
| `init_command` | SQL command issued on each new connection |
| `charset` | Connection character set; `utf8mb4` recommended |
| `read_default_file` | Path to a MySQL option file (`.cnf`) to read credentials from |
| `sql_mode` | Session SQL mode; activates `STRICT_TRANS_TABLES` by default |

##### Apply Migrations

The `startproject` template installs Django apps such as `admin`, `auth`, and `sessions` that require database tables. Run migrations to create them in the MySQL database:

```bash
python manage.py makemigrations
python manage.py migrate
```

Verify the tables from the MySQL client:

```sql
USE mydatabase;
SHOW TABLES;
```

##### View MySQL Data in VS Code

Instead of the MySQL terminal, install the MySQL extension from the VS Code marketplace (search for "MySQL").

After installing, click the `+` button in the MySQL panel and enter:

- **Host**: `localhost`
- **User**: `root`
- **Password**: *(leave empty if none was set, or use the one set in the `.env` file)*

> **Note:** If you see the error `Client does not support authentication protocol requested by server`, run these commands in the MySQL client to fix the authentication method:
>
> ```sql
> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
> FLUSH PRIVILEGES;
> ```

After connecting, `localhost` appears in the VS Code explorer. Expand it, select `mydatabase`, and all tables created by `migrate` for `INSTALLED_APPS` will be visible.

![Display of mydatabase directory under localhost](./assets/vs_code_mysql.png)

#### Setting Up a MySQL Connection

New details compared to the previous section -- install, user creation, and migration steps.

##### Install MySQL on macOS

On macOS, use Homebrew as the package manager to install MySQL:

```bash
brew install mysql
```

##### Create a Dedicated Database User

Rather than connecting Django to MySQL as `root`, create a dedicated user for the project. From the MySQL shell:

```sql
CREATE USER 'admindjango' IDENTIFIED BY 'password';
--- If we CREATE DATABASE feedback, we can grant all privileges to the new user for that database:
GRANT ALL PRIVILEGES ON feedback.* TO 'admindjango';
--- or if we want to grant access to all databases:
GRANT ALL PRIVILEGES ON *.* TO 'admindjango';
FLUSH PRIVILEGES;
```

- `GRANT ALL PRIVILEGES ON <db>.*` gives the user full access to the target database.
- `FLUSH PRIVILEGES` applies the permission changes immediately.
- Update `settings.py` to use the new credentials (`USER`, `PASSWORD`, `NAME`).

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "feedback",  # changed from "mydatabase" to "feedback"
        "USER": "admindjango",  # new user
        "PASSWORD": os.environ.get("MYSQL_ADMIN_PASSWORD", ""),  # new user pw
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
        },
    }
}
```

##### Run makemigrations Before migrate

When starting a new database connection, run `makemigrations` before `migrate` so any pending model changes are captured:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Extra: Configuring PostgreSQL Connection

Django supports PostgreSQL 14 and higher. This section covers every step from a fresh OS install to a running Django migration.

##### Install PostgreSQL

###### Windows

Download and run the **EDB Interactive Installer** from [enterprisedb.com/downloads/postgres-postgresql-downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). The wizard installs:
- PostgreSQL server,
- **pgAdmin** -- a desktop GUI for managing databases,
- **StackBuilder** -- a package manager for add-ons.

###### macOS

Using Homebrew (CLI-first):

```bash
brew install postgresql@17
brew services start postgresql@17
```

Or install [Postgres.app](https://postgresapp.com) for a menubar-managed server with no extra configuration.

After a Homebrew install, add the client binaries to your path:

```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

###### Linux (Ubuntu / Debian)

Quick install from the distribution repository:

```bash
sudo apt install postgresql postgresql-client
sudo systemctl enable --now postgresql
```

For a specific version from the official PostgreSQL Apt Repository (PGDG):

```bash
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
# The script prompts for a version; it sets up the repo and installs it.
```

For Red Hat / Rocky / AlmaLinux, use the [PGDG RPM repo](https://www.postgresql.org/download/linux/redhat/).

##### Verify the Installation

```bash
psql --version        # e.g. psql (PostgreSQL) 17.x
pg_isready            # prints "accepting connections" if the server is running
```

##### Create a Database and User

Open the PostgreSQL interactive shell as the `postgres` superuser:

```bash
# Linux / macOS (Homebrew)
psql -U postgres

# macOS (Postgres.app -- uses the OS user as default superuser)
psql
```

Inside the psql shell:

```sql
-- Create a dedicated application user.
CREATE USER djangouser WITH PASSWORD 'strongpassword';

-- Create the database owned by that user.
CREATE DATABASE myproject OWNER djangouser;

-- Verify.
\l          -- list all databases
\du         -- list all users / roles
\q          -- quit
```

> Using a dedicated user (not `postgres`) limits the blast radius if application credentials are ever leaked.

##### Install the Python Driver

Django 5.x recommends **psycopg** (version 3). Install the binary variant, which bundles the C library and avoids needing `libpq-dev` on the system:

```bash
pip install "psycopg[binary,pool]"
```

The `pool` extra enables Django 5.1+ built-in connection pooling. If you need psycopg2 instead (e.g. for legacy compatibility):

```bash
pip install psycopg2-binary
```

Both drivers use the same `ENGINE` string in `settings.py`; Django detects which one is installed.

##### Configure Django to Use PostgreSQL

Open the project's `settings.py` and replace the default `DATABASES` entry:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "myproject",
        "USER": "djangouser",
        "PASSWORD": "strongpassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

Key fields:
- `ENGINE` -- always `"django.db.backends.postgresql"` for both psycopg2 and psycopg3.
- `HOST` -- use `"127.0.0.1"` for TCP; use `""` (empty string) to connect via a Unix socket (Linux default).
- `PORT` -- PostgreSQL defaults to `5432`.

**Common `OPTIONS`** (all optional):

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "myproject",
        "USER": "djangouser",
        "PASSWORD": "strongpassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "CONN_MAX_AGE": 60,       # reuse connections for 60 s (0 = close after each request)
        "OPTIONS": {
            "pool": True,         # enable psycopg3 connection pool (Django 5.1+, psycopg[pool])
            "sslmode": "require", # require TLS for remote servers; omit for localhost
        },
    }
}
```

| Key | Where | Description |
|-----|-------|-------------|
| `CONN_MAX_AGE` | top-level | Seconds to reuse a connection; `None` means unlimited |
| `pool` | `OPTIONS` | Enable psycopg3 built-in connection pool (Django 5.1+) |
| `sslmode` | `OPTIONS` | TLS enforcement (`require`, `verify-full`, `disable`) |
| `service` | `OPTIONS` | Name of a `pg_service.conf` entry (stores credentials outside code) |
| `passfile` | `OPTIONS` | Path to a `.pgpass` file for credential storage |

##### Apply Migrations

```bash
python manage.py migrate
```

Verify from the psql shell:

```bash
psql -U djangouser -d myproject
```

```sql
\dt             -- list all tables created by migrate
SELECT COUNT(*) FROM django_migrations;
```

##### View PostgreSQL Data in VS Code

The **Database Client** extension (`cweijan.vscode-database-client2`) used in the MySQL section also supports PostgreSQL. Install or open it, click `+`, select **PostgreSQL**, and enter:

- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `myproject`
- **User**: `djangouser`
- **Password**: `strongpassword`

After connecting, the database tree expands to show tables, views, and data -- no psql shell needed for day-to-day inspection.

Alternatively, **pgAdmin** (bundled with the EDB Windows installer, or available at [pgadmin.org](https://www.pgadmin.org)) provides a full-featured desktop GUI with a query editor, visual explain plans, and a server dashboard.

#### Exercise: Connecting to a Database

Folder: [`lab/10-django-msql-exercise/`](./lab/10-django-msql-exercise/)

- The `myproject` Django project came pre-built with a SQLite `DATABASES` stub in `settings.py`.
- The SQLite configuration was replaced with a MySQL connection pointing to a `feedback` database on localhost.
- `STRICT_TRANS_TABLES` SQL mode is set via `OPTIONS.init_command` to prevent silent data truncation on insertion.
- `mysqlclient` is expected to be installed as the Python--MySQL connector before running migrations.

Before running Django, create the database and enter the MySQL shell:

```bash
mysql -u root -p
```

```sql
CREATE DATABASE feedback;
SHOW DATABASES;  -- verify feedback is listed
EXIT;
```

Then apply migrations from the project directory:

```bash
cd lab/10-django-msql-exercise/myproject
python manage.py makemigrations
python manage.py migrate
```

**Files edited:**

`lab/10-django-msql-exercise/myproject/myproject/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'feedback',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

#### Additional Resources

- [Databases -- Django official](https://docs.djangoproject.com/en/4.1/ref/databases/)
- [MySQL notes -- Django official](https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-notes)
- [Installing MySQL Client](https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-db-api-drivers)
- [Installing MySQL on MacOS](https://dev.mysql.com/doc/refman/5.7/en/macos-installation.html)
- [Installing MySQL on Windows](https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html)
- [Installing and configuring MySQL with Django](https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-notes)


## 4. Templates

### Templates

#### Templates

- A template is a text-based document or Python string marked up with the Django Template Language (DTL).
- Templates have two types of content:
  - **Static** -- plain HTML that does not change between requests.
  - **Dynamic** -- DTL syntax that inserts context-dependent data, written inside `{{ }}`.
- The `render()` shortcut ties the template to the view; it takes three arguments:
  - `request` -- the incoming HTTP request,
  - a template path string,
  - a context dict whose keys become the variable names available inside the template.
- When rendered, every `{{ variable }}` placeholder is replaced with its value looked up in the context dict.
- Templates form the **presentation layer** of Django's MVT (Model-View-Template) architecture, keeping display logic separate from business logic.

View passing context to a template:

```python
# myapp/views.py
from django.shortcuts import render


def menu_item(request):
    context = {
        "dish_name": "Pasta",
        "price": 12.50,
    }
    return render(request, "myapp/menu_item.html", context)
```

Template receiving the context:

```html
<!-- myapp/templates/myapp/menu_item.html -->
<h1>{{ dish_name }}</h1>
<p>Price: ${{ price }}</p>
```

##### Django Template Engine and DTL

- Python is dynamic; HTML is static. The Django template engine bridges the gap by processing DTL inside HTML files before sending the response.
- DTL provides four types of constructs:
  - **Variables** -- `{{ name }}` -- output a value from the context.
  - **Tags** -- `{% tag %}` -- add logic such as loops, conditionals, and block definitions.
  - **Filters** -- `{{ name|filter }}` -- transform a variable's value before output.
  - **Comments** -- `{# comment #}` -- notes ignored by the engine.
- Tags map context dict values into the template and implement control flow (e.g. `{% for item in items %}`).

```html
<!-- Variables -->
<p>Welcome, {{ username }}!</p>

<!-- Filter: make the name uppercase -->
<p>{{ dish_name|upper }}</p>

<!-- Tag: for loop -->
<ul>
  {% for item in menu %}
    <li>{{ item.name }} -- ${{ item.price }}</li>
  {% endfor %}
</ul>

<!-- Tag: conditional -->
{% if user.is_authenticated %}
  <p>Hello, {{ user.username }}.</p>
{% else %}
  <p>Please log in.</p>
{% endif %}

<!-- Comment (not rendered in the output) -->
{# TODO: add allergen info here #}
```

##### Template Engine Configuration

- Template engine settings live in the `TEMPLATES` list inside `settings.py`.
- Key settings:
  - `APP_DIRS: True` -- tells Django to look for a `templates/` subdirectory inside each installed app.
  - `DIRS` -- a list of additional absolute paths Django searches for templates.
- Django's built-in engine can be replaced or extended; Jinja2 is a common alternative configured as a second entry in `TEMPLATES`.

```python
# settings.py
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # project-level template folder
        "APP_DIRS": True,                  # also search <app>/templates/
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
    # Optional: add Jinja2 as a second engine
    # {
    #     "BACKEND": "django.template.backends.jinja2.Jinja2",
    #     "DIRS": [BASE_DIR / "jinja2"],
    # },
]
```

Expected `templates/` layout when `APP_DIRS: True`:

```text
myapp/
└── templates/
    └── myapp/          <- namespace folder (prevents name collisions between apps)
        └── menu_item.html
```

##### Template Inheritance

- Template inheritance avoids duplicating shared HTML across pages, following the DRY (don't repeat yourself) principle.
- A **base template** defines the site-wide structure (head, navigation, footer) and marks overridable regions with `{% block name %}{% endblock %}`.
- **Child templates** extend the base with `{% extends "base.html" %}` and fill in only the blocks specific to that page.
- All pages that extend the base template automatically inherit its layout; changing the base updates every page at once.
- Best practice: keep all template files in a `templates/` folder inside the relevant app directory.

Base template:

```html
<!-- templates/base.html -->
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{% block title %}Little Lemon{% endblock %}</title>
</head>
<body>
  <nav><a href="/">Home</a> | <a href="/menu/">Menu</a></nav>

  <main>
    {% block content %}{% endblock %}
  </main>

  <footer><p>&copy; Little Lemon</p></footer>
</body>
</html>
```

Child template overriding the blocks:

```html
<!-- myapp/templates/myapp/menu_item.html -->
{% extends "base.html" %}

{% block title %}{{ dish_name }} -- Little Lemon{% endblock %}

{% block content %}
  <h1>{{ dish_name }}</h1>
  <p>Price: ${{ price }}</p>
{% endblock %}
```

#### Template Examples

##### HTML Response

A Django view's `HttpResponse` uses `Content-Type: text/html` by default, so any HTML string passed to it is rendered by the browser.

```python
# views.py -- static HTML embedded in Python
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")
```

When you need to inject variable data, you can use Python string formatting:

```python
# views.py -- dynamic HTML via string formatting
from django.http import HttpResponse


def index(request, name):
    return HttpResponse("<h1>Hello, {}.</h1>".format(name))
```

Embedding HTML directly in Python becomes hard to maintain as pages grow: 
- escaping is tedious, 
- conditional logic clutters the view, 
- and designers cannot edit a Python file.

Templates solve all three problems.

##### Rendering a Template

A template is an HTML file with placeholders for variable data, written in the DTL (Django Template Language). Create `hello.html` inside a `templates/` folder:

```html
<!-- templates/hello.html -->
<html>
<head>
  <title>My Django website</title>
</head>
<body>
  <h1>Hello World</h1>
</body>
</html>
```

**Long form** -- use `django.template.loader` to load and render the template explicitly:

```python
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("hello.html")
    context = {}
    return HttpResponse(template.render(context, request))
```

**Shortcut** -- `render()` from `django.shortcuts` combines all three steps into one call:

```python
from django.shortcuts import render


def index(request):
    return render(request, "hello.html", {})
```

##### Variable Tag

The third argument of `render()` is the **context** -- a dict whose keys become variable names inside the template. Pass a `name` URL parameter through the context:

```python
# views.py
from django.shortcuts import render


def index(request, name):
    context = {"name": name}
    return render(request, "hello.html", context)
```

Inside the template, wrap the context key in double curly braces to output its value:

```html
<!-- templates/hello.html -->
<html>
<body>
  <h1>Hello {{ name }}</h1>
</body>
</html>
```

##### If and For Tags

Tags add control flow to a template. Use `{% if %}` for conditionals and `{% for %}` to iterate over a list -- useful for displaying database records.

```html
<!-- conditional -->
{% if name %}
  <h1>Hello {{ name }}</h1>
{% else %}
  <h1>Hello stranger</h1>
{% endif %}

<!-- loop -- render one <li> per item in a queryset or list -->
<ul>
  {% for item in menu_items %}
    <li>{{ item.name }}</li>
  {% endfor %}
</ul>
```

##### Filters

Filters transform a variable's value before output. They are applied with the `|` (pipe) operator: `{{ variable|filter }}`.

```html
<!-- upper / lower / title -- change letter case -->
{{ name|upper }}    {# "john" -> "JOHN" #}
{{ name|lower }}    {# "JOHN" -> "john" #}
{{ name|title }}    {# "simple is better" -> "Simple Is Better" #}

<!-- length -- number of items in a list or characters in a string -->
{{ nums|length }}   {# [1,2,3,4] -> 4 #}

<!-- wordcount -- number of words in a string -->
{{ string|wordcount }}  {# "Simple is better than complex" -> 5 #}

<!-- slice -- subset of a list, using Python slice notation as a string argument -->
{{ nums|slice:"1:3" }}  {# [1,2,3,4,5,6,7,8] -> [2, 3] #}

<!-- first / last -- first or last item in a list -->
{{ nums|first }}    {# 1 #}
{{ nums|last }}     {# 8 #}
```

The pipe syntax passes the slice range as a quoted string argument (`"1:3"`), not bracket notation.

##### Built-in Filter Reference

| Category | Filters |
|---|---|
| **Strings** | `upper`, `lower`, `title`, `capfirst`, `truncatewords:N`, `truncatechars:N`, `wordcount`, `slugify`, `striptags`, `linebreaks`, `safe` |
| **Numbers** | `floatformat:N`, `filesizeformat`, `intcomma` (requires `humanize`) |
| **Lists** | `length`, `first`, `last`, `slice:"1:3"`, `join:", "`, `dictsort:"key"`, `random` |
| **Dates** | `date:"Y-m-d"`, `time:"H:i"`, `timesince`, `timeuntil` |
| **Logic** | `default:"fallback"`, `default_if_none:"n/a"`, `yesno:"yes,no,maybe"` |
| **URLs** | `urlencode`, `urlize` |

Full reference: [Django built-in filters](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#filters)

##### Custom Filters

You can define your own filters inside a `templatetags/` package in any installed app.

**1. Create the package:**

```text
myapp/
└── templatetags/
    ├── __init__.py
    └── myapp_filters.py
```

**2. Register and write the filter functions:**

```python
# myapp/templatetags/myapp_filters.py
from django import template

register = template.Library()


@register.filter(name="euros")
def euros(value):
    """Format a number as a euro price: 12.5 -> '€12.50'"""
    return f"€{value:.2f}"


@register.filter(name="clamp")
def clamp(value, max_value):
    """Cap a number at max_value: {{ score|clamp:100 }}"""
    return min(value, max_value)
```

**3. Load the library and use it in the template:**

```html
{% load myapp_filters %}

<p>{{ price|euros }}</p>           {# -> €12.50 #}
<p>{{ user_score|clamp:100 }}</p>  {# -> never exceeds 100 #}
```

Rules for custom filters:
- A filter that accepts an argument receives it as its second parameter (`value, arg`).
- Mark output as safe with `mark_safe()` only when the string contains no user-supplied HTML -- otherwise it is an XSS (cross-site scripting) risk.
- The `templatetags/` directory must live inside an app that is listed in `INSTALLED_APPS`.

#### Creating Templates

- Templates combine static HTML with dynamic data from the view, promoting code reusability.
- The view retrieves data (from a dict, model query, etc.) and passes it to the template via `render()`.
- `render()` takes three arguments:
  - `request` -- the incoming HTTP request object,
  - `path` -- relative path to the HTML file inside the templates directory,
  - `context` -- a dict whose keys become variable names inside the template.

**Checklist to wire up a new template:**

1. Define a view in `views.py` that returns `render()` with a context dict.
2. Register the URL in `urls.py` at both the app and project levels.
3. Add the `templates/` directory to `DIRS` in `settings.py` and confirm the app is in `INSTALLED_APPS`.
4. Create the HTML file inside the `templates/` folder.
5. Use `{{ key }}` in the HTML to output values from the context dict.

**Example -- About page for Little Lemon:**

```python
# myapp/views.py
from django.shortcuts import render


def about(request):
    about_content = {
        "about": "Little Lemon is a family-owned Mediterranean restaurant.",
    }
    return render(request, "about.html", about_content)
```

```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
]
```

```python
# myproject/settings.py  -- add the project-level templates folder to DIRS
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # project-level folder
        "APP_DIRS": True,
        ...
    },
]
```

```html
<!-- templates/about.html -->
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>About</title>
  <style>
    body { background-color: #f5f5dc; }
  </style>
</head>
<body>
  <h2>About</h2>
  <p>{{ about }}</p>  <!-- replaced at render time with the dict value -->
</body>
</html>
```

- Changing the value of `"about"` in the view's dict and saving immediately updates the rendered page on refresh -- no template edit needed.
- Static content (headings, styling) lives in the HTML; dynamic content comes from the context dict.

#### Exercise: Creating Templates

Folder: [`lab/11-django-templates/`](./lab/11-django-templates/)

- `settings.py` -- set `DIRS` to `['templates']` so Django finds the project-level templates folder, and added `STATICFILES_DIRS = ['myapp/static']` so the `{% static %}` tag can resolve images stored under the app.
- `views.py` -- implemented two view functions (`about` and `menu`); each builds the same `about_content` dict and passes it to `render()` under the `'content'` key.
- `templates/about.html` -- created with a styled `<h1>` heading and a `<p>` tag using `{{ content.about }}` to render the dict value dynamically.
- `templates/menu.html` -- created with `{% load static %}` at the top, a styled `<h1>` heading, and an `<img>` tag using `{% static 'img/dessert.jpg' %}` to serve the dessert image from the app's static folder.
- URL routing was already wired in `myapp/urls.py` (`about/` -> `views.about`, `menu/` -> `views.menu`) and included in the project-level `urls.py`.

**Static files explained:**

Static files (CSS, JavaScript, images, fonts) are served as-is -- the server sends them unchanged to every browser request, with no Python code involved.

| `settings.py` key | Purpose |
|---|---|
| `STATIC_URL` | URL prefix browsers use to request static files (e.g. `/static/`) |
| `STATICFILES_DIRS` | Extra folders Django searches for static files beyond each app's own `static/` subfolder |
| `STATIC_ROOT` | Destination for `collectstatic` in production; not used during development |

Standard static file layout inside an app (namespace subfolder prevents name collisions between apps):

```text
myapp/
└── static/
    └── myapp/
        ├── img/
        │   └── dessert.jpg
        ├── css/
        │   └── style.css
        └── js/
            └── main.js
```

In this exercise the static folder is flat (`myapp/static/img/`) without the extra namespace level, which is fine for single-app projects. Reference static files in any template with `{% load static %}` and the `{% static %}` tag:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
<img src="{% static 'myapp/img/dessert.jpg' %}">
```

During development (`DEBUG = True`) Django's built-in server serves static files automatically. In production, run `python manage.py collectstatic` to copy everything into `STATIC_ROOT`, then let nginx or a CDN (Content Delivery Network) serve that folder instead of Django.

Run the server and visit:

```bash
cd lab/11-django-templates/myproject
python manage.py runserver
# http://127.0.0.1:8000/about/  ->  heading + restaurant description
# http://127.0.0.1:8000/menu/   ->  heading + dessert image
```

`templates/menu.html`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <!-- Add heading code -->
    <h1 style="color: #495E57"> Menu </h1>
    <!-- Add paragraph code -->

    <!-- Add image code -->
    <img src="{% static 'img/dessert.jpg' %}">
</body>

</html>
```

`templates/about.html`:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <!-- Add heading code -->
    <!-- Add heading code -->
    <h1 style="color: #495E57"> About </h1>
    <!-- Add paragraph code -->
    <p> {{content.about}} </p>
    <!-- Add image code -->

</body>

</html>
```

Relevant code for `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
STATICFILES_DIRS = [
    'myapp/static',
]
```

`views.py`:

```python
from django.shortcuts import render

# Create your views here for menu.
def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12--15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "about.html", {'content': about_content})

def menu(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12--15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "menu.html", {'content': about_content})
```

### Working with Templates

#### Working with Template Language

- DTL (Django Template Language) separates presentation logic from application logic.
- It is based on the Jinja2 template engine and shares most of its features.
- The Python interpreter does not execute DTL code, which adds a security layer.
- DTL follows the DRY (don't repeat yourself) principle by letting developers write reusable markup.
- The four DTL constructs are: **variables**, **tags**, **filters**, and **comments**.

##### Variables

- Variables are wrapped in double curly braces: `{{ variable }}`.
- The template engine looks up the key in the context dict and replaces the placeholder with its value.
- Dot notation supports dict key access, object attribute access, and list index lookup.

```html
<!-- context = {"restaurant_name": "Little Lemon", "menu": [{"name": "Pasta", "price": 12}]} -->

<p>Welcome to {{ restaurant_name }} restaurant.</p>

<!-- dot notation: dict key -> attribute -> list index, tried in that order -->
<p>{{ menu.0.name }}</p>
```

##### Tags

- Tags add control flow and logic to templates; they use `{% %}` syntax and always require a closing tag.
- Common tags:
  - `{% if %}` / `{% elif %}` / `{% else %}` / `{% endif %}` -- conditional rendering,
  - `{% for %}` / `{% endfor %}` -- iteration over a list or queryset,
  - `{% extends %}` / `{% block %}` -- template inheritance (covered separately).

```html
<!-- if tag: check login status -->
{% if logged_in %}
  <p>Welcome back!</p>
{% else %}
  <a href="/login/">Log in</a>
{% endif %}

<!-- for tag: render a menu list dynamically -->
<ul>
  {% for item in menu %}
    <li>{{ item.name }} -- ${{ item.price }}</li>
  {% endfor %}
</ul>
```

##### Filters

- Filters transform a variable's value before output using the `|` (pipe) operator.
- Some filters accept an argument after a colon: `{{ variable|filter:"argument" }}`.

```html
<!-- upper: convert string to uppercase -->
{{ restaurant_name|upper }}        {# "little lemon" -> "LITTLE LEMON" #}

<!-- date: format a date object -->
{{ order_date|date:"Y-m-d" }}      {# -> "2026-06-25" #}
{{ order_date|date:"d M Y" }}      {# -> "25 Jun 2026" #}
```

##### Comments

- Comments are ignored by the template engine and do not appear in the rendered HTML.
- Use `{# #}` for single-line comments and `{% comment %}` / `{% endcomment %}` for multi-line blocks.

```html
{# This line is not rendered #}

{% comment %}
  This entire block is ignored.
  Useful for temporarily disabling template sections.
{% endcomment %}
```

#### Template Language and Variable Interpolation

##### Template Engine Overview

A web template is a static HTML file interspersed with placeholder blocks of DTL code. The template engine merges data from any source (e.g., a database query) with these placeholders and renders the result to the browser.

![Diagram for the template engine that shows the data input and generated content to browser](./assets/template_engine.png)

Django's default engine is DTL, but you can swap in another engine (e.g., Jinja2) by changing the `TEMPLATES` setting in `settings.py`.

##### Variable Interpolation via `render()`

The `render()` function passes context data to a template. It takes the HTTP request, the template path, and a context dictionary -- each key in the dict becomes a template variable.

```python
# URL: http://localhost:8000/myapp/Novak  (name captured as a path parameter)
def index(request, name):
    context = {'name': name}
    return render(request, 'index.html', context)
```

```html
<h2>Welcome {{ name }}</h2>  {# renders: Welcome Novak #}
```

Context values can also be dictionaries; access their keys with the same dot notation:

```python
def person_view(request):
    person = {'name': 'Roger', 'profession': 'Teacher'}
    return render(request, 'person.html', {'person': person})
```

```html
Name: {{ person.name }}             {# -> Roger #}
Profession: {{ person.profession }} {# -> Teacher #}
```

##### `for` Loop Extras

**Iterating over a dictionary's key--value pairs:**

```html
{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}
```

**`forloop` loop variables** -- available inside every `{% for %}` block:

| Variable | Description |
|---|---|
| `forloop.counter` | Current iteration, 1-indexed |
| `forloop.revcounter` | Remaining iterations from the end, 1-indexed |
| `forloop.first` | `True` on the first iteration |
| `forloop.last` | `True` on the last iteration |
| `forloop.parentloop` | Reference to the enclosing loop in nested loops |

```html
<ul>
    {% for lang in langs %}
    <li>{{ forloop.counter }}: {{ lang }}</li>
    {% endfor %}
</ul>
{# output: 1: Python  2: Java  3: PHP … #}
```

Nested loops use `forloop.parentloop` to access the outer counter:

```html
{% for key, values in dct.items %}
    <p>{{ forloop.parentloop.counter }}: {{ key }}</p>
    <ul>
        {% for value in values %}
        <li>{{ value }}</li>
        {% endfor %}
    </ul>
{% endfor %}
```

##### Additional Tags

**`{% comment "Optional note" %}`** -- The `{% comment %}` tag accepts an optional descriptive string in the opening tag (useful for noting why a block is disabled):

```html
{% comment "Disabled during A/B test" %}
    <p>Old hero section</p>
{% endcomment %}
```

**`{% csrf_token %}`** -- Inserts a hidden CSRF (Cross-Site Request Forgery) protection token into forms. Django rejects POST requests that are missing this token.

```html
<form method="post">
    {% csrf_token %}
    ...
</form>
```

**`{% include %}`** -- Renders another template in place, passing it the current context. The template name can be a string literal or a variable.

```html
{% include "nav.html" %}
```

**`{% with %}`** -- Defines a scoped local variable available only between `{% with %}` and `{% endwith %}`.

```html
{% with rate=5 %}
    Interest = {{ amt }} * {{ rate }}
{% endwith %}
```

##### Additional Filters

| Filter | What it does | Example |
|---|---|---|
| `default` | Returns a fallback when the variable is falsy | `{{ value\|default:"nothing" }}` |
| `join` | Joins a list with a separator (like `str.join()`) | `{{ words\|join:" _ " }}` |
| `length` | Length of a string or list; `0` for undefined | `{{ name\|length }}` |
| `first` | First item in a list | `{{ list\|first }}` |
| `last` | Last item in a list | `{{ list\|last }}` |
| `lower` | Convert to all lowercase | `{{ name\|lower }}` |
| `title` | Title-case each word | `{{ string\|title }}` |
| `wordcount` | Number of words in a string | `{{ string\|wordcount }}` |

#### Mapping Model Objects to a Template

- Django makes it straightforward to fetch database records and display them dynamically in a template.
- The workflow has four steps: import the model, query all records, pass them to the template via a context dict, and render.
  - Use `Model.objects.all()` to retrieve a QuerySet of every row.
  - Wrap it in a dict and pass that dict as the third argument to `render()`.
- In the template, use Django Template Language (DTL) tags to iterate safely:
  - `{% if menu %}` checks that the QuerySet is non-empty before looping.
  - `{% for item in menu %}` iterates over each model instance.
  - `{{ item.name }}` and `{{ item.price }}` access instance attributes.
  - `{% else %}` provides a fallback message when the QuerySet is empty.
  - Close with `{% endfor %}` and `{% endif %}`.
- Wrap output in HTML tags (e.g., `<p>`) to control line breaks and formatting.
- New database entries added via Django Admin appear automatically on page refresh -- no code change needed.

```python
# models.py
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

# views.py
from django.shortcuts import render
from .models import Menu

def menu_card(request):
    new_menu = Menu.objects.all()
    new_menu_dict = {"menu": new_menu}
    return render(request, "menu_card.html", new_menu_dict)

# urls.py  (inside urlpatterns)
# path("menu_card/", views.menu_card, name="menu_card"),
```

```html
<!-- menu_card.html -->
{% if menu %}
  {% for item in menu %}
    <p>{{ item.name }} -- {{ item.price }}</p>
  {% endfor %}
{% else %}
  <p>No items available.</p>
{% endif %}
```

#### Exercise: Creating Dynamic Templates

Folder: [`lab/12-django-dynamic-templates/`](./lab/12-django-dynamic-templates/).

- The goal is to display all `Menu` model rows dynamically on a `/menu/` page using a view, a context dict, and a DTL (Django Template Language) template.
- **`myapp/models.py`** -- already provided; defines `Menu` with `name` (CharField) and `price` (IntegerField) and a `__str__` returning `name`.
- **`myapp/views.py`** -- implement a `menu(request)` view:
  - Import `Menu` from `.models`.
  - Call `Menu.objects.all()` and store in `menu_items`.
  - Wrap it in `items_dict = {"menu": menu_items}`.
  - Return `render(request, "menu.html", items_dict)`.
- **`templates/menu.html`** -- create in the project-root `templates/` directory (already registered in `settings.py` `DIRS`):
  - Use `{% if menu %}` to guard against an empty QuerySet.
  - Loop with `{% for item in menu %}` and render `{{ item.name }} : {{ item.price }}<br>`.
  - Add `{% else %}` with a fallback message and close with `{% endif %}`.
- **Migrations** -- run `makemigrations myapp` then `migrate` to create the `Menu` table in the SQLite database.
- New entries added via Django Admin at `/admin/` appear on the page immediately after refresh.

```python
# myapp/views.py
from django.shortcuts import render
from .models import Menu

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {"menu": menu_items}
    return render(request, "menu.html", items_dict)
```

```html
<!-- templates/menu.html -->
<!DOCTYPE html>
<html lang="en">
<body>
    {% if menu %}
        {% for item in menu %}
            {{ item.name }} : {{ item.price }}<br>
        {% endfor %}
    {% else %}
        No items to display
    {% endif %}
</body>
</html>
```

```bash
# Run once to set up the database table
python manage.py makemigrations myapp
python manage.py migrate
# Then start the dev server and visit http://127.0.0.1:8080/menu/
python manage.py runserver 8080
```

#### Template Inheritance

- DRY (Don't Repeat Yourself) is a core Django principle: every piece of data or logic should live in exactly one place.
- Template inheritance solves repeated markup (headers, footers) by extracting common elements into a single base template rather than copying them across every page.
- A page is broken into **blocks** -- named regions such as the header and footer -- that child templates can reference or override.
- Django provides two DTL tags for reuse: `{% include %}` and `{% extends %}`.
- **`{% include %}`** -- embeds a sub-template into the current page:
  - References a template by string literal or variable, e.g. `{% include "header.html" %}`.
  - Each include is an independent rendering process with no shared state between templates.
  - Variables/objects from the view's context dict are available inside the included template; extra attributes can be passed directly on the tag.
- **`{% extends %}`** -- creates a parent--child relationship between templates:
  - The child declares `{% extends "base.html" %}` (string literal) or `{% extends parent_var %}` (variable that resolves to a string).
  - The child can override named `{% block %}` regions defined in the parent; anything outside a block in the child is ignored.
  - Unlike `{% include %}`, which simply inserts HTML, `{% extends %}` allows the child to *replace* parent content, not just append it.
- Use `{% include %}` for self-contained, stateless partials (nav bars, footers); use `{% extends %}` when pages share a full layout skeleton and differ only in certain regions.

```html
<!-- base.html -- parent template -->
<!DOCTYPE html>
<html>
<body>
    {% include "header.html" %}   {# stateless partial -- no shared state #}

    {% block content %}
    {% endblock %}               {# child templates override this region #}

    {% include "footer.html" %}
</body>
</html>

<!-- about.html -- child template -->
{% extends "base.html" %}

{% block content %}
    <h1>{{ page.name }}</h1>
    <p>About us content here.</p>
{% endblock %}
```

#### More on Template Inheritance

Template inheritance in Django Template Language (DTL) mirrors OOP (object-oriented programming) inheritance: a child template inherits the full layout of a parent and can override only specific regions. This keeps headers, footers, and navigation bars consistent across all pages without duplicating markup.

##### Page Layout and the `{% block %}` Tag

Suppose you are building a three-page web app (home, register, login). Every page shares a header, a sidebar, and a footer -- only the main content area changes per page.

![Display of the place of contents block on a page](./assets/web_app_page.png)

Template inheritance is implemented with the `{% block %}` and `{% endblock %}` tags. A block is a named region that child templates can override:

```html
{% block name %}
  ...
{% endblock %}
```

To design the layout:

1. Identify elements shared across all pages (header, sidebar, footer) -- these become plain HTML in `base.html`.
2. Identify elements that vary per page (main content) -- wrap these in `{% block %}` tags.
3. Leave variable blocks empty (or with default content) in `base.html`.

##### Building `base.html`

Place the following sections in `templates/base.html`. This file is never rendered directly -- it is only inherited.

**Header** -- company title and a horizontal rule:

```html
<!--header-->
<div style="height:10%;">
    <h2 align="center">Django Web Application</h2>
    <hr>
</div>
```

**Sidebar** -- navigation links (use dummy `#` hrefs initially; replace after URL patterns are defined):

```html
<!--sidebar-->
<div style="width:20%; float:left; border-right-style:groove">
    <ul>
        <b>
            <li><a href="#">home</a></li>
            <li><a href="#">register</a></li>
            <li><a href="#">login</a></li>
        </b>
    </ul>
</div>
```

**Contents block** -- empty block that each child template fills in:

```html
<!--contents-->
<div style="margin-left:21%;">
    <p>
        {% block contents %}
        {% endblock %}
    </p>
</div>
```

**Footer** -- also wrapped in a `{% block %}` so the login page can extend it later:

```html
<!--footer-->
<hr>
{% block footer %}
<div>
    <h4 align="right">All rights reserved</h4>
</div>
{% endblock %}
```

##### Adding Views and URL Patterns

Add a view function for each page in `views.py`:

```python
def home(request):
    return render(request, "home.html", {})

def register(request):
    return render(request, "register.html", {})

def login(request):
    return render(request, "login.html", {})
```

Register the URL patterns in `urls.py`:

```python
urlpatterns = [
    # ... existing patterns ...
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
```

Then update the sidebar links in `base.html` to use the real URLs:

```html
<!--sidebar-->
<div style="width:20%; float:left; border-right-style:groove">
    <ul>
        <b>
            <li><a href="/myapp/home/">home</a></li>
            <li><a href="/myapp/register/">register</a></li>
            <li><a href="/myapp/login/">login</a></li>
        </b>
    </ul>
</div>
```

##### Writing Child Templates

Each child template opens with `{% extends "base.html" %}` and overrides only the blocks it needs. Any content in a child template that is not inside a `{% block %}` tag is silently ignored.

**`home.html`:**

```html
{% extends "base.html" %}

{% block contents %}
<h2 align="center">This is Home page</h2>
{% endblock %}
```

Visit `/myapp/home/` -- the page inherits the full layout with only the content block replaced:

![Django web application homepage view](./assets/web_app_page_2.png)

**`register.html`:**

```html
{% extends "base.html" %}

{% block contents %}
<h2 align="center">Registration Form appears here</h2>
{% endblock %}
```

![Register page view](./assets/web_app_page_3.png)

**`login.html`** -- overrides both `contents` and `footer`. It uses `{{ block.super }}` to render the parent's footer content first, then appends extra text. `{{ block.super }}` works like Python's `super()`: it injects the parent block's output at that position.

```html
{% extends "base.html" %}

{% block contents %}
<h2 align="center">Login Form appears here</h2>
{% endblock %}

{% block footer %}
{{ block.super }}
<h4 align="right">Designed By: Alexa Designs Ltd</h4>
{% endblock %}
```

The `templates/` folder now contains four files -- `base.html` plus the three child templates:

![Display of child templates as home, register and login in templates folder](./assets/web_app_page_4.png)

`/myapp/login/` renders with the original "All rights reserved" footer followed by the extra credit line:

![Location of login form display between header and footer](./assets/web_app_page_5.png)

##### Serving Static Files

Web apps also serve static assets (images, JavaScript, CSS). Django includes `django.contrib.staticfiles` in `INSTALLED_APPS` by default.

- `settings.py` sets `STATIC_URL = 'static/'`.
- Place all static assets under `myapp/static/myapp/`.
- In any template, load the `{% static %}` tag and reference assets by their path relative to `STATIC_URL`:

```html
{% load static %}
<img src="{% static 'my_app/example.jpg' %}">
```

#### Working with Template Inheritance

- `{% extends %}` creates a parent--child relationship: the child replaces named `{% block %}` regions of the parent and inherits everything else.
- `{% include %}` embeds a sub-template at that position without any inheritance; each include is an independent render with no shared state.
- The demo builds the Little Lemon website with three pages (Home, Menu, About) that share a common layout and header.
- **Project setup steps:**
  - Add three view functions (`home`, `about`, `menu`) to `views.py` and map them in both the project-level and app-level `urls.py`.
  - Register the app in `INSTALLED_APPS` and add the `templates/` path to `DIRS` in `settings.py`.
  - Create a `templates/` folder at the project root and a `templates/partials/` subfolder for reusable fragments.
- **File structure to create:**
  - `templates/base.html` -- the shared layout skeleton.
  - `templates/index.html`, `templates/about.html`, `templates/menu.html` -- the three child pages.
  - `templates/partials/_header.html` -- the header/nav fragment included via `{% include %}`.
- **`base.html`** -- define the full HTML shell with a `{% block content %}` placeholder and any shared styles:
  - A background color set on `<body>` in `base.html` automatically applies to every child page, proving inheritance.
  - Add `{% include "partials/_header.html" %}` above the block so the header appears on every page.
- **Child templates** -- only two lines needed to inherit the full layout and inject page-specific content:
  - `{% extends "base.html" %}` must be the very first line.
  - Page content goes inside `{% block content %}…{% endblock %}`.
- Adding `{% include "partials/_header.html" %}` to `base.html` once is enough; the header propagates to all child pages without touching each page file individually.

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head><title>Little Lemon</title></head>
<body style="background-color: #f0f0f0;">
    {% include "partials/_header.html" %}
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>

<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
<p>Welcome to Little Lemon.</p>
<p>We serve the finest Mediterranean cuisine.</p>
{% endblock %}
```

```bash
python manage.py runserver 8080
# Visit http://127.0.0.1:8080/home/ -- background color from base.html is inherited
# Visit http://127.0.0.1:8080/about/ -- same layout, different block content
```

#### Exercise: Working with Templates

Folder: [`lab/13-django-template-inheritance/`](./lab/13-django-template-inheritance/).

- Added `STATICFILES_DIRS = ["myproject/static",]` to `settings.py` so Django can locate project-level static assets.
- Created four view functions (`home`, `about`, `menu`, `book`) in `views.py`, each rendering its corresponding HTML template via `render()`.
- Created `templates/partials/_header.html` as a reusable partial that loads static files and renders a `<header>` with the logo image and a `<nav>` with links to all four pages using `{% url %}` tags.
- Updated `templates/base.html` to `{% include 'partials/_header.html' %}` inside the `<body>` and to wrap the main content area with `{% block content %}{% endblock %}`, making it the shared layout for all pages.
- Updated each child template (`index.html`, `about.html`, `menu.html`, `book.html`) to use `{% extends 'base.html' %}`, `{% load static %}`, and `{% block content %}` so they inherit the base layout and only define their own page content.

```python
# -- settings.py
STATIC_URL = 'static/'

STATICFILES_DIRS = ["myproject/static",]

# -- views.py
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')
```

```html
<!-- templates/menu.html -->

{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> Menu</p>
<p> This is a Menu page for Little Lemon </p>
{% endblock %}

<!-- templates/index.html -->
{% extends 'base.html'%}
{% load static %}
{% block content%}
<p> Home</p>
<p> This is the Home page for Little Lemon </p>
{% endblock %}

<!-- templates/book.html -->
{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> Book</p>
<p> This is a Booking page for Little Lemon </p>
{% endblock %}

<!-- templates/about.html -->
{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> About Us</p>
<p> This is an About page for Little Lemon </p>

{% endblock %}

<!-- templates/base.html -->
    <!-- Add include tag -->
    {% include 'partials/_header.html' %}


    <main>
        <!-- Begin block content --> 

        {% block content%}
        {% endblock %}
        
        <!-- End block content -->
    </main>

<!-- templates/partials/_header.html -->
{% load static %}
<footer style="background-color: #EE9972; "></footer>
<header>
  <img src="{% static 'img/logo.png' %}" />
</header>
  <nav>
    <ul>
      <li><a href="{% url 'home' %}">Home</a></li>
      <li><a href="{% url 'about' %}">About</a></li>
      <li><a href="{% url 'menu' %}">Menu</a></li>
      <li><a href="{% url 'book' %}">Book</a></li> 
    </ul>
  </nav>
```

### Debugging and Testing

#### Debugging Django Applications

- Debugging means identifying, isolating, and fixing errors; web projects are harder to debug than standalone files because of interlinked files and dependencies.
- Common Django mistakes include: missing a view, incorrect template names, missing import statements, inaccessible model data, and missing commas in function arguments.
- Django's built-in debugger is enabled by `DEBUG = True` in `settings.py` and displays as a yellow error page in the browser.
  - It must be set to `DEBUG = False` in production because it exposes internal file paths, database details, and project configuration to end users.
- Two categories of errors by where they surface:
  - **Console log errors** -- Python-level errors (e.g., `NameError: name 'x' is not defined`) appear in the terminal after the server reloads; the page will fail to load.
  - **Silent errors** -- missing imports or incorrect template context may cause the page to render partially with no console error; always verify imports and function arguments.
- **Django yellow page errors** are framework-level and more specific to Django internals than raw Python errors:
  - Missing CSRF token -> `403 Forbidden: CSRF verification failed`.
  - Wrong template name in `render()` -> `TemplateDoesNotExist` with the searched paths listed.
  - The yellow page includes the exception location, a traceback stack with the offending line highlighted, HTTP request META headers, and current settings values.
  - A "copy and paste view" switch provides a cleaner, shareable traceback text.
- No single rule covers all debugging scenarios; systematic practice gradually reduces the frequency of errors.

#### Testing in Django

- Testing focuses on quality, reliability, and performance; debugging focuses on removing errors and bugs -- both are distinct parts of the software development lifecycle (SDLC).
- Unit testing (UT) isolates the smallest testable unit (a function, class, or method) and produces a pass, fail, or error result.
- Django integrates Python's built-in `unittest` module using a class-based approach via `django.test.TestCase`.
  - Each test class inherits from `TestCase`.
  - `setUpTestData()` is a `@classmethod` that creates shared fixture data once for the entire class, improving performance over per-test `setUp()`.
  - Individual test methods start with `test_` and use `assert*` helpers such as `assertIsInstance()`.
- Test output in the terminal: a dot (`.`) per passing test, `F` for failure, `E` for error; an `AssertionError` message is printed for failures.
- Test file naming conventions:
  - Small projects: a single `tests.py` inside the app directory.
  - Large projects: multiple files such as `test_models.py` and `test_views.py` inside the app directory.
- `manage.py test` command variants for scoping test runs:
  - All tests: `python manage.py test`
  - All tests in an app: `python manage.py test reservations`
  - Specific test case class: `python manage.py test reservations.tests.ReservationTestCase`
  - Specific test method: `python manage.py test reservations.tests.ReservationTestCase.test_seat_count`

```python
# models.py
from django.db import models

class Reservation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    booking_time = models.DateTimeField(auto_now=True)  # auto-set to current time on save

# tests.py
import datetime
from django.test import TestCase
from .models import Reservation

class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create(
            first_name="John",
            last_name="Smith",
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, str)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.booking_time, datetime.datetime)
```

#### Sub-Classing Generic Views

Django supports two styles of views: function-based views (FBVs) and class-based views (CBVs). CBVs extend `django.views.View`, define `get()` and `post()` methods, and are wired to URLs via `as_view()`.

```python
# views.py
from django.views import View
from django.http import HttpResponse

class NewView(View):
    def get(self, request):
        return HttpResponse('response')
```

```python
# urls.py
from myapp.views import NewView

urlpatterns = [
    path('about/', NewView.as_view()),
]
```

##### Function-Based vs Class-Based Views

A function-based view for rendering a template looks like this:

```python
# views.py -- function-based
from django.http import HttpResponse
from django import template

def index(request):
    t = template.loader.get_template('myapp/index.html')
    return HttpResponse(t.render({}, request))
```

```python
# myapp/urls.py
path('/', views.index, name='index')
```

```python
# myproject/urls.py
urlpatterns = [
    path('myapp/', include('myapp.urls')),
]
```

The equivalent using `TemplateView` is much shorter -- just set `template_name`:

```python
# views.py -- class-based
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
```

```python
# urls.py
path('/', IndexView.as_view(), name='index')
```

**Advantages and disadvantages of each style:**

| | Function-Based Views | Class-Based Views |
|---|---|---|
| **Pros** | Simple, explicit flow, easy to read, decorators work directly, good for one-off logic | Code reuse (DRY (Don't Repeat Yourself)), per-method dispatch, extensible, built-in generic views |
| **Cons** | Hard to extend/reuse, HTTP method branching via `if` | Harder to read, implicit flow, decorators need `method_decorator` or override |

##### Generic Views for CRUD Operations

Django's generic CBVs handle common patterns automatically. The most frequently used are:

- `TemplateView` -- renders a template
- `CreateView` -- form to create a new model instance
- `ListView` -- renders a list of model objects
- `DetailView` -- renders a single model object
- `UpdateView` -- form to update an existing model instance
- `DeleteView` -- confirmation form to delete a model instance
- `LoginView` -- built-in authentication login

**Requirements for any generic view:**

- Set `model` to the model class the view operates on.
- Each generic view looks for a template named `<modelname>_<suffix>.html` by default (e.g., `employee_list.html` for `ListView`).
- Map the view to a URL using `as_view()`.

The examples below use this `Employee` model:

```python
# models.py
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = "Employee"
```

##### CreateView

`CreateView` auto-generates a model form and saves the submitted data. The default template name is `employee_form.html`.

```python
# views.py
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee-list')  # redirect after successful save
```

```python
# urls.py
path('create/', EmployeeCreate.as_view(), name='EmployeeCreate'),
```

```html
<!-- templates/employee_form.html -->
<form method="post">
    {% csrf_token %}
    <table>{{ form.as_table }}</table>
    <input type="submit" value="Save">
</form>
```

When the client visits `/create/`, the form is displayed. On submission, the employee is saved in the `Employee` table and the user is redirected to `success_url`.

##### ListView

`ListView` fetches all model objects and passes them to the template as `object_list`. The default template name is `employee_list.html`.

```python
# views.py
from django.views.generic.list import ListView

class EmployeeList(ListView):
    model = Employee
```

```html
<!-- templates/employee_list.html -->
<ul>
    {% for object in object_list %}
    <li>Name: {{ object.name }}</li>
    <li>Email: {{ object.email }}</li>
    <li>Contact: {{ object.contact }}</li>
    <br/>
    {% endfor %}
</ul>
```

Visiting `http://localhost:8000/employees/list` lists all rows in the `Employee` table.

##### DetailView

`DetailView` fetches a single object by primary key (passed in the URL) and passes it to the template as `object`. The default template name is `employee_detail.html`.

```python
# urls.py
path('show/<int:pk>/', EmployeeDetail.as_view(), name='EmployeeDetail'),
```

```html
<!-- templates/employee_detail.html -->
<h1>Name: {{ object.name }}</h1>
<p>Email: {{ object.email }}</p>
<p>Contact: {{ object.contact }}</p>
```

Visiting `/employees/show/1/` displays the `Employee` with `pk=1`.

##### UpdateView

`UpdateView` pre-fills a model form with an existing instance's data and saves changes on submission. The default template name is `employee_update_form.html`.

```python
# views.py
from django.views.generic.edit import UpdateView

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee-list')
```

```python
# urls.py
path('update/<int:pk>/', EmployeeUpdate.as_view(), name='EmployeeUpdate'),
```

```html
<!-- templates/employee_update_form.html -->
<form method="post">
    {% csrf_token %}
    <table>{{ form.as_table }}</table>
    <input type="submit" value="Save">
</form>
```

##### DeleteView

`DeleteView` displays a confirmation page before deleting the model instance. The default template name is `employee_confirm_delete.html`.

```python
# views.py
from django.views.generic.edit import DeleteView

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee-list')
```

```python
# urls.py
path('delete/<int:pk>/', EmployeeDelete.as_view(), name='EmployeeDelete'),
```

```html
<!-- templates/employee_confirm_delete.html -->
<form method="post">
    {% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    <input type="submit" value="Confirm">
</form>
```

Generic views require significantly less boilerplate than FBVs for standard CRUD operations, but FBVs remain preferable for highly customized or one-off logic.

#### Additional Resources

- [Testing in Django official](https://docs.djangoproject.com/en/4.1/topics/testing/)
- [Testing overview -- Django official](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)
- [Django Advanced Testing topics](https://docs.djangoproject.com/en/4.1/topics/testing/advanced/#advanced-testing-topics)
- [Django META header](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.META)
- [Add unit testing to your Django project](https://docs.djangoproject.com/en/4.1/internals/contributing/writing-code/unit-tests/)
- [Adding Django apps -- Extended information](https://docs.djangoproject.com/en/4.1/ref/applications/)


## 5. Summary and Project

### Project Goals

#### Purpose of the Assessments

The primary purpose of the assessments is to check your knowledge and understanding of the key learning objectives of the course. They help you identify which topics you have mastered and which require further focus. The graded assessments are designed to confirm that you can apply what you have learned.

#### Graded Quiz

The quiz covers only the topics from the course -- no surprises. Review the feedback on your answers and revisit any topics that need more attention.

#### Little Lemon Django Project

All course exercises, knowledge checks, and in-video questions build toward this final project, so nothing in it will be outside the scope of what you have already learned.

**Scenario:** Little Lemon is a neighborhood bistro serving simple food and classic cocktails in a casual environment, with a locally sourced menu and daily specials. The restaurant is transitioning from a static one-page website to a database-driven web application built with Django.

**Current state:** The Home, About, and Book pages are already completed.

**What you need to build -- the Menu feature:**

- Store menu information in a database so it can be updated as the menu changes seasonally.
- Allow managers to add or update menu items by editing the name, description, price, and photo.
- Display each menu item on a dedicated page that loads when a user clicks on it from the Menu page.

### Project

Folder: [`lab/14-django-project/`](./lab/14-django-project/).

**Summary:** Built the Menu and Menu Item pages for the Little Lemon restaurant Django project. Created the `Menu` model with `name`, `price`, and `menu_item_description` fields; registered both models in Django admin; added `menu()` and `display_menu_item()` view functions that query the database and pass context to templates; wired URL patterns for `/menu/` and `/menu_item/<pk>/`; created `menu.html` listing all items as clickable links with prices, and `menu_item.html` displaying the full detail (name, description, price, image) of a single item; implemented the `_footer.html` partial with the logo and copyright notice; and included the footer in `base.html` via a DTL `{% include %}` tag.

#### Solution

##### `restaurant/models.py`

```python
from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name
```

##### `restaurant/admin.py`

```python
from django.contrib import admin
from .models import Menu
from .models import Booking

admin.site.register(Menu)
admin.site.register(Booking)
```

##### `restaurant/views.py`

```python
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})
```

##### `restaurant/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]
```

##### `restaurant/templates/menu.html`

```html
{% extends 'base.html' %}
{% load static %}
{% block content %}
<h1>Menu</h1>
<!--Begin col-->
<div class="column">
    {% for item in menu.menu %}
    <p>
        <a href="{% url 'menu_item' pk=item.pk %}">
            {{ item.name }}
        </a>
        <span class="menu-price">
            ${{ item.price }}.00
        </span>
    </p>
    {% endfor %}
</div>
<!--End col-->
{% endblock %}
```

##### `restaurant/templates/menu_item.html`

```html
{% extends 'base.html' %}
{% load static %}
{% block content %}
<section>
   <article>
      <h1>Menu item</h1>
      <span>
         <a href="{% url 'home' %}">Home</a> /
         <a href="{% url 'menu' %}">Menu</a> /
         {{ menu_item.name }}
      </span>
      <!--Begin row-->
      <div class="row">
         <!--Begin col-->
         <div class="column">
            <h2>{{ menu_item.name }}</h2>
            <p>{{ menu_item.menu_item_description }}</p>
            <p>Price: ${{ menu_item.price }}.00</p>
         </div>
         <!--End col-->
         <!--Begin col-->
         <div class="column">
            <img src="/restaurant/static/img/menu_items/{{ menu_item.name }}.jpg" alt="{{ menu_item.name }}" />
         </div>
         <!--End col-->
      </div>
      <!--End row-->
   </article>
</section>
{% endblock %}
```

##### `restaurant/templates/partials/_footer.html`

```html
{% load static %}
<footer>
  <article>
    <img src="{% static 'img/logo_footer.png' %}" />
  </article>
  <article>
    <p>Copyright Little Lemon</p>
  </article>
</footer>
```

##### `restaurant/templates/base.html` -- footer include

```html
    <!--Footer content-->
    {% include 'partials/_footer.html' %}
```

#####  Shell Commands and Adding Menu Items

```bash
# Run inside the littlelemon/ directory (where manage.py lives)

# Apply model migrations
python manage.py makemigrations
python manage.py migrate

# Create a Django admin superuser
python manage.py createsuperuser
# Username: bistroadmin | Email: admin@littlelemon.com | Password: lemon@786!

# Start the development server
python manage.py runserver 8080
# Open http://127.0.0.1:8080/
```

To add menu items, open `http://127.0.0.1:8080/admin/`, log in with the superuser credentials, and add menu items with names, prices, and descriptions. The menu item images should be in `restaurant/static/img/menu_items/` with filenames matching the menu item names.

- Greek salad (`menu_items/Greek salad.jpg`)
- Bruschetta (`menu_items/Bruschetta.jpg`)
- Lemon dessert (`menu_items/Lemon dessert.jpg`)
- Grilled fish (`menu_items/Grilled fish.jpg`)

The menu item names and the image filenames must match, since the `menu_item.html` template uses the menu item name to construct the image path:

```html
<img src="/restaurant/static/img/menu_items/{{ menu_item.name }}.jpg" alt="{{ menu_item.name }}" />
```

## Extra: Authentication and Authorization

References:
- [Authentication Overview](https://docs.djangoproject.com/en/5.2/topics/auth/)
- [Using the Authentication System](https://docs.djangoproject.com/en/5.2/topics/auth/default/)
- [Password Management](https://docs.djangoproject.com/en/5.2/topics/auth/passwords/)

- Django's authentication system handles both **authentication** (verifying identity) and **authorization** (determining what an authenticated user may do).
- It ships as `django.contrib.auth` and is enabled by default; it provides users, passwords, permissions, groups, and a pluggable backend system.
- The system deliberately does *not* include login throttling, OAuth, or object-level permissions -- those come from third-party packages (e.g., `django-allauth`, `django-guardian`).

### Setup

- `django.contrib.auth` and `django.contrib.contenttypes` must be in `INSTALLED_APPS`.
- `SessionMiddleware` and `AuthenticationMiddleware` must be in `MIDDLEWARE`.
- Both are present by default in any project created with `django-admin startproject`.

```python
# settings.py -- defaults, shown for reference
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",           # auth models, backends, signals
    "django.contrib.contenttypes",   # required by the permission system
    ...
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # sets request.user
    ...
]
```

```bash
python manage.py migrate   # creates auth_user, auth_permission, auth_group tables
```

### The User Model

- `django.contrib.auth.models.User` is the built-in user model; it covers the vast majority of standard use cases.
- Key fields: 
  - `username`,
  - `password` (always stored hashed), 
  - `email`, 
  - `first_name`, 
  - `last_name`, 
  - `is_active`, 
  - `is_staff`, 
  - `is_superuser`, 
  - `date_joined`, 
  - `last_login`.
- Key methods: 
  - `is_authenticated` (always `True` for real users),
  - `has_perm(perm)`,
  - `has_perms(perm_list)`,
  - `has_module_perms(app_label)`,
  - `set_password(raw)`,
  - `check_password(raw)`.

```python
from django.contrib.auth.models import User

# Create a regular user -- use create_user(), never User.objects.create()
# create_user() hashes the password automatically.
user = User.objects.create_user("john", "john@example.com", "s3cr3t!")
user.first_name = "John"
user.save()

# Create a superuser (has all permissions without explicit assignment)
User.objects.create_superuser("admin", "admin@example.com", "adminpass")
```

```bash
# Equivalent shell commands
python manage.py createsuperuser
python manage.py changepassword john
```

```python
# Changing a password programmatically
user = User.objects.get(username="john")
user.set_password("newpassword")   # hashes and sets; never assign user.password directly
user.save()

# Verifying a password (e.g., in a custom flow)
user.check_password("newpassword")  # True
```

### Authentication: `authenticate()`, `login()`, `logout()`

- `authenticate()` checks credentials against all configured `AUTHENTICATION_BACKENDS` and returns a `User` or `None`.
- `login()` persists the authenticated user in the session; `logout()` wipes the session entirely.
- Never call `login()` without first calling `authenticate()` -- `authenticate()` sets an internal `backend` attribute that `login()` requires.

```python
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)          # writes user.id into the session
            return redirect("home")
        # credentials invalid -- fall through to re-render form with error
    return render(request, "registration/login.html")

def logout_view(request):
    logout(request)    # clears session data; safe to call even if not logged in
    return redirect("home")
```

### Restricting Access to Views

- `request.user` is always populated: it is a `User` instance for authenticated users or an `AnonymousUser` otherwise.
- Use `request.user.is_authenticated` for inline checks; use the `@login_required` decorator for the common redirect pattern.

```python
# Inline check
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/login/?next=/dashboard/")
    ...
```

```python
from django.contrib.auth.decorators import login_required

# Redirects unauthenticated users to settings.LOGIN_URL ("/accounts/login/" by default)
# and appends ?next=<current_path> so the user is returned after login.
@login_required
def dashboard(request):
    ...

# Custom login URL or redirect field
@login_required(login_url="/my-login/", redirect_field_name="return_to")
def secret(request):
    ...
```

```python
# settings.py -- override defaults
LOGIN_URL = "/accounts/login/"          # default
LOGIN_REDIRECT_URL = "/dashboard/"      # where to go after login if no ?next=
LOGOUT_REDIRECT_URL = "/"              # where to go after logout
```

#### Class-Based Views

- `LoginRequiredMixin` provides the same behaviour as `@login_required` for CBVs; it must be listed *first* in the MRO.

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class DashboardView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "next"

    def get(self, request):
        ...
```

#### Custom Test with `@user_passes_test`

- `@user_passes_test` redirects if a callable returns `False` for the request user; useful for arbitrary conditions beyond authentication.

```python
from django.contrib.auth.decorators import user_passes_test

def is_editor(user):
    return user.groups.filter(name="Editors").exists()

@user_passes_test(is_editor, login_url="/no-access/")
def editor_dashboard(request):
    ...
```

### Permissions

- Django automatically creates four permissions per model on every `migrate`: `add_<model>`, `change_<model>`, `delete_<model>`, `view_<model>`.
- Permissions are checked with `user.has_perm("app_label.codename")`; this returns `False` for inactive users.
- **Permission caching:** permissions are fetched from the DB once and cached on the user object for the lifetime of the request. If you grant a permission and then check in the same request, re-fetch the user.

```python
from django.contrib.auth.models import User

user = User.objects.get(pk=1)

# Model-level permission check
user.has_perm("myapp.change_article")   # True/False
user.has_perm("myapp.add_article")

# Multiple at once (all must be held)
user.has_perms(["myapp.add_article", "myapp.change_article"])

# App-level check (user has *any* permission in the app)
user.has_module_perms("myapp")
```

#### `@permission_required` Decorator

```python
from django.contrib.auth.decorators import login_required, permission_required

# Single permission
@permission_required("myapp.change_article")
def edit_article(request, pk):
    ...

# Multiple permissions (user must hold all of them)
@permission_required(["myapp.view_article", "myapp.change_article"])
def edit_article(request, pk):
    ...

# Raise 403 instead of redirecting to login (use after @login_required
# to avoid a redirect loop for authenticated-but-unauthorised users)
@login_required
@permission_required("myapp.change_article", raise_exception=True)
def edit_article(request, pk):
    ...
```

```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class ArticleEditView(PermissionRequiredMixin, View):
    permission_required = "myapp.change_article"
    raise_exception = True          # 403 instead of login redirect

    # For multiple permissions:
    # permission_required = ["myapp.view_article", "myapp.change_article"]
```

#### Custom Permissions

- Declare extra permissions in the model's `Meta.permissions`; they are created during `migrate`.

```python
class Article(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_publish", "Can publish articles"),
            ("can_archive", "Can archive articles"),
        ]
```

```python
# Assign custom permission programmatically
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Article

ct = ContentType.objects.get_for_model(Article)
perm = Permission.objects.get(codename="can_publish", content_type=ct)
user.user_permissions.add(perm)
```

### Groups

- A `Group` is a named collection of permissions; every user in the group inherits the group's permissions.
- Groups are the idiomatic way to manage role-based access control in Django.

```python
from django.contrib.auth.models import Group, Permission

# Create group and attach permissions
editors = Group.objects.create(name="Editors")
publish_perm = Permission.objects.get(codename="can_publish")
editors.permissions.add(publish_perm)

# Assign user to group
user.groups.add(editors)

# Effective permission is union of direct + group permissions
user.has_perm("myapp.can_publish")   # True (via group)
```

### Built-in Auth Views and URLs

- Django provides a complete set of ready-made auth views; include them with a single `path()` call.
- Override only the templates -- place them in `templates/registration/`.

```python
# project urls.py
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
```

Registered URL names:

| URL | Name |
|---|---|
| `accounts/login/` | `login` |
| `accounts/logout/` | `logout` |
| `accounts/password_change/` | `password_change` |
| `accounts/password_change/done/` | `password_change_done` |
| `accounts/password_reset/` | `password_reset` |
| `accounts/password_reset/done/` | `password_reset_done` |
| `accounts/reset/<uidb64>/<token>/` | `password_reset_confirm` |
| `accounts/reset/done/` | `password_reset_complete` |

```python
# Override individual views with custom templates or behaviour
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="myapp/login.html"),
        name="login",
    ),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="myapp/password_change.html",
            success_url="/dashboard/",
        ),
        name="password_change",
    ),
]
```

Minimal `registration/login.html` template:

```html
{% extends "base.html" %}
{% block content %}
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log in</button>
  <input type="hidden" name="next" value="{{ next }}">
</form>
<a href="{% url 'password_reset' %}">Forgot password?</a>
{% endblock %}
```

### Built-in Auth Forms

- Django's auth forms handle validation, password hashing, and error messages -- use them directly in custom views.

```python
from django.contrib.auth.forms import (
    UserCreationForm,       # new user signup
    AuthenticationForm,     # login (wraps authenticate())
    PasswordChangeForm,     # change password (requires old password)
    SetPasswordForm,        # set password without old (used in reset flow)
    PasswordResetForm,      # sends reset email
)
```

```python
# Custom signup view using UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
```

```python
# Extend UserCreationForm to add extra fields (e.g. email)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
```

### Password Management

- Passwords are stored using PBKDF2-SHA256 by default; the algorithm is configurable via `PASSWORD_HASHERS`.
- `set_password()` hashes and stores; `check_password()` verifies a plain-text string against the stored hash.
- After a password change, the current session's auth hash is invalidated -- call `update_session_auth_hash()` to keep the user logged in.

```python
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Without this call, the user is logged out immediately
            # because the session's password hash no longer matches.
            update_session_auth_hash(request, form.user)
            return redirect("password_change_done")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "registration/password_change_form.html", {"form": form})
```

```python
# settings.py -- password validation rules (shown to the user on signup/change)
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
     "OPTIONS": {"min_length": 10}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
```

### Authentication in Templates

- `request.user` is available in all templates when `django.template.context_processors.request` and `django.contrib.auth.context_processors.auth` are enabled (both are on by default).
- `perms` is a template proxy that checks permissions lazily without extra DB queries.

```html
{% if user.is_authenticated %}
    <p>Hello, {{ user.username }} -- <a href="{% url 'logout' %}">Log out</a></p>
{% else %}
    <a href="{% url 'login' %}">Log in</a>
{% endif %}

{% if perms.myapp.can_publish %}
    <a href="{% url 'publish' %}">Publish</a>
{% endif %}

{% if perms.myapp %}
    <!-- user has at least one permission in myapp -->
{% endif %}
```

### Authentication Backends

- `AUTHENTICATION_BACKENDS` is an ordered list of dotted paths; `authenticate()` tries each in turn.
- The default backend (`ModelBackend`) queries `auth_user` by username and verifies the password hash.
- Custom backends enable alternative login strategies (e.g., email login, LDAP, token-based) without touching views.

```python
# myapp/backends.py -- allow login by email instead of username
from django.contrib.auth.models import User

class EmailBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        return user.is_active
```

```python
# settings.py
AUTHENTICATION_BACKENDS = [
    "myapp.backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",  # fallback to username
]
```

### Password Strength Measurement

- Django's built-in `AUTH_PASSWORD_VALIDATORS` are **pass/fail only** -- each validator either raises a `ValidationError` or accepts the password; none returns a score or strength level.
- The four built-in validators and what they check:

| Validator | What it checks |
|---|---|
| `UserAttributeSimilarityValidator` | Password is not too similar to username, email, or name |
| `MinimumLengthValidator` | Password meets a minimum character count (default: 8) |
| `CommonPasswordValidator` | Password is not in the list of ~20,000 common passwords |
| `NumericPasswordValidator` | Password is not entirely numeric |

- For an actual strength score, use **zxcvbn** -- it estimates crack time and returns a 0–4 score without enforcing a hard reject.

```bash
pip install zxcvbn
```

```python
from zxcvbn import zxcvbn

result = zxcvbn("correcthorsebatterystaple", user_inputs=["john", "example.com"])
print(result["score"])          # 3  (0 = very weak, 4 = very strong)
print(result["crack_times_display"]["offline_slow_hashing_1e4_per_second"])
# "centuries"
print(result["feedback"]["suggestions"])
# ["Add another word or two. Uncommon words are better."]
```

- The typical pattern is to combine both: run `zxcvbn.js` on the client for a live strength bar (advisory UX, no server round-trip), and keep `AUTH_PASSWORD_VALIDATORS` on the server for the hard reject on form submission.

```html
<!-- signup.html -- live strength bar with zxcvbn.js -->
<input type="password" id="id_password1" name="password1">
<div id="strength-bar"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/zxcvbn/4.4.2/zxcvbn.js"></script>
<script>
  const labels = ["Very weak", "Weak", "Fair", "Strong", "Very strong"];
  document.getElementById("id_password1").addEventListener("input", function () {
    const result = zxcvbn(this.value);
    document.getElementById("strength-bar").textContent = labels[result.score];
  });
</script>
```

```python
# Optional: enforce a minimum zxcvbn score server-side with a custom validator
from django.core.exceptions import ValidationError
from zxcvbn import zxcvbn

class ZxcvbnValidator:
    MIN_SCORE = 2

    def validate(self, password, user=None):
        user_inputs = [user.username, user.email] if user else []
        if zxcvbn(password, user_inputs=user_inputs)["score"] < self.MIN_SCORE:
            raise ValidationError("This password is too weak.")

    def get_help_text(self):
        return "Your password must have a strength score of at least 2 out of 4."
```

```python
# settings.py -- plug the custom validator in alongside the built-ins
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "myapp.validators.ZxcvbnValidator"},
]
```

## Extra: Security

References:
- [Django Security Overview](https://docs.djangoproject.com/en/5.2/topics/security/)
- [Security Middleware](https://docs.djangoproject.com/en/5.2/ref/middleware/#security-middleware)
- [CSRF Protection](https://docs.djangoproject.com/en/5.2/ref/csrf/)
- [Clickjacking Protection](https://docs.djangoproject.com/en/5.2/ref/clickjacking/)

- Django addresses many of the [OWASP Top 10 vulnerabilities](https://owasp.org/Top10/2025/) by default; some require explicit configuration in production.
- The built-in `SecurityMiddleware` (`django.middleware.security.SecurityMiddleware`) should be the **first** entry in `MIDDLEWARE` so SSL redirects fire before any other processing.

### OWASP Top 10 and Django Coverage

- The [OWASP Top 10](https://owasp.org/Top10/) (2021 edition) is the industry-standard ranking of the most critical web application security risks.
- Django addresses several entries natively; others are architectural concerns or require third-party packages.

| # | Vulnerability | Django coverage |
|---|---|---|
| A01 | **Broken Access Control** -- users acting outside intended permissions | Partial -- permission system, `@login_required`, `@permission_required`; object-level access is your responsibility |
| A02 | **Cryptographic Failures** -- sensitive data exposed via weak/missing encryption | Partial -- passwords hashed with PBKDF2 by default; TLS/HTTPS config is yours |
| A03 | **Injection** -- SQL, NoSQL, command, LDAP injection via untrusted input | Strong -- ORM parameterizes all queries; risk only with `raw()` / `cursor.execute()` |
| A04 | **Insecure Design** -- flawed architecture and threat modelling | None -- framework-agnostic design concern |
| A05 | **Security Misconfiguration** -- default credentials, verbose errors, open storage | Partial -- `check --deploy` catches many issues; `DEBUG`, `ALLOWED_HOSTS`, `SECURE_*` are yours |
| A06 | **Vulnerable and Outdated Components** -- libraries with known CVEs | None -- use `pip audit` or Dependabot externally |
| A07 | **Identification and Authentication Failures** -- weak sessions, credential stuffing | Partial -- session management and password hashing are solid; throttling and MFA require third-party packages |
| A08 | **Software and Data Integrity Failures** -- unsigned updates, insecure deserialization | Partial -- `SECRET_KEY` signs sessions/tokens; pickle deserialization in cache backends is a risk |
| A09 | **Security Logging and Monitoring Failures** -- no audit trail for breaches | None -- Django logging is general-purpose; security-specific audit logging is your responsibility |
| A10 | **Server-Side Request Forgery (SSRF)** -- server fetches attacker-controlled URLs | None -- any code that fetches a user-supplied URL needs manual validation |

- Gaps not covered by Django natively: insecure design (A04), outdated dependencies (A06), SSRF (A10), audit logging (A09), and MFA / brute-force throttling (A07).
- Useful third-party packages for the gaps: `django-axes` (login throttling), `django-allauth` (MFA/OAuth), `pip-audit` (CVE scanning), `django-auditlog` (audit trail).

### Cross-Site Scripting (XSS)

- Django templates **auto-escape** `<`, `>`, `"`, `'`, and `&` in every `{{ variable }}` expression -- this is on by default and covers the common case.
- Escaping is **not** applied when using `{% autoescape off %}`, the `|safe` filter, or `mark_safe()` in Python; use these only for trusted, developer-controlled content.

```python
from django.utils.html import mark_safe, escape, format_html

# SAFE -- format_html escapes all arguments and returns a SafeString
def render_link(url, label):
    return format_html('<a href="{}">{}</a>', url, label)

# UNSAFE -- never interpolate user data directly into a SafeString
def bad(label):
    return mark_safe(f"<b>{label}</b>")   # XSS if label is user-supplied

# Manual escaping when you must build HTML in Python without format_html
safe_label = escape(user_label)
```

```django
{# Template: variable is escaped automatically #}
{{ user_comment }}

{# Only use |safe for values you fully control #}
{{ trusted_html_from_admin|safe }}

{# Block-level escape control #}
{% autoescape off %}
    {{ definitely_safe_content }}
{% endautoescape %}
```

### Cross-Site Request Forgery (CSRF)

- `CsrfViewMiddleware` embeds a per-session secret token in every form and validates it on every state-changing request (POST, PUT, PATCH, DELETE).
- The token is stored in a cookie; the middleware compares it against the `csrfmiddlewaretoken` field in POST data or the `X-CSRFToken` header.

```django
{# Every HTML form must include the token tag #}
<form method="post">
  {% csrf_token %}
  ...
</form>
```

```python
import requests

# AJAX -- pass the token in a custom header
# Fetch the cookie value in JS: document.cookie, then:
# headers: { "X-CSRFToken": csrftoken }

# Exempt a view from CSRF (use sparingly -- only for public APIs with their own auth)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    ...
```

```python
# settings.py -- harden CSRF cookies in production
CSRF_COOKIE_SECURE = True       # send cookie only over HTTPS
CSRF_COOKIE_HTTPONLY = False    # JS must be able to read it to include in AJAX headers
CSRF_TRUSTED_ORIGINS = [        # required when behind a proxy or using non-standard ports
    "https://example.com",
]
```

### SQL Injection

- Django's ORM uses **parameterized queries** for all `QuerySet` operations -- user-supplied values are never interpolated into SQL strings.
- Risk surfaces -- all accept raw SQL where injection is possible:
  - `QuerySet.raw()`
  - `connection.execute()`
  - `QuerySet.extra()`
  - `RawSQL()`

```python
# SAFE -- ORM parameterizes automatically
Article.objects.filter(title=user_input)

# SAFE -- raw() with parameter list; %s placeholders are never formatted as strings
Article.objects.raw("SELECT * FROM article WHERE title = %s", [user_input])

# UNSAFE -- string formatting bypasses parameterization
Article.objects.raw(f"SELECT * FROM article WHERE title = '{user_input}'")

# SAFE -- executing raw SQL via the connection cursor
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM article WHERE title = %s", [user_input])
    rows = cursor.fetchall()
```

### Clickjacking (`X-Frame-Options`)

- `XFrameOptionsMiddleware` adds the `X-Frame-Options: DENY` header to every response, preventing the page from being embedded in a `<frame>` or `<iframe>` on another site.
- Override per-view when embedding is intentional (e.g., a widget meant to be iframed).

```python
# settings.py -- DENY (default) or SAMEORIGIN
X_FRAME_OPTIONS = "DENY"        # no framing allowed at all
# X_FRAME_OPTIONS = "SAMEORIGIN"  # allow framing by same origin only
```

```python
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin

@xframe_options_exempt           # allow all framing (e.g. an embeddable widget)
def embeddable_widget(request):
    ...

@xframe_options_sameorigin       # override the global DENY for this view only
def internal_dashboard(request):
    ...
```

### HTTPS and `SecurityMiddleware`

- All `SECURE_*` settings are read by `SecurityMiddleware`; they are **all off by default** and must be enabled for production.
- Enable `SECURE_SSL_REDIRECT` at the Django level only if your reverse proxy does not handle it -- doing it at the proxy is more efficient.

```python
# settings.py -- production HTTPS hardening
SECURE_SSL_REDIRECT = True              # 301-redirect all HTTP -> HTTPS
SECURE_PROXY_SSL_HEADER = (             # trust this header from the reverse proxy
    "HTTP_X_FORWARDED_PROTO", "https"   # misconfiguring this is a CSRF attack surface
)

# HTTP Strict Transport Security -- tells browsers to refuse plain HTTP for N seconds
SECURE_HSTS_SECONDS = 31_536_000        # 1 year; start with 3600 while testing
SECURE_HSTS_INCLUDE_SUBDOMAINS = True   # apply to all subdomains
SECURE_HSTS_PRELOAD = True              # opt into browser HSTS preload lists

# Cookie transport security
SESSION_COOKIE_SECURE = True            # session cookie only over HTTPS
CSRF_COOKIE_SECURE = True               # CSRF cookie only over HTTPS
SESSION_COOKIE_HTTPONLY = True          # JS cannot read session cookie (default True)

# Security response headers
SECURE_CONTENT_TYPE_NOSNIFF = True      # X-Content-Type-Options: nosniff
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"  # Referrer-Policy header
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"           # COOP header
```

```python
# MIDDLEWARE -- SecurityMiddleware must be first
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",   # <- first
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

### Host Header Validation

- Django validates the `Host` header against `ALLOWED_HOSTS` in every call to `request.get_host()`; requests with unrecognised hosts raise `SuspiciousOperation` (HTTP 400).
- Bypassing `get_host()` by accessing `request.META["HTTP_HOST"]` directly skips validation -- never do this.

```python
# settings.py
ALLOWED_HOSTS = [
    "example.com",
    "www.example.com",
    ".example.com",   # leading dot matches all subdomains
]
# DEBUG = True implicitly adds "localhost", "127.0.0.1" -- never use DEBUG=True in production

# If the reverse proxy forwards the original Host via X-Forwarded-Host:
USE_X_FORWARDED_HOST = True   # then also add that host to ALLOWED_HOSTS
```

### Session Security

- Sessions are stored server-side by default (database backend); only the session key is sent to the browser in a cookie -- no sensitive data is exposed.
- Critical settings prevent session cookies from leaking over plain HTTP or being read by JavaScript.

```python
# settings.py
SESSION_COOKIE_SECURE = True      # HTTPS only
SESSION_COOKIE_HTTPONLY = True    # inaccessible to JavaScript (default True)
SESSION_COOKIE_SAMESITE = "Lax"   # "Strict" / "Lax" / "None"; mitigates CSRF further
SESSION_COOKIE_AGE = 1209600      # seconds (default 2 weeks); reduce for sensitive apps
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # session deleted when browser closes

# Prevent session fixation: regenerate session key after login
# Django does this automatically in contrib.auth.login()
```

```python
# Manually cycle the session key (e.g. after privilege escalation)
request.session.cycle_key()
```

### Secret Key

- `SECRET_KEY` is used to sign cookies, sessions, CSRF tokens, and password-reset links -- if it leaks, all of these can be forged.
- Rotate the key without immediately invalidating existing sessions by listing old keys in `SECRET_KEY_FALLBACKS`.

```python
# settings.py
SECRET_KEY = "production-value-from-env-never-hard-coded"

# Key rotation: move old key to fallbacks, set new key above
SECRET_KEY_FALLBACKS = [
    "previous-secret-key",
]
```

```bash
# Generate a new key on the command line
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

```python
# Load from environment in production (never commit the value to version control)
import os
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
```

### File Upload Security

- Uploaded files are untrusted data and must be treated accordingly; the main risks are denial-of-service (large files), code execution (serving executables), and content-type spoofing.
- Serve uploads from a **separate domain** (not a subdomain of the main site) to prevent an uploaded HTML file from running scripts in the same origin as the application.

```python
# settings.py
MEDIA_ROOT = BASE_DIR / "mediafiles"
MEDIA_URL = "https://media.example-cdn.com/"   # separate domain, not /media/ on same host

DATA_UPLOAD_MAX_MEMORY_SIZE = 5_242_880   # 5 MB limit for in-memory file data
FILE_UPLOAD_MAX_MEMORY_SIZE = 5_242_880   # 5 MB limit before spooling to disk
```

```python
# Validate file type in a form (whitelist extensions; never trust Content-Type alone)
import os
from django import forms

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

class UploadForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        f = self.cleaned_data["file"]
        ext = os.path.splitext(f.name)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise forms.ValidationError("Unsupported file type.")
        return f
```

### `check --deploy`

- Django's system check framework includes a deployment checklist that reports every security misconfiguration.
- Run it against the production settings before every release.

```bash
python manage.py check --deploy --settings=myproject.settings.production
```

Example output for a misconfigured project:

```
WARNINGS:
?: (security.W004) You have not set a value for SECURE_HSTS_SECONDS.
?: (security.W008) Your SECRET_KEY has less than 50 characters.
?: (security.W012) SESSION_COOKIE_SECURE is not set to True.
?: (security.W016) CSRF_COOKIE_SECURE is not set to True.
```

All `security.W*` warnings must be resolved before deploying to production.

## Extra: Caching

References:
- [Django Cache Framework](https://docs.djangoproject.com/en/5.2/topics/cache/)

- Django's cache framework stores the output of expensive computations so subsequent requests can be served from fast storage instead of recomputing.
- Caching operates at three granularities:
  - the entire site (middleware),
  - a single view (`@cache_page`),
  - or a fragment of a template (`{% cache %}`)
- The low-level API also allows caching arbitrary Python objects.
- Every cache backend shares the same API -- swapping backends is a one-line change in `settings.py`.

### Cache Backends

- The `CACHES` setting maps named aliases to backend configurations; `"default"` is the alias used implicitly by all helpers.
- Common arguments for every backend: `TIMEOUT` (seconds until expiry, default `300`; `None` = never expire), `KEY_PREFIX` (string prepended to every key), `VERSION` (integer included in the key), `OPTIONS` (backend-specific dict).

```python
# settings.py -- pick one backend for "default"

# 1. Local-memory (default, per-process, not shared between workers)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",   # distinguishes multiple locmem caches
    }
}

# 2. Redis (recommended for production; requires `pip install redis`)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        # With auth: "redis://user:password@127.0.0.1:6379"
        # With DB index: "redis://127.0.0.1:6379/1"
    }
}

# 3. Memcached (requires `pip install pymemcache`)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
        # Multiple servers (distributed): "LOCATION": ["10.0.0.1:11211", "10.0.0.2:11211"]
    }
}

# 4. Database (no extra dependencies; slowest but durable)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
    }
}
# Then create the table:
# python manage.py createcachetable

# 5. Filesystem
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

# 6. Dummy (no-op; useful in development to disable caching without code changes)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}
```

```python
# Full example with all common arguments
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "TIMEOUT": 300,           # default expiry in seconds
        "KEY_PREFIX": "mysite",   # prepended to every key -> "mysite:1:mykey"
        "VERSION": 1,             # included in composed key
        "OPTIONS": {
            "MAX_ENTRIES": 1000,  # for locmem/filesystem/db backends
        },
    }
}
```

### Multiple Caches

- Define multiple named caches and use each for a different purpose (e.g., one Redis for general data, one for sessions, one local-memory for per-worker hot data).

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
    },
    "sessions": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    },
    "local": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "local-hot",
    },
}

SESSION_CACHE_ALIAS = "sessions"  # point session backend at the sessions cache
```

```python
from django.core.cache import caches

caches["default"].set("key", "value")
caches["local"].set("key", "value")
```

### Per-Site Caching (Middleware)

- Wrapping the entire middleware stack with `UpdateCacheMiddleware` + `FetchFromCacheMiddleware` caches every cacheable GET/HEAD response automatically.
- `UpdateCacheMiddleware` must be **first** and `FetchFromCacheMiddleware` must be **last** because Django processes request middleware top-to-bottom and response middleware bottom-to-top.

```python
# settings.py
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",    # <- first
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",  # <- last
]

CACHE_MIDDLEWARE_ALIAS = "default"   # which cache to use
CACHE_MIDDLEWARE_SECONDS = 600       # cache duration (10 minutes)
CACHE_MIDDLEWARE_KEY_PREFIX = "mysite"
```

### Per-View Caching (`@cache_page`)

- `@cache_page` caches the full rendered response of a view for a given number of seconds, keyed by the request URL (including query string).
- It can be applied in the view file or directly in `urls.py` -- the URL pattern approach is cleaner for third-party views you cannot modify.

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)   # 15 minutes
def article_list(request):
    ...

# Target a specific cache and add a key prefix
@cache_page(60 * 15, cache="local", key_prefix="v2")
def article_list(request):
    ...
```

```python
# urls.py -- apply cache_page without touching the view
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path("articles/", cache_page(60 * 15)(views.article_list), name="article-list"),
]
```

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View

# Class-based view -- wrap dispatch to cache all HTTP methods
@method_decorator(cache_page(60 * 15), name="dispatch")
class ArticleListView(View):
    ...
```

### Template Fragment Caching

- The `{% cache %}` tag caches a block of template output, avoiding re-rendering expensive sections on every request.
- Additional arguments after the fragment name create per-argument cache keys -- use them to cache per-user, per-language, or per-object fragments.

```django
{% load cache %}

{# Cache the sidebar for 5 minutes, shared by all users #}
{% cache 300 sidebar %}
    <aside>... expensive query ...</aside>
{% endcache %}

{# Per-user fragment -- one cache entry per username #}
{% cache 300 user-sidebar request.user.username %}
    <aside>Welcome, {{ request.user }}</aside>
{% endcache %}

{# Use a specific named cache backend #}
{% cache 300 sidebar using="local" %}
    ...
{% endcache %}
```

```python
# Invalidate a template fragment from Python
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

# Must match the tag: {% cache 300 user-sidebar username %}
key = make_template_fragment_key("user-sidebar", [username])
cache.delete(key)
```

### Low-Level Cache API

- Import `cache` (the default cache) or `caches["alias"]` for a named cache.
- All methods have async equivalents prefixed with `a` -- `aset`, `aget`, `adelete`, etc.

```python
from django.core.cache import cache   # shortcut for caches["default"]

# --- Basic get / set / delete ---
cache.set("key", {"user": 1, "data": [1, 2, 3]}, timeout=60)
value = cache.get("key")                    # returns the dict, or None
value = cache.get("key", default="miss")    # return "miss" if absent

cache.delete("key")                         # returns True if key existed
cache.delete_many(["key1", "key2"])
cache.clear()                               # !! wipes the entire cache namespace

# --- Add (only if absent) ---
cache.add("counter", 0)          # True  -- key was absent, value set
cache.add("counter", 99)         # False -- key already exists, value unchanged

# --- Atomic get-or-set ---
# Second arg can be a value or a zero-arg callable (evaluated lazily only on miss)
hits = cache.get_or_set("homepage_hits", 0, timeout=3600)
user = cache.get_or_set("user:42", lambda: User.objects.get(pk=42), timeout=300)

# --- Bulk operations (fewer round-trips) ---
cache.set_many({"a": 1, "b": 2, "c": 3}, timeout=60)
result = cache.get_many(["a", "b", "c", "missing"])
# -> {"a": 1, "b": 2, "c": 3}  (absent keys not included)

# --- Atomic counters ---
cache.set("views", 0)
cache.incr("views")          # -> 1
cache.incr("views", 10)      # -> 11
cache.decr("views", 5)       # -> 6
# incr/decr raise ValueError if the key does not exist

# --- Refresh expiry without changing value ---
cache.touch("views", timeout=600)   # reset TTL to 10 minutes; returns True/False
```

```python
# Async views
async def my_view(request):
    data = await cache.aget("expensive")
    if data is None:
        data = await compute_expensive()
        await cache.aset("expensive", data, timeout=300)
    return JsonResponse(data)
```

### Cache Versioning

- Versioning adds an integer to the composed cache key, allowing atomic "invalidate everything" by bumping the version rather than iterating over keys.
- The composed key format is `"<KEY_PREFIX>:<VERSION>:<key>"`.

```python
cache.set("article", data, version=2)

cache.get("article")            # uses DEFAULT VERSION (1) -> None
cache.get("article", version=2) # -> data

# Bump the version for a key (new version = old + 1)
cache.incr_version("article")   # key is now accessible at version=3
cache.decr_version("article")   # back to version=2
```

### Cache Control and Vary Headers

- `Cache-Control` and `Vary` headers tell **downstream caches** (CDNs, browser caches, proxies) what they may and may not cache.
- Django's `@cache_page` sets these headers automatically; use `@cache_control` and `@vary_on_headers` to fine-tune them for views not wrapped by `@cache_page`.

```python
from django.views.decorators.cache import cache_control, never_cache
from django.views.decorators.vary import vary_on_headers, vary_on_cookie

# Tell proxies this response is public and cacheable for 1 hour
@cache_control(public=True, max_age=3600)
def public_article(request):
    ...

# Tell proxies never to cache (e.g. account pages)
@cache_control(private=True, no_store=True)
def account_settings(request):
    ...

# Convenience: sets Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private
@never_cache
def checkout(request):
    ...

# Tell downstream caches to keep separate copies per User-Agent
@vary_on_headers("User-Agent")
def mobile_aware_view(request):
    ...

# Shortcut for Vary: Cookie (common for session-dependent pages)
@vary_on_cookie
def personalised_homepage(request):
    ...
```

### Cache Invalidation

- The hardest part of caching is knowing when to evict stale data; Django offers no automatic ORM-level invalidation -- you wire it up explicitly.
- Signal-based invalidation is the cleanest pattern: listen for `post_save` / `post_delete` and delete the relevant keys.

```python
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Article

@receiver(post_save, sender=Article)
@receiver(post_delete, sender=Article)
def invalidate_article_cache(sender, instance, **kwargs):
    cache.delete(f"article:{instance.pk}")
    cache.delete("article_list")           # also bust the list view

# Manual invalidation in a view or service
def publish_article(article):
    article.published = True
    article.save()
    cache.delete(f"article:{article.pk}")
    cache.delete_many([f"tag:{t.pk}" for t in article.tags.all()])
```

```python
# Version-based invalidation -- bump the version to instantly "forget" all related keys
# without needing to enumerate them
CACHE_VERSION = cache.get("global_version", 1)

def get_article(pk):
    key = f"article:{pk}"
    return cache.get(key, version=CACHE_VERSION)

def bust_all():
    cache.incr("global_version")   # all old keys become unreachable
```

## Extra: Logging

- [Django Logging](https://docs.djangoproject.com/en/5.2/topics/logging/)
- [Django Logging Reference](https://docs.djangoproject.com/en/5.2/ref/logging/)

Django integrates with Python's built-in `logging` module and adds its own built-in loggers, handlers, and filters on top. All logging is configured via the `LOGGING` dictionary in `settings.py` using Python's **dictConfig** format.

### The Four Components

Python's logging framework has four building blocks -- loggers, handlers, filters, and formatters -- that form a pipeline from message emission to final output.

- **Loggers** are named entry points (e.g. `"myapp.views"`) where you post messages; each has a minimum level, and a message is only processed if its level >= the logger's level.
- **Handlers** consume records from a logger and send them somewhere (console, file, email, etc.); they also have their own level, so a handler can further restrict what it processes.
- **Filters** sit on loggers or handlers and provide fine-grained control -- they can reject records or even mutate them before output.
- **Formatters** turn a `LogRecord` into a string using a format pattern; Django ships `ServerFormatter` for the dev server.

```
view code
  └─► logger.error("msg")          # posted to logger "myapp.views"
        └─► passes level check?
              └─► each Handler
                    └─► passes filter(s)?
                          └─► Formatter -> final output
```

### Log Levels

- Django uses the standard Python levels in ascending severity order:

| Level | Numeric | Typical use |
|---|---|---|
| `DEBUG` | 10 | SQL queries, variable dumps |
| `INFO` | 20 | Request served, task started |
| `WARNING` | 30 | Recoverable issues |
| `ERROR` | 40 | Exceptions, failed requests |
| `CRITICAL` | 50 | System-level failures |

```python
import logging
logger = logging.getLogger(__name__)

logger.debug("SQL: %s", sql)          # only if level ≤ DEBUG
logger.info("User %s logged in", user)
logger.warning("Rate limit close: %d", count)
logger.error("Payment failed", exc_info=True)   # attaches traceback
logger.critical("DB connection pool exhausted")
```

- Use `exc_info=True` (or pass the exception) to attach a traceback automatically; avoid formatting strings eagerly -- pass args as positional params so formatting is skipped when the level is suppressed.

### Configuring `LOGGING` in `settings.py`

- `LOGGING` uses Python's `dictConfig` schema; Django **merges** it with its own defaults, so set `disable_existing_loggers: False` to preserve built-in loggers.
- `version: 1` is the only value currently accepted by Python's `dictConfig`.

```python
# settings.py
import os

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,          # preserve Django's defaults
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {message}",
            "style": "{",                        # use str.format() style
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],   # only in dev
            "formatter": "simple",
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs" / "django.log",
            "maxBytes": 1024 * 1024 * 5,        # 5 MB
            "backupCount": 5,
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],  # only in production
        },
    },
    "root": {                                    # catch-all for all loggers
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,                  # don't bubble to root
        },
        "myapp": {
            "handlers": ["console", "file", "mail_admins"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
```

### Django's Built-in Loggers

Django posts messages to a hierarchy of named loggers; you can attach handlers or adjust levels for any of them.

| Logger | Default level | Emits |
|---|---|---|
| `django` | INFO | Parent of all; Django doesn't post here directly |
| `django.request` | WARNING/ERROR | 4xx -> WARNING, 5xx -> ERROR; extras: `status_code`, `request` |
| `django.server` | INFO | dev-server access log; 4xx -> WARNING, 5xx -> ERROR |
| `django.template` | DEBUG | Missing template variables |
| `django.db.backends` | DEBUG | Every SQL statement (only when `DEBUG=True`); extras: `sql`, `duration`, `params`, `alias` |
| `django.security.*` | WARNING | `SuspiciousOperation`, bad host headers, CSRF failures |
| `django.security.DisallowedHost` | WARNING | Host header not in `ALLOWED_HOSTS` |
| `django.security.csrf` | WARNING | CSRF token failures |
| `django.contrib.auth` | ERROR | Failed password-reset email delivery |

```python
# Silence the noisy DisallowedHost warnings in production
LOGGING = {
    ...
    "handlers": {"null": {"class": "logging.NullHandler"}},
    "loggers": {
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
    },
}
```

```python
# See every SQL query in development
LOGGING = {
    ...
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
```

### Handlers

- **`logging.StreamHandler`** -- writes to `sys.stderr` (or any stream); ideal for console/Docker output.
- **`logging.FileHandler`** -- appends to a single file; use `RotatingFileHandler` or `TimedRotatingFileHandler` from `logging.handlers` for production.
- **`django.utils.log.AdminEmailHandler`** -- emails `settings.ADMINS` on ERROR; accepts `include_html=True` to attach the full debug page (be careful -- it includes local variable values and settings).
- **`logging.NullHandler`** -- silently discards records; useful to suppress chatty third-party loggers.

```python
# RotatingFileHandler -- rotate at 5 MB, keep 3 archives
"file": {
    "class": "logging.handlers.RotatingFileHandler",
    "filename": "/var/log/myapp/django.log",
    "maxBytes": 5 * 1024 * 1024,
    "backupCount": 3,
    "formatter": "verbose",
},

# AdminEmailHandler with explicit email backend
"mail_admins": {
    "level": "ERROR",
    "class": "django.utils.log.AdminEmailHandler",
    "include_html": False,           # set True only if recipients are trusted
    "email_backend": "django.core.mail.backends.smtp.EmailBackend",
    "filters": ["require_debug_false"],
},
```

### Filters

- **`RequireDebugTrue`** -- passes records only when `DEBUG=True`; gates the console handler to dev.
- **`RequireDebugFalse`** -- passes records only when `DEBUG=False`; gates `AdminEmailHandler` to production.
- **`CallbackFilter`** -- wraps an arbitrary callable; return `True` to pass the record, `False` to suppress it.

```python
# myapp/logging_filters.py
from django.http import UnreadablePostError

def skip_unreadable_post(record):
    if record.exc_info:
        exc_type, exc_value = record.exc_info[:2]
        if isinstance(exc_value, UnreadablePostError):
            return False
    return True
```

```python
# settings.py
"filters": {
    "skip_unreadable_posts": {
        "()": "django.utils.log.CallbackFilter",
        "callback": "myapp.logging_filters.skip_unreadable_post",
    },
},
"handlers": {
    "mail_admins": {
        "level": "ERROR",
        "class": "django.utils.log.AdminEmailHandler",
        "filters": ["require_debug_false", "skip_unreadable_posts"],
    },
},
```

### Formatters

- Formatters control the string layout of each log record; use `"style": "{"` for `str.format()` syntax or `"style": "%"` (default) for `%-formatting`.
- Standard `LogRecord` attributes include `levelname`, `asctime`, `module`, `process`, `thread`, `message`, `pathname`, `lineno`.

```python
"formatters": {
    "verbose": {
        "format": "{levelname} {asctime} {module}:{lineno} [{process}] {message}",
        "style": "{",
        "datefmt": "%Y-%m-%d %H:%M:%S",
    },
},
```

- For structured/JSON logging in production (easier to ingest into ELK, Datadog, Loki, etc.) use `python-json-logger`:

```bash
pip install python-json-logger
```

```python
"formatters": {
    "json": {
        "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
        "format": "%(levelname)s %(asctime)s %(module)s %(message)s",
    },
},
```

### Logging in Your Own Code

- Obtain a logger per module with `logging.getLogger(__name__)`; the dotted module path becomes the logger's name, which slots naturally into the logger hierarchy.
- Never build the log message string yourself -- pass it as a format string with positional args so the work is skipped when the level is suppressed.

```python
# myapp/views.py
import logging

logger = logging.getLogger(__name__)   # "myapp.views"

def checkout(request):
    logger.info("Checkout started for user %s", request.user.pk)
    try:
        result = process_payment(request)
    except PaymentError as e:
        logger.error(
            "Payment failed for user %s: %s",
            request.user.pk, e,
            exc_info=True,             # attach full traceback
            extra={"order_id": request.POST.get("order_id")},
        )
        return render(request, "checkout_error.html", status=500)
    logger.info("Payment succeeded, order=%s", result.order_id)
    return redirect("order_confirmation", pk=result.order_id)
```

- Use `extra={}` to attach custom fields to the `LogRecord`; handlers/formatters can then include them in output (useful for request IDs, tenant IDs, etc.).

### Context Variables with `LoggerAdapter`

- `logging.LoggerAdapter` wraps a logger and auto-injects contextual data (request ID, user, tenant) into every record without threading it through every call site.

```python
# myapp/middleware.py
import logging, uuid

class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.id = str(uuid.uuid4())
        request.log = logging.LoggerAdapter(
            logging.getLogger("myapp.requests"),
            {"request_id": request.id},
        )
        return self.get_response(request)
```

```python
# myapp/views.py
def my_view(request):
    request.log.info("Processing started")   # automatically includes request_id
```

### Security Considerations

- Log files may contain passwords, tokens, session keys, and PII -- treat them as sensitive data with restricted filesystem permissions (`chmod 640`).
- `AdminEmailHandler` with `include_html=True` sends the full debug page (local variables, all settings) to admins; only enable if the email transport is encrypted and recipients are trusted.
- Never log raw `request.POST` or `request.body`; extract and redact fields explicitly before logging.
- Prefer a third-party error tracker (Sentry, Rollbar) over `AdminEmailHandler` for production -- they provide redaction, deduplication, and rate limiting out of the box.

```python
# Safe -- log only what you need
logger.info(
    "Password reset requested",
    extra={"email_domain": email.split("@")[1]},   # NOT the full email
)

# Unsafe -- leaks credentials and PII
logger.debug("POST data: %s", request.POST)
```

## Extra: Emails

- [Django Email](https://docs.djangoproject.com/en/5.2/topics/email/)

Django wraps Python's `smtplib` in a clean API centred on `EmailMessage` and a swappable **backend** system. All email functions live in `django.core.mail`; settings are under `EMAIL_*`.

### Key Settings

```python
# settings.py
EMAIL_BACKEND  = "django.core.mail.backends.smtp.EmailBackend"  # default
EMAIL_HOST     = "smtp.sendgrid.net"
EMAIL_PORT     = 587
EMAIL_USE_TLS  = True          # STARTTLS on port 587
EMAIL_USE_SSL  = False         # TLS-wrap on port 465 (mutually exclusive with USE_TLS)
EMAIL_HOST_USER     = "apikey"
EMAIL_HOST_PASSWORD = env("SENDGRID_API_KEY")
EMAIL_TIMEOUT  = 10            # seconds; None uses socket default

DEFAULT_FROM_EMAIL   = "noreply@myapp.com"   # used when from_email=None
SERVER_EMAIL         = "errors@myapp.com"    # used by mail_admins/mail_managers
EMAIL_SUBJECT_PREFIX = "[MyApp] "            # prepended by mail_admins/mail_managers
ADMINS   = [("Alice", "alice@myapp.com")]
MANAGERS = [("Bob",   "bob@myapp.com")]
```

### `send_mail()` -- Quick One-Shot

- `send_mail()` opens a fresh connection per call, sends one message, then closes -- fine for low-volume transactional mail; use `send_mass_mail()` or a shared connection for batches.

```python
from django.core.mail import send_mail

sent = send_mail(
    subject="Welcome to MyApp",
    message="Plain-text fallback body.",
    from_email="noreply@myapp.com",   # None -> DEFAULT_FROM_EMAIL
    recipient_list=["user@example.com"],
    fail_silently=False,              # raise on error (default False)
    html_message="<h1>Welcome!</h1>", # triggers multipart/alternative
)
# send_mail returns number of messages actually sent (0 or 1)
```

### `send_mass_mail()` -- Efficient Batch Sending

- `send_mass_mail()` reuses a **single SMTP connection** for all messages in the tuple, making it substantially faster than calling `send_mail()` in a loop.

```python
from django.core.mail import send_mass_mail

messages = [
    ("Invoice #101", "See attached.", "billing@myapp.com", ["alice@example.com"]),
    ("Invoice #102", "See attached.", "billing@myapp.com", ["bob@example.com"]),
]
send_mass_mail(messages, fail_silently=False)
```

### `EmailMessage` -- Full Control

- `EmailMessage` exposes every SMTP header and supports attachments, CC/BCC, Reply-To, and custom headers; it is the foundation that `send_mail()` wraps internally.

```python
from django.core.mail import EmailMessage

email = EmailMessage(
    subject="Quarterly report",
    body="Please find the report attached.",
    from_email="reports@myapp.com",
    to=["ceo@example.com"],
    cc=["cfo@example.com"],
    bcc=["audit@myapp.com"],
    reply_to=["no-reply@myapp.com"],
    headers={"X-Priority": "1", "List-Unsubscribe": "<mailto:unsub@myapp.com>"},
)

# Attach from memory (filename, bytes, mimetype)
email.attach("report.pdf", pdf_bytes, "application/pdf")

# Attach from disk (mimetype auto-detected)
email.attach_file("/srv/reports/q3.pdf")

email.send()
```

### `EmailMultiAlternatives` -- HTML + Plain Text

- RFC 2822 best practice requires a plain-text fallback alongside HTML; `EmailMultiAlternatives` makes this easy with `attach_alternative()`.

```python
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

ctx = {"user": user, "activation_url": url}
text = render_to_string("emails/activation.txt", ctx)
html = render_to_string("emails/activation.html", ctx)

msg = EmailMultiAlternatives(
    subject="Activate your account",
    body=text,
    from_email="noreply@myapp.com",
    to=[user.email],
)
msg.attach_alternative(html, "text/html")
msg.send()
```

- In Django 5.2+ you can inspect attached alternatives via `msg.alternatives` (a list of `EmailAlternative` named tuples with `.content` and `.mimetype`) and verify content with `msg.body_contains("some text")`.

### Template-Based Emails

- Keeping email content in templates separates design from logic and supports i18n.

```
myapp/
  templates/
    emails/
      welcome.subject.txt    # single-line subject
      welcome.body.txt       # plain-text body
      welcome.body.html      # HTML body
```

```python
# myapp/emails.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(user):
    ctx = {"user": user, "site_name": "MyApp"}
    subject = render_to_string("emails/welcome.subject.txt", ctx).strip()
    text    = render_to_string("emails/welcome.body.txt",    ctx)
    html    = render_to_string("emails/welcome.body.html",   ctx)

    msg = EmailMultiAlternatives(subject, text, to=[user.email])
    msg.attach_alternative(html, "text/html")
    msg.send()
```

### Shared Connections

- Open one SMTP connection explicitly and reuse it across multiple messages to avoid per-message TCP/TLS handshake overhead.

```python
from django.core import mail

emails = build_batch()   # list of EmailMessage objects

# Context manager: opens on __enter__, closes on __exit__
with mail.get_connection() as conn:
    conn.send_messages(emails)   # all sent over a single connection
```

### Admin & Manager Shortcuts

- `mail_admins()` and `mail_managers()` are convenience wrappers that read from `ADMINS` / `MANAGERS`, prefix the subject with `EMAIL_SUBJECT_PREFIX`, and use `SERVER_EMAIL` as the From address.

```python
from django.core.mail import mail_admins, mail_managers

mail_admins(
    "Database disk usage at 90%",
    "Please free up space immediately.",
    fail_silently=True,
)

mail_managers("New milestone: 10,000 users", "Congratulations team!")
```

### Email Backends

Django's backend system lets you swap transport without touching application code.

| Backend | Setting suffix | Use |
|---|---|---|
| SMTP (default) | `smtp.EmailBackend` | Production |
| Console | `console.EmailBackend` | Dev -- prints to stdout |
| File | `filebased.EmailBackend` | Dev -- writes `.eml` files to `EMAIL_FILE_PATH` |
| In-memory | `locmem.EmailBackend` | Tests -- stores in `mail.outbox` |
| Dummy | `dummy.EmailBackend` | CI -- discards all mail silently |

All backend classes share the prefix `django.core.mail.backends.`.

```python
# Development: print emails to the terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Development: save emails as files for inspection
EMAIL_BACKEND  = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"
```

### Testing Emails

- The test runner automatically switches to the `locmem` backend; all sent messages accumulate in `django.core.mail.outbox` (a plain list, reset between tests).

```python
# myapp/tests.py
from django.core import mail
from django.test import TestCase

class WelcomeEmailTest(TestCase):
    def test_welcome_sent(self):
        self.client.post("/register/", {"email": "u@example.com", ...})

        self.assertEqual(len(mail.outbox), 1)
        msg = mail.outbox[0]
        self.assertEqual(msg.subject, "[MyApp] Welcome to MyApp")
        self.assertIn("u@example.com", msg.to)
        self.assertTrue(msg.body_contains("Welcome"))   # Django 5.2+
```

### Header Injection Prevention

- Django automatically raises `BadHeaderError` if any newline (`\n`, `\r`) appears in `subject`, `from_email`, or recipient addresses -- always catch it when those values come from user input.

```python
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def contact(request):
    subject = request.POST.get("subject", "")
    message = request.POST.get("message", "")
    try:
        send_mail(subject, message, "contact@myapp.com", ["support@myapp.com"])
    except BadHeaderError:
        return HttpResponse("Invalid header found.", status=400)
    return HttpResponseRedirect("/thanks/")
```

### Custom Backend

- Subclass `BaseEmailBackend` to integrate third-party providers (Mailgun, SES, Postmark) or route to a message queue; implement `open()`, `close()`, and `send_messages()`.

```python
# myapp/backends.py
from django.core.mail.backends.base import BaseEmailBackend
import requests

class MailgunBackend(BaseEmailBackend):
    def open(self):
        self._session = requests.Session()
        return True

    def close(self):
        self._session.close()

    def send_messages(self, email_messages):
        num_sent = 0
        for msg in email_messages:
            resp = self._session.post(
                "https://api.mailgun.net/v3/mg.myapp.com/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": msg.from_email,
                    "to": msg.recipients(),
                    "subject": msg.subject,
                    "text": msg.body,
                },
            )
            if resp.ok:
                num_sent += 1
        return num_sent
```

```python
# settings.py
EMAIL_BACKEND = "myapp.backends.MailgunBackend"
```

## Extra: Tasks

- [Django Tasks (dev docs -- arrives in Django 6.0)](https://docs.djangoproject.com/en/dev/topics/tasks/)

> **Note:** Django's built-in task framework is scheduled for **Django 6.0** (not yet in 5.2). Use the `ImmediateBackend` for development today; wire a third-party backend for production.

Django's task framework lets you move work outside the HTTP request-response cycle -- sending emails, resizing images, generating reports -- without pulling in a full message-broker stack. The API is deliberately minimal: Django owns task *definition*, *validation*, and *queuing*; actual execution is delegated to a backend (and a worker process).

### Architecture

Three components form the pipeline:

```
View / signal
  └─► task.enqueue(...)      # stores task metadata in the queue store
        └─► Queue Store       # durable storage (DB, Redis, etc. -- backend-specific)
              └─► Worker(s)   # external process: claims tasks and runs them
```

- **Tasks** -- plain Python functions decorated with `@task`; arguments and return values must be JSON-serializable.
- **Backends** -- pluggable classes responsible for storing and retrieving task state; Django ships two dev-only backends, production needs a third-party one.
- **Workers** -- long-running processes (`manage.py run_workers`) that poll the queue store and execute tasks.

### Defining Tasks

- Define tasks in a `tasks.py` file per app (convention, not enforced); import `task` from `django.tasks`.
- The decorated function becomes a `Task` object with `.enqueue()`, `.aenqueue()`, `.get_result()`, and `.using()` methods.

```python
# myapp/tasks.py
from django.core.mail import send_mail
from django.tasks import task

@task
def send_welcome_email(user_email: str, username: str) -> None:
    send_mail(
        subject="Welcome!",
        message=f"Hi {username}, welcome to MyApp.",
        from_email=None,            # -> DEFAULT_FROM_EMAIL
        recipient_list=[user_email],
    )

@task
def generate_report(report_id: int) -> dict:
    report = Report.objects.get(pk=report_id)
    data = build_report_data(report)   # heavy computation
    report.result = data
    report.save()
    return data
```

### Task Decorator Parameters

- `priority` (int, default `0`) -- higher number = higher priority; backend must support it.
- `queue_name` (str, default `"default"`) -- route tasks to different queues mapped in `TASKS`.
- `takes_context` (bool) -- injects a `TaskContext` as the first argument with `.attempt` (current retry count) and `.task_result` (the live `TaskResult` instance).

```python
@task(priority=5, queue_name="emails")
def urgent_email(to: str, body: str) -> None:
    ...

@task(takes_context=True)
def resilient_task(context, item_id: int) -> None:
    logger.info(
        "Attempt %d for task %s",
        context.attempt,
        context.task_result.id,
    )
    process(item_id)
```

### Backends & `TASKS` Setting

```python
# settings.py
TASKS = {
    "default": {
        "BACKEND": "django.tasks.backends.immediate.ImmediateBackend",
    },
    "emails": {                          # named queue
        "BACKEND": "path.to.ThirdPartyBackend",
        "OPTIONS": {"url": "redis://localhost:6379/1"},
    },
}
```

| Backend | Class | When to use |
|---|---|---|
| `ImmediateBackend` | `django.tasks.backends.immediate.ImmediateBackend` | Development -- runs the task inline, synchronously |
| `DummyBackend` | `django.tasks.backends.dummy.DummyBackend` | Testing -- stores but never executes tasks |
| Third-party | e.g. `django_tasks_redis.RedisBackend` | Production -- durable queue + real worker processes |

- `ImmediateBackend` executes tasks synchronously in the calling process -- no worker needed during development, but results are not retrievable via `get_result()`.
- `DummyBackend` is useful in tests to assert tasks were enqueued without side effects; inspect `default_task_backend.results`.

```python
# tests.py
from django.tasks import default_task_backend
from django.test import TestCase, override_settings

@override_settings(TASKS={"default": {"BACKEND": "django.tasks.backends.dummy.DummyBackend"}})
class MyTaskTest(TestCase):
    def test_task_enqueued(self):
        send_welcome_email.enqueue("u@example.com", "Alice")
        self.assertEqual(len(default_task_backend.results), 1)
        default_task_backend.clear()
```

### Enqueueing Tasks

- Call `.enqueue()` (sync) or `.aenqueue()` (async) with the same arguments as the underlying function; both return a `TaskResult`.
- Use `.using(**overrides)` to create a one-off modified task (different priority or queue) without altering the original definition.

```python
# Enqueue with defaults
result = send_welcome_email.enqueue("user@example.com", "Alice")

# Override priority for this call only
result = generate_report.using(priority=10).enqueue(report_id=42)

# Async enqueue inside an async view
result = await send_welcome_email.aenqueue("user@example.com", "Alice")

# Store the result ID for later retrieval
request.session["report_task_id"] = str(result.id)
```

### Transaction Safety

- Enqueue tasks **after** the surrounding transaction commits; otherwise the worker may run before the data it needs is visible in the database.

```python
from functools import partial
from django.db import transaction
from myapp.tasks import send_welcome_email

def register_user(email, username):
    with transaction.atomic():
        user = User.objects.create_user(username=username, email=email)
        # enqueue only after commit -- user row is visible to the worker
        transaction.on_commit(
            partial(send_welcome_email.enqueue, email, username)
        )
```

### Task Results

- `task.enqueue()` returns a `TaskResult` immediately; poll `.status` and call `.refresh()` (or `await .arefresh()`) to get fresh state from the backend.
- Access `.return_value` only when `status == SUCCESSFUL`; accessing it earlier raises `ValueError`.

```python
result = generate_report.enqueue(report_id=42)
print(result.id)        # UUID
print(result.status)    # QUEUED | RUNNING | SUCCESSFUL | FAILED

# Poll until done (in a real app, check asynchronously)
result.refresh()
if result.status == "SUCCESSFUL":
    print(result.return_value)   # whatever the task returned
elif result.status == "FAILED":
    err = result.errors[0]
    print(err.exception_class)   # e.g. <class 'ValueError'>
    print(err.traceback)         # full traceback string
```

```python
# Retrieve a stored result by ID (e.g. from session)
from django.tasks import default_task_backend

result = default_task_backend.get_result(task_id)
result = await default_task_backend.aget_result(task_id)
```

### Workers

- Start one or more worker processes with the built-in management command; workers poll the backend and execute queued tasks.

```bash
# Start workers (uses TASKS["default"] backend)
python manage.py run_workers

# Run workers for a named queue
python manage.py run_workers --queue emails
```

- In production run the worker under a process supervisor (systemd, supervisord, Docker) so it restarts on failure.

```ini
# /etc/systemd/system/myapp-worker.service
[Unit]
Description=MyApp Task Worker
After=network.target

[Service]
User=myapp
WorkingDirectory=/srv/myapp
ExecStart=/srv/myapp/venv/bin/python manage.py run_workers
Restart=always

[Install]
WantedBy=multi-user.target
```

### Serialization Constraints

- All task arguments **and** return values must be JSON-serializable; this is a hard constraint imposed by the backend protocol.

```python
# WRONG -- datetime is not JSON-serializable
process.enqueue(datetime.now())   # TypeError

# RIGHT -- pass primitive types only
process.enqueue(datetime.now().isoformat())

# WRONG -- tuples silently become lists after JSON round-trip
@task
def process_ids(ids):
    return {id: id * 2 for id in ids}   # fails if ids was a tuple

# RIGHT -- use lists; convert inside the task if needed
process_ids.enqueue([1, 2, 3])

# WRONG -- model instances are not serializable
send_welcome_email.enqueue(user)       # TypeError

# RIGHT -- pass the primary key, re-fetch inside the task
send_welcome_email.enqueue(user.email, user.username)
```

### Django Tasks vs Celery

| | Django Tasks (6.0+) | Celery |
|---|---|---|
| **Extra infrastructure** | None (ImmediateBackend) / backend-specific | Redis or RabbitMQ broker required |
| **Configuration** | `TASKS` dict in `settings.py` | `celery.py` + `CELERY_*` settings |
| **Task definition** | `@task` | `@shared_task` / `@app.task` |
| **Enqueueing** | `task.enqueue()` | `task.delay()` / `task.apply_async()` |
| **Post-transaction** | `transaction.on_commit(partial(...))` | `task.delay_on_commit()` (v5.4+) |
| **Periodic tasks** | Not built-in | `django-celery-beat` |
| **Retries** | Via `takes_context` + manual re-enqueue | `autoretry_for`, `retry_backoff` built-in |
| **Result backend** | Backend-specific | `django-celery-results` |
| **Maturity** | New (Django 6.0) | Very mature, huge ecosystem |
| **Complexity** | Low | Medium–High |

**When to choose Django Tasks:** you want zero extra infrastructure for development, a clean Django-native API, and you don't need periodic tasks or complex retry policies out of the box.

**When to choose Celery:** you need periodic/scheduled tasks, advanced retry backoff, fan-out/chord/chain primitives, or a proven production ecosystem today (Django 5.x and earlier).

### Redis Backend (`django-tasks-rq`)

- `django-tasks-rq` wraps **Redis Queue (RQ)** -- a mature Python job queue library -- and exposes it as a `django.tasks`-compatible backend; swapping to it from `ImmediateBackend` is a single settings change.

```bash
pip install django-tasks-rq
```

```python
# settings.py
TASKS = {
    "default": {
        "BACKEND": "django_tasks_rq.RQBackend",
        "OPTIONS": {
            "URL": env("REDIS_URL", default="redis://localhost:6379/0"),
        },
    },
    # Optional: a second high-priority queue on the same Redis instance
    "urgent": {
        "BACKEND": "django_tasks_rq.RQBackend",
        "OPTIONS": {
            "URL": env("REDIS_URL", default="redis://localhost:6379/0"),
            "QUEUE": "urgent",
        },
    },
}
```

```python
# tasks.py -- unchanged from before; backend is transparent
from django.tasks import task

@task(queue_name="urgent")
def send_urgent_alert(message: str) -> None:
    ...

@task
def generate_report(report_id: int) -> dict:
    ...
```

```bash
# Start the worker (reads TASKS["default"] by default)
python manage.py run_workers

# Worker for a named queue
python manage.py run_workers --queue urgent
```

#### Running Redis -- Same Machine vs Separate Machine

**Same machine** is fine for:
- Development and local testing -- Redis listens on `localhost:6379`, zero network overhead.
- Small-to-medium production deployments where the Django app, worker, and Redis all share one server; Redis is lightweight (typically < 50 MB RAM for most workloads).

**Separate machine** (or managed service) is better when:
- You scale Django/workers horizontally -- multiple app servers need to reach the same Redis instance.
- You want Redis memory to be isolated from your app's memory so neither starves the other.
- You use a managed service (AWS ElastiCache, Redis Cloud, Upstash) and want Redis backed up and monitored independently.

#### Option A -- Redis directly on the machine

```bash
# Ubuntu/Debian
sudo apt install redis-server
sudo systemctl enable --now redis-server

# macOS
brew install redis
brew services start redis

# Verify
redis-cli ping   # → PONG
```

```python
# settings.py -- local install
REDIS_URL = "redis://localhost:6379/0"
```

#### Option B -- Docker Compose (recommended for dev and single-server prod)

Add a `redis` service alongside your Django app and worker; all three share a Docker network so `redis://redis:6379` resolves correctly inside containers.

```yaml
# docker-compose.yml
services:

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: myapp
      POSTGRES_PASSWORD: secret
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine          # minimal footprint
    restart: unless-stopped
    ports:
      - "6379:6379"                # expose to host for redis-cli debugging
    volumes:
      - redis_data:/data           # persist queue across restarts
    command: redis-server --appendonly yes   # AOF persistence

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
    environment:
      DATABASE_URL: postgres://myapp:secret@db:5432/myapp
      REDIS_URL: redis://redis:6379/0

  worker:
    build: .
    command: python manage.py run_workers
    volumes:
      - .:/app
    depends_on:
      - db
      - redis
    environment:
      DATABASE_URL: postgres://myapp:secret@db:5432/myapp
      REDIS_URL: redis://redis:6379/0

volumes:
  postgres_data:
  redis_data:
```

```bash
docker compose up          # starts db + redis + web + worker together
docker compose up -d       # detached
docker compose logs -f worker   # tail worker output
```

- Use `redis://redis:6379/0` inside Docker (service name resolves via Docker DNS).
- Use `redis://localhost:6379/0` when running Django/worker outside Docker (e.g. `python manage.py runserver` on the host with only Redis in Docker).
- The `--appendonly yes` flag enables AOF persistence so queued tasks survive a Redis restart; without it, Redis is purely in-memory and tasks are lost on restart.

