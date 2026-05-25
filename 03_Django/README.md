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
    - [Projects and Apps](#projects-and-apps)
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


### Projects and Apps

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

