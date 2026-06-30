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

This module deals with the fourth topic/course: **APIs**.

Table of Contents:

- [Intoduction to Web-App Back-End Development](#intoduction-to-web-app-back-end-development)
  - [1. REST APIs](#1-rest-apis)
    - [Note on Lab Usage](#note-on-lab-usage)
    - [Introduction to APIs](#introduction-to-apis)
      - [HTTP and HTTPS Refresher](#http-and-https-refresher)
    - [Principles of API Development](#principles-of-api-development)
    - [Writing Your First API](#writing-your-first-api)
  - [2. Django REST Framework](#2-django-rest-framework)
    - [Introduction to Django REST Framework (DRF)](#introduction-to-django-rest-framework-drf)
    - [Django REST Framework Essentials](#django-rest-framework-essentials)
  - [3. Advanced API Development](#3-advanced-api-development)
    - [Filtering, Ordering, Searching](#filtering-ordering-searching)
    - [Securing an API in Django REST Framework](#securing-an-api-in-django-rest-framework)
  - [4. Final Project](#4-final-project)

## 1. REST APIs

### Note on Lab Usage

In the coursera lab environment, we need to run the following commands to set up the environment and start the Django server:

```bash
# Go to project directory
cd /home/coder/project/YOUR_DJANGO_PROJECT

# Setup environment
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

pipenv shell
pipenv install 

# Migrate the database
python3 manage.py makemigrations # To compile the migrations
python3 manage.py migrate  # To migrate the changes in Database

# Start the server
python3 manage.py runserver 8080 # To run the server
```

### Introduction to APIs

#### HTTP and HTTPS Refresher

- HTTP (Hypertext Transfer Protocol) is one of the most widely used protocols for transferring data across the Internet.
  - Browsing webpages, viewing images, or submitting a form all transmit data using HTTP or its secured version, HTTPS.
- Communicating over HTTP requires at least two parts: the client, which requests information, and the server, which responds to the request and serves the content.
- HTTPS is the secured version of HTTP and is better suited when security is a concern.
  - The client's computer encrypts data before sending it to the server.
  - The server decrypts the client-side data and processes it.
  - The server then encrypts the response data and sends it back to the browser.
  - The browser decrypts the response and displays it.
  - Encrypted content is harder to steal or read, so HTTPS should always be used for sensitive data such as credit card information.
- HTTP methods (also called HTTP verbs) define the action of a request. Five are commonly used:
  - `GET`: retrieves a resource.
  - `POST`: sends data to the server to create a record.
  - `PUT`: updates the whole resource.
  - `PATCH`: partially updates a resource.
  - `DELETE`: deletes a resource.
- An HTTP request is the encoded data a browser sends, and typically includes:
  - the HTTP version (e.g., 1.1 or 2.0),
  - the URL or path,
  - the HTTP method,
  - HTTP request headers,
  - an optional HTTP body.
  - The body carries submitted data, such as a login form's username and password, as a raw JSON string or a form URL-encoded string.
  - Headers are a core part of every request and carry extra information that helps the server decide how to present the content, such as cookies, user agents, and referrers.
- An HTTP response contains the information the browser uses to display the content, plus the response body.
  - It includes the requested resource, the content length, the content type, headers (e.g., cookies), ETags, and the time the content was last modified.
  - It also includes an HTTP status code: a numerical code that gives the browser extra information about the resource rather than a message meant for the user.
    - Example: the server sends `200` when everything is okay (not shown in the browser), or `404` when the requested content cannot be found (usually shown in the browser).
  - Status codes fall into ranges by meaning:
    - `100`-`199`: informational messages.
    - `200`-`299`: successful responses.
    - `300`-`399`: redirection information.
    - `400`-`499`: client error responses, usually from a bad API request with insufficient information, or a request for a resource that does not exist.
    - `500`-`599`: server error codes, usually from missing error checks, configuration mismatches, or incorrect package dependencies.
  - The same status code can mean different things depending on the request method.
    - `200` on a `GET` request means the content was found.
    - `200` on a `PUT` request means the update was successful.
    - `200` on a `DELETE` request means the resource was successfully deleted.
  - The most commonly used status codes are `200`, `201`, `303`, `304`, `400`, `401`, `403`, `404`, and `500`.

### Principles of API Development

### Writing Your First API

## 2. Django REST Framework

### Introduction to Django REST Framework (DRF)

### Django REST Framework Essentials

## 3. Advanced API Development

### Filtering, Ordering, Searching

### Securing an API in Django REST Framework

## 4. Final Project


