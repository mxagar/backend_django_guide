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
      - [HTTP Methods, Status Codes and Response Types](#http-methods-status-codes-and-response-types)
        - [HTTP Methods](#http-methods)
        - [Status Codes](#status-codes)
        - [Response Types and Content Negotiation](#response-types-and-content-negotiation)
      - [RESTfulness](#restfulness)
        - [Resources](#resources)
        - [Statelessness in Practice](#statelessness-in-practice)
      - [Naming Conventions](#naming-conventions)
      - [Examples of Good and Bad Routes](#examples-of-good-and-bad-routes)
        - [Rule 01: Lowercase, Hyphens, No Abbreviations](#rule-01-lowercase-hyphens-no-abbreviations)
        - [Rule 02: Forward Slash for Hierarchy](#rule-02-forward-slash-for-hierarchy)
        - [Rule 03: Nouns for Resource Names, Not Verbs](#rule-03-nouns-for-resource-names-not-verbs)
        - [Rule 04: Avoid Special Characters](#rule-04-avoid-special-characters)
        - [Rule 05: No File Extensions in URIs](#rule-05-no-file-extensions-in-uris)
        - [Rule 06: Query Parameters for Filtering and Pagination](#rule-06-query-parameters-for-filtering-and-pagination)
        - [Rule 07: No Trailing Slash](#rule-07-no-trailing-slash)
      - [Essential Tools for API Development](#essential-tools-for-api-development)
      - [Setting Up a Django REST Framework Project](#setting-up-a-django-rest-framework-project)
      - [How to Use Insomnia](#how-to-use-insomnia)
        - [Getting Started](#getting-started)
        - [Running httpbin Locally with Docker (Optional)](#running-httpbin-locally-with-docker-optional)
        - [Create a GET Request](#create-a-get-request)
        - [Create a POST Request with Form Data](#create-a-post-request-with-form-data)
        - [Create a POST Request with JSON Data](#create-a-post-request-with-json-data)
    - [Principles of API Development](#principles-of-api-development)
      - [REST Best Practices](#rest-best-practices)
      - [Security and Authentication in REST APIs](#security-and-authentication-in-rest-apis)
      - [Access Control](#access-control)
      - [Authentication vs. Authorization](#authentication-vs-authorization)
        - [Authentication](#authentication)
        - [Authorization](#authorization)
        - [Implementing Authorization](#implementing-authorization)
        - [User Groups in Django](#user-groups-in-django)
    - [Writing Your First API](#writing-your-first-api)
      - [BookAPI List Project](#bookapi-list-project)
      - [Organizing an API Project](#organizing-an-api-project)
      - [Consequences of a Poorly Designed API Project](#consequences-of-a-poorly-designed-api-project)
      - [XML and JSON Response Types](#xml-and-json-response-types)
      - [Exercise: Build a Simple API](#exercise-build-a-simple-api)
      - [Debugging your API](#debugging-your-api)
      - [Browser Tools and Extensions for API Development](#browser-tools-and-extensions-for-api-development)
      - [Mock APIs](#mock-apis)
  - [2. Django REST Framework](#2-django-rest-framework)
    - [Introduction to Django REST Framework (DRF)](#introduction-to-django-rest-framework-drf)
      - [What Is the Django REST Framework (DRF)?](#what-is-the-django-rest-framework-drf)
      - [Installing and Setting Up DRF](#installing-and-setting-up-drf)
      - [Better API View with Decorators](#better-api-view-with-decorators)
      - [Different Types of Routing in DRF](#different-types-of-routing-in-drf)
        - [Regular routes](#regular-routes)
        - [Routing to a class method](#routing-to-a-class-method)
        - [Routing class-based views](#routing-class-based-views)
        - [Routing classes that extend viewsets](#routing-classes-that-extend-viewsets)
        - [Routing with the SimpleRouter class in DRF](#routing-with-the-simplerouter-class-in-drf)
        - [Routing with the DefaultRouter class in DRF](#routing-with-the-defaultrouter-class-in-drf)
      - [Generic Views and ViewSets in DRF](#generic-views-and-viewsets-in-drf)
        - [ViewSets](#viewsets)
        - [Generic views](#generic-views)
        - [Authentication and selective authentication](#authentication-and-selective-authentication)
        - [Return items for the authenticated user only](#return-items-for-the-authenticated-user-only)
        - [Override default behavior](#override-default-behavior)
      - [Function and Class-Based Views](#function-and-class-based-views)
      - [Django Debug Toolbar](#django-debug-toolbar)
      - [Restaurant Menu API Project with DRF](#restaurant-menu-api-project-with-drf)
      - [Exercise: Book List API with DRF](#exercise-book-list-api-with-drf)
      - [Additional Resources](#additional-resources)
    - [Django REST Framework Essentials](#django-rest-framework-essentials)
      - [Serializers](#serializers)
      - [Model Serializers](#model-serializers)
      - [Relationship Serializers](#relationship-serializers)
      - [Other Types of Serializers in DRF](#other-types-of-serializers-in-drf)
        - [Nested Fields](#nested-fields)
        - [Displaying a Related Field as a Hyperlink](#displaying-a-related-field-as-a-hyperlink)
      - [Deserialization and Validation](#deserialization-and-validation)
      - [Renderers](#renderers)
      - [Different Types of Renderers](#different-types-of-renderers)
        - [TemplateHTMLRenderer](#templatehtmlrenderer)
        - [StaticHTMLRenderer](#statichtmlrenderer)
        - [CSV Renderer](#csv-renderer)
        - [YAML Renderer](#yaml-renderer)
        - [Global Settings](#global-settings)
      - [Exercise: Restaurant Menu API with Serialization](#exercise-restaurant-menu-api-with-serialization)
      - [Additional Resources](#additional-resources-1)
  - [3. Advanced API Development](#3-advanced-api-development)
    - [Filtering, Ordering, Searching](#filtering-ordering-searching)
      - [Filtering and Searching](#filtering-and-searching)
      - [Ordering](#ordering)
      - [Importance of Data Validation](#importance-of-data-validation)
        - [Validation in DRF](#validation-in-drf)
        - [Method 1: Conditions on the Field](#method-1-conditions-on-the-field)
        - [Method 2: `extra_kwargs` on the Meta Class](#method-2-extra_kwargs-on-the-meta-class)
        - [Method 3: `validate_<field>()` Methods](#method-3-validate_field-methods)
        - [Method 4: The `validate()` Method](#method-4-the-validate-method)
        - [Where This Code Goes, and Validation Order](#where-this-code-goes-and-validation-order)
        - [Unique Validation](#unique-validation)
      - [Data Sanitization](#data-sanitization)
        - [Sanitizing HTML and JavaScript](#sanitizing-html-and-javascript)
        - [Preventing SQL Injection](#preventing-sql-injection)
      - [Pagination](#pagination)
        - [Complete `menu_items` View](#complete-menu_items-view)
      - [More on Filtering and Pagination](#more-on-filtering-and-pagination)
        - [Scaffolding the Project](#scaffolding-the-project)
        - [Ordering and Sorting](#ordering-and-sorting)
        - [Pagination](#pagination-1)
        - [Search](#search)
        - [Searching in Nested Fields](#searching-in-nested-fields)
      - [Caching](#caching)
      - [Extra: What Is a Reverse Proxy?](#extra-what-is-a-reverse-proxy)
      - [Exercise: Restaurant Menu API with Filtering, Ordering, and Searching](#exercise-restaurant-menu-api-with-filtering-ordering-and-searching)
      - [Additional Resources](#additional-resources-2)
    - [Securing an API in Django REST Framework](#securing-an-api-in-django-rest-framework)
      - [Token-Based Authentication in DRF](#token-based-authentication-in-drf)
      - [User Roles](#user-roles)
      - [Setting up API Throttling](#setting-up-api-throttling)
      - [API Throttling for Class-Based Views](#api-throttling-for-class-based-views)
        - [Project Scaffolding](#project-scaffolding)
        - [Add Support for Throttling](#add-support-for-throttling)
        - [Throttling for Class-Based Views](#throttling-for-class-based-views)
        - [Conditional Throttling](#conditional-throttling)
        - [Custom Throttling Classes](#custom-throttling-classes)
        - [Real-World Examples of API Rate Limits](#real-world-examples-of-api-rate-limits)
      - [Introduction to Djoser library for Better Authentication](#introduction-to-djoser-library-for-better-authentication)
      - [Registration and Authentication Endpoints with JWT](#registration-and-authentication-endpoints-with-jwt)
      - [User Account Management](#user-account-management)
  - [4. Final Project](#4-final-project)

## 1. REST APIs

### Note on Lab Usage

In the Coursera lab environment, we need to run the following commands to set up the environment and start the Django server:

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
  - Headers are a core part of every request and carry extra information that helps the server decide how to present the content, such as 
    - cookies, 
    - user agents, 
    - and referrers.
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
  - The most commonly used status codes are 
    - `200`, `201`, 
    - `303`, `304`, 
    - `400`, `401`, `403`, `404`, 
    - and `500`.

#### HTTP Methods, Status Codes and Response Types

HTTP methods and status codes play an essential role in REST APIs. Following their conventions matters for two reasons:
- it prevents bugs early, making deployment to production smoother;
- it makes your API immediately understandable to other developers.

##### HTTP Methods

In REST APIs a single endpoint can serve multiple actions -- the method (verb) on the request tells the server what to do with the resource.

| Method | Action |
|---|---|
| `GET` | Returns the requested resource; responds with `404 Not Found` if it does not exist. |
| `POST` | Creates a new record from the JSON or form-encoded payload in the request body. Creating multiple resources in a single `POST` is possible but not a best practice. |
| `PUT` | Replaces a resource entirely; the payload must include all fields. Operates on a single resource. |
| `PATCH` | Updates selected fields of a resource; only the changed fields need to be in the payload. Operates on a single resource. |
| `DELETE` | Removes a resource (or a whole collection when sent to a collection endpoint). |

**Example calls**

```
GET  /api/menu-items                          -> list all items
GET  /api/menu-items/1                        -> single item
GET  /api/menu-items?category=appetizers      -> filtered list
GET  /api/menu-items?perpage=3&page=2         -> paginated list
```

- `GET` carries no payload; filters are passed as query-string parameters.

```
POST /api/menu-items
POST /api/orders
```

```json
// POST payload -- creates a new menu item
{
  "title": "Beef Steak",
  "price": 5.50,
  "category": "main"
}
```

```
PUT   /api/menu-items/1
PUT   /api/orders/1
```

```json
// PUT payload -- replaces item 1 completely; all fields required
{
  "title": "Chicken Steak",
  "price": 2.50,
  "category": "main"
}
```

```
PATCH /api/menu-items/1
PATCH /api/orders/1
```

```json
// PATCH payload -- updates only the price
{
  "price": 3.00
}
```

```
DELETE /api/menu-items        -> deletes the entire collection
DELETE /api/menu-items/1      -> deletes only item 1
DELETE /api/orders
DELETE /api/orders/1
```

##### Status Codes

Every API response must include an appropriate status code -- the code signals the outcome to the client and must match the actual result.

| Range | Category | Key codes and when to use them |
|---|---|---|
| `100–199` | Informational | `102 Processing` -- server is still working; client should poll again |
| `200–299` | Success | `200 OK` -- GET/PUT/PATCH/DELETE succeeded; `201 Created` -- POST created a new resource; `204 No Content` -- DELETE succeeded, no body returned |
| `300–399` | Redirection | `301 Moved Permanently` -- endpoint URL has changed (e.g. `/api/items` -> `/api/menu-items`); `304 Not Modified` -- cached response is still valid |
| `400–499` | Client error | `400 Bad Request` -- invalid or missing payload data; `401 Unauthorized` -- authentication required or token invalid; `403 Forbidden` -- authenticated but not permitted; `404 Not Found` -- resource does not exist |
| `500–599` | Server error | `500 Internal Server Error` -- unhandled exception; usually caused by missing validation or error handling. **Always avoid 5xx errors** -- they indicate code you must fix. |

##### Response Types and Content Negotiation

The most common response formats for REST APIs are JSON, XML, plain text, and YAML. Frameworks like Django REST Framework (DRF) include built-in **renderer** classes that serialise data into the requested format automatically.

The client declares its preferred format via the `Accept` request header; the server picks the best match -- a process called **content negotiation** -- and returns the data with the matching `Content-Type` response header.

| Response type | `Accept` header value(s) |
|---|---|
| JSON / JSONP | `application/json` |
| XML | `application/xml`, `text/xml` |
| YAML | `application/yaml`, `application/x-yaml`, `text/yaml` |
| HTML | `text/html` |

```http
GET /api/menu-items/1 HTTP/1.1
Accept: application/json
```

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 1, "title": "Bruschetta", "price": "8.00", "category": "appetizers"}
```

```http
GET /api/menu-items/1 HTTP/1.1
Accept: application/xml
```

```http
HTTP/1.1 200 OK
Content-Type: application/xml

<item><id>1</id><title>Bruschetta</title><price>8.00</price><category>appetizers</category></item>
```

DRF's `DEFAULT_RENDERER_CLASSES` setting controls which formats are available; `JSONRenderer` is included by default, and third-party packages (e.g. `djangorestframework-xml`, `djangorestframework-yaml`) add further renderers without requiring changes to view code.

#### RESTfulness

- REST (Representational State Transfer) is an architectural style for designing APIs; it is popular because it is easy to learn and can produce production-ready APIs quickly.
- An API is only RESTful if it satisfies six constraints:
  - **Client-server** -- a server serves resources and a client consumes them; the two are separated and independent.
  - **Stateless** -- the server holds no state for any client; each request must carry all the information the server needs to fulfil it.
  - **Cacheable** -- responses may be saved by browsers, proxies, or any intermediate system to reduce server load.
  - **Layered** -- the system can be split into decoupled layers (firewall, load balancer, web server, database) that can be added or removed independently.
  - **Uniform interface** -- every resource has a unique URL; resources are represented in a standard format (JSON or XML); clients interact with them consistently.
  - **Code on demand** *(optional)* -- the API may return executable code (e.g. a `<script>` tag) that the client runs to extend its behaviour.

![RESTful API Systems](./assets/restful_api_systems.png)

##### Resources

- Resources are the core objects a REST API exposes; every resource type maps to a distinct URL pattern.

```
GET /orders                         -> collection of all orders
GET /orders/16                      -> single order (id=16)
GET /orders/16/customer             -> sub-resource: customer of order 16
GET /orders/16/menu-items           -> sub-resource: items of order 16
GET /menu-items                     -> all menu items
GET /menu-items?category=appetizers -> filtered collection (same resource type)
```

- A collection endpoint (e.g. `/menu-items`) returns all resources of that type.
- A detail endpoint (e.g. `/menu-items/1`) returns one specific resource identified by its primary key.
- A sub-resource endpoint (e.g. `/orders/16/menu-items`) scopes the result to a parent resource.
- Query-string parameters filter or paginate a collection without changing the resource type.

##### Statelessness in Practice

- The server has no memory of previous requests; it returns exactly what the current request asks for, nothing more.
- A follow-up call to `/menu-items` after requesting `/orders/16` returns **all** menu items -- the server does not know the previous call was about order 16.
- Every request must therefore carry full context: use `/orders/16/menu-items` to scope results to a specific order, not a bare `/menu-items`.

#### Naming Conventions

Well-designed URI (Uniform Resource Identifier) endpoints convey purpose at a glance, making APIs easier for other developers to use and maintain. The rules below apply to every endpoint you expose.

- **Lowercase letters and hyphens** -- use `kebab-case` for all path segments; never use `snake_case`, `TitleCase`, or `camelCase` for static path words.
- **Path variables** -- represent dynamic IDs in `camelCase` wrapped in curly braces; `Id` is always capitalised.
- **Nouns, not verbs** -- resource names must be nouns; the HTTP method supplies the verb.
  - Good: `GET /orders`, `DELETE /users/{userId}`
  - Bad: `GET /getAllOrders`, `POST /users/{userId}/delete`
  - Never embed CRUD words (`create`, `read`, `update`, `delete`, `save`) in the path.
- **Forward slashes for hierarchy** -- indicate parent-child relationships by nesting with `/`; do not use `/` as a suffix.
- **No file extensions** -- never append `.json` or `.xml`; use a `format` query-string parameter instead.
- **Query strings for filtering and format** -- everything after `?` is a query string; use it for optional parameters that narrow or shape a collection.
- **No trailing slash** -- omit the final `/`; `orders/{orderId}` is correct, `orders/{orderId}/` is not.

```
# Lowercase + hyphens
GET  /menu-items                      OK
GET  /Menu-Items                      Not OK
GET  /menu_items                      Not OK

# camelCase path variables
GET  /orders/{orderId}                OK
GET  /orders/{order_id}               Not OK

# Hierarchical relationships
GET  /orders/{orderId}/menu-items     OK   items of a specific order
GET  /customers/{customerId}/orders   OK   orders of a specific customer
GET  /library/books/{bookId}/author   OK   author of a specific book

# Nouns, not verbs
GET    /orders                        OK
POST   /orders                        OK   HTTP method is the verb
DELETE /users/{userId}                OK
GET    /getAllOrders                  Not OK
POST   /orders/{orderId}/save         Not OK

# No file extensions -- use query string for format
GET  /orders/{orderId}?format=json    OK
GET  /orders/{orderId}.json           Not OK

# Query strings for filtering and pagination
GET  /menu-items?category=appetizers  OK
GET  /menu-items?perpage=3&page=2     OK

# No trailing slash
GET  /orders/{orderId}                OK
GET  /orders/{orderId}/               Not OK
```

#### Examples of Good and Bad Routes

Good API endpoint names follow a consistent set of rules. This reading walks through each rule with concrete good and bad examples.

##### Rule 01: Lowercase, Hyphens, No Abbreviations

- URI paths must be entirely lowercase; never use `camelCase`, `PascalCase`, or `Title Case` for static path segments.
- Separate multiple words with hyphens, not underscores; never abbreviate words.
- Dynamic path variables are the only exception: represent them in `camelCase` wrapped in `{}`.

| URI | Status | Why |
|---|---|---|
| `/customers` | Good | Plural and lowercase |
| `/customers/16/phone-number` | Good | Lowercase, hyphen separates words |
| `/customers/16/address/home` | Good | Lowercase, hierarchical, no trailing slash |
| `/users/{userId}` | Good | Variable in camelCase, no hyphen inside variable name |
| `/Customers` | Bad | Title case |
| `/generalMembers` | Bad | camelCase, no hyphens |
| `/MenuItems`, `/GeneralMembers` | Bad | PascalCase |
| `/customers/16/tel-no` | Bad | Abbreviation |
| `/customers/16/phone_number` | Bad | Underscore instead of hyphen |
| `/customers/16/phonenumber` | Bad | No word separation |
| `/users/{user-id}` | Bad | Variable uses hyphen instead of camelCase |

##### Rule 02: Forward Slash for Hierarchy

- Use `/` to express parent-child relationships between related resources; the path reads left-to-right from broadest to most specific.

```
# Store domain: customers -> orders -> menu items
/store/customers/{customerId}/orders     Good
/store/orders/{orderId}                  Good
/store/orders/{orderId}/menu-items       Good

# Library domain: authors -> books -> ISBN
/library/authors/books                   Good
/library/book/{bookId}/isbn              Good
```

##### Rule 03: Nouns for Resource Names, Not Verbs

- Resource names must always be nouns; the HTTP method (GET, POST, DELETE, ...) is the verb.
- Use plural nouns for collections (`/orders`, not `/order`).

| URI | Expects | Status | Why |
|---|---|---|---|
| `/orders` | Collection | Good | Plural noun |
| `/users/{userId}` | Single user | Good | Noun with correct variable convention |
| `/order` | Collection | Bad | Singular; use `/orders` for collections |
| `/getOrder` | Single resource | Bad | Verb in path, camelCase |
| `/getUser/{userId}` | Single user | Bad | Verb in path, camelCase |

##### Rule 04: Avoid Special Characters

- Never use special characters (`|`, `^`, `#`, `%`, etc.) in URI paths; they are confusing and can break parsers.
- To accept multiple IDs in a single request, separate them with a comma.

| URI | Status | Why |
|---|---|---|
| `/users/12,23,23/address` | Good | Comma as separator |
| `/users/12\|23\|23/address` | Bad | Pipe character `\|` |
| `/orders/16/menu^items` | Bad | Caret character `^` |

##### Rule 05: No File Extensions in URIs

- Never append `.json` or `.xml` to a URI; format selection belongs in a query string or the `Accept` header.
- The same applies to static asset endpoints: use a path segment (`/min`, `/source`) or a `format` query parameter.

| URI | Status | Why |
|---|---|---|
| `/sports/basketball/teams/{teamId}?format=json` | Good | Format in query string |
| `/sports/basketball/teams/{teamId}?format=xml` | Good | Format in query string |
| `/assets/js/jquery/3.12/min` | Good | No extension |
| `/assets/js/jquery/3.12/source` | Good | No extension |
| `/assets/js/jquery/3.12/?format=min` | Good | Format as query param |
| `/menu-items?format=json` | Good | Clean endpoint, format in query string |
| `/sports/basketball/teams/{teamId}.json` | Bad | File extension in URI |
| `/sports/basketball/teams/{teamId}.xml` | Bad | File extension in URI |
| `/menu-items.json` | Bad | File extension in URI |

##### Rule 06: Query Parameters for Filtering and Pagination

- All optional narrowing of a collection -- filtering by field value, pagination, sorting -- belongs in the query string, not in the path.
- Embedding filter values in path segments creates redundant, hard-to-read URIs.

| URI | Status | Why |
|---|---|---|
| `/users/{userId}/locations` | Good | Hierarchical path |
| `/users/{userId}/locations?country=USA` | Good | Filter in query string |
| `/articles?per-page=10&page=2` | Good | Pagination in query string |
| `/users/{userId}/locations/USA` | Bad | Filter value embedded in path |
| `/articles/page/2/items-per-page/10` | Bad | Pagination in path; redundant and obscure |

##### Rule 07: No Trailing Slash

- Omit the trailing `/` from every endpoint; a trailing slash implies a directory, not a resource, and causes inconsistency.

| URI | Status | Why |
|---|---|---|
| `/users/{userId}` | Good | No trailing slash |
| `/articles/{articleId}/author` | Good | No trailing slash |
| `/users/{userId}/` | Bad | Trailing slash |
| `/articles/{articleId}/author/` | Bad | Trailing slash |

#### Essential Tools for API Development

Three cross-platform tools cover the main ways to interact with APIs during development: a CLI (Command-Line Interface) tool, and two GUI (Graphical User Interface) clients.

- **curl** -- command-line HTTP client available on Windows (PowerShell), macOS, and Linux with no GUI.
  - Sends any HTTP method directly from the terminal; useful for quick scripted tests and CI pipelines.
  - `httpbin.org` is a free echo service that reflects back whatever you send -- ideal for testing.

```bash
# GET request -- httpbin echoes back the query arguments
curl "https://httpbin.org/get?project=LittleLemon"

# POST request -- send form data with -d; specify method with -X
curl -X POST -d "project=LittleLemon" "https://httpbin.org/post"

# POST JSON body
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"project": "LittleLemon"}' \
     "https://httpbin.org/post"
```

- **Postman** -- cross-platform desktop app and web version with an advanced GUI for building, testing, and documenting APIs.
  - Supports collections, environments, automated tests, and mock servers.
  - Good for team collaboration and long-lived API workspaces.
- [**Insomnia**](https://insomnia.rest/) -- free, cross-platform desktop REST client for storing, organising, and executing API requests; desktop-only (no web version).
  - All requests are saved in **Request Collections** that persist between sessions.
  - Supports GET, POST, and all other HTTP methods; POST bodies can be entered as Form URL Encoded or JSON in the Body tab.

**Insomnia quick-start workflow:**

1. Click **Create** -> **Request collection**, name it, and click **Create**.
2. Click the **+** icon in the left sidebar -> **HTTP Request** (or `Cmd+N` / `Ctrl+N`).
3. Rename the request, select the HTTP method from the dropdown, and enter the URL.
4. For GET: add query parameters in the **Query** tab; click **Send**.
5. For POST: select the method, open the **Body** tab, choose **JSON** or **Form URL Encoded**, fill in key-value pairs, and click **Send**.

```
# Insomnia GET example
Method: GET
URL:    https://httpbin.org/get?project=LittleLemon
-> Response body echoes back: { "args": { "project": "LittleLemon" }, ... }

# Insomnia POST example
Method: POST
URL:    https://httpbin.org/post
Body (JSON): { "project": "LittleLemon" }
-> Response body echoes back: { "json": { "project": "LittleLemon" }, ... }
```

#### Setting Up a Django REST Framework Project

- The course sets up the project with `pipenv`; this guide uses `uv` instead, since it manages the virtual environment and dependency lockfile together and is faster.
- Project setup workflow:
  - Create a project directory, then create a virtual environment pinned to a specific Python version with `uv venv --python 3.11`.
  - Add Django and the DRF (Django REST Framework) packages as dependencies with `uv add`; this updates `pyproject.toml` and `uv.lock`, then installs them.
  - Activate the virtual environment (or skip activation and prefix commands with `uv run`).
  - Scaffold the Django project with `django-admin startproject <ProjectName> .` -- the trailing dot creates it in the current directory instead of a nested subfolder.
  - Create an app inside the project with `python manage.py startapp <AppName>`.
  - Run the development server with `python manage.py runserver`; it serves on port 8000 by default, or on a custom port when one is passed as an argument (e.g. `runserver 8080`).
  - In VS Code, open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run **Python: Select Interpreter** to pick the `uv`-created virtual environment -- this step matters because it makes the integrated terminal auto-activate that environment, so commands like `manage.py runserver` work in any new terminal tab without manual activation.
- Everyday `uv` commands used beyond initial setup:
  - `uv lock` / `uv sync` -- refresh the lockfile from `pyproject.toml`, or install/sync the environment to match `pyproject.toml` and `uv.lock`.
  - `uv add <package>` / `uv remove <package>` -- add or remove a dependency, updating the lockfile automatically.
  - `uv run <command>` -- run a command (script, `pytest`, etc.) inside the project's virtual environment without activating it manually.
  - `git submodule update --init --recursive` -- pull in any git submodules the project depends on.

```bash
# Create the project directory and a virtual environment with the correct Python version
cd labs/01-little-lemon-api
mkdir LittleLemon && cd LittleLemon
uv venv --python 3.11

# Add Django + DRF packages to pyproject.toml, update the lockfile, and install them
uv add django djangorestframework djangorestframework-xml djoser
uv sync

# Activate the virtual environment
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

# Scaffold the Django project (the trailing dot avoids a nested subfolder) and app
uv run django-admin startproject LittleLemon .
uv run python manage.py startapp LittleLemonAPI

# Run the development server
uv run python manage.py runserver        # default port 8000, http://127.0.0.1:8000
uv run python manage.py runserver 8080   # custom port

# Other everyday uv/related commands
uv lock                                  # refresh uv.lock without installing
uv sync                                  # create/sync the venv with pyproject.toml + uv.lock
uv run <command>                         # run any command inside the project environment
git submodule update --init --recursive  # update submodules
```

#### How to Use Insomnia

This section uses the desktop REST API client [Insomnia](https://insomnia.rest/) to make HTTP requests against `httpbin.org`, an open-source echo service that reflects back whatever is sent, with no server-side setup required.

##### Getting Started

- Open Insomnia and go to the collection tab -- the tab used to be labelled **Debug** and is now labelled **Collection**.
- On launch, Insomnia offers a choice between signing in/creating an account or using **Scratch Pad** mode:
  - Scratch Pad lets you use the full app locally without an Insomnia (Kong) account.
  - Requests, collections, and environments are stored only on your machine (typically under your local app-data folder) rather than synced to Insomnia's cloud.
  - There is no team sharing, cloud sync, or multi-device access -- it is local storage for solo, offline use.
  - You can switch to a signed-in account later and migrate/import the scratch pad data if needed.
  - This exercise uses Scratch Pad mode.

##### Running httpbin Locally with Docker (Optional)

- The [httpbin.org](https://httpbin.org/) website exposes an **HTTP Methods** menu listing the endpoints available for each verb (`DELETE`, `GET`, `PATCH`, `POST`, etc.).
- Since the public `httpbin.org` service can be unreliable, a local alternative is running its Docker image instead:

```bash
docker pull kennethreitz/httpbin
docker run -p 8081:80 kennethreitz/httpbin
# Then access the local instance at http://localhost:8081

# To stop the container:
docker ps                    # find the container ID/name
docker stop <container_id>   # gracefully stop it
docker rm <container_id>     # optional: remove the stopped container
# ... or stop the most recently started container:
docker stop $(docker ps -lq)
# ... or press Ctrl+C in the terminal where it was started, if run without -d
```

![The HTTP Methods menu on the httpbin.org website includes options such as DELETE, GET, PATCH and POST](./assets/httpbin_docker_https_methods.png)

##### Create a GET Request

1. Click the **+** icon on the left-hand side of Insomnia and select **HTTP Request** from the drop-down menu.

   ![New Request in Scratch Pad Collection](./assets/insomnia_new_request.png)

2. Double-click the new request to rename it, e.g. `GET request using Insomnia`.

   ![GET Method](./assets/insomnia_get_method.png)

3. Open the method dropdown and (re-)select `GET`. Set the URL to `https://httpbin.org/get` or `http://localhost:8081/get`, then press **Send**.
   - The JSON response echoes the request's headers, origin, and (empty) args:

```json
{
	"args": {},
	"headers": {
		"Accept": "*/*",
		"Host": "localhost:8081",
		"User-Agent": "insomnia/13.0.2"
	},
	"origin": "172.xxx.xxx.xxx",
	"url": "http://localhost:8081/get"
}
```

   ![Insomnia GET Request](./assets/insomnia_get_request.png)

4. Under the **Body** dropdown, select **Multipart Form Data**, add a `title: Lord of the Rings` name/value pair, and press **Send** again.
   - `Content-Length` in the response updates to reflect the added form field.

   ![Insomnia GET Request](./assets/insomnia_get_method_2.png)

5. Add a second form entry, `author: JRR Tolkien`, and press **Send** again -- `Content-Length` increases further:

```json
{
	"args": {},
	"headers": {
		"Accept": "*/*",
		"Content-Length": "200",
		"Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
		"Host": "localhost:8081",
		"User-Agent": "insomnia/13.0.2"
	},
	"origin": "172.xxx.xxx.xxx",
	"url": "http://localhost:8081/get"
}
```

6. Use the **Filter response body** field in the bottom-right of Insomnia to query the JSON output with a JSONPath-style dot notation.

   ![Insomnia Filter Response Body](./assets/insomnia_get_method_3.png)

   - Filter `$.origin` narrows the preview to the matching field:

```
$.origin
```

```json
[
	"172.xxx.xxx.xxx"
]
```
7. Refine the filter incrementally to drill into nested fields:
   - `$.headers` returns the full headers object:

```
$.headers
```

```json
[
	{
		"Accept": "*/*",
		"Content-Length": "200",
		"Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
		"Host": "localhost:8081",
		"User-Agent": "insomnia/13.0.2"
	}
]
```

   - `$.headers.Content-Type` narrows further to a single field:

```
$.headers.Content-Type
```

```json
[
	"multipart/form-data; boundary=X-INSOMNIA-BOUNDARY"
]
```

   - The dot operator navigates the JSON structure; `Content-Type` shows `multipart/form-data` because the body used the Multipart Form option.
   - Clear the filter field afterward to see the full response again.

8. Deselect the `title` form field and re-send the `GET` request -- `Content-Length` changes again to reflect the smaller payload.

9. *(Optional)* Explore Insomnia's other configuration options to get more familiar with the tool now that the basic `GET` workflow is clear.

##### Create a POST Request with Form Data

1. Click **+** and select **HTTP Request** to create a new request.

   ![Insomnia POST Request](./assets/insomnia_post_request.png)

2. Keep the same form data, change the method to `POST`, set the URL to `https://httpbin.org/post` or `http://localhost:8081/post`, and press **Send**.

   ![Form data output of a POST request in Insomnia](./assets/insomnia_post_method.png)

```json
{
	"args": {},
	"data": "",
	"files": {},
	"form": {
		"author": "JRR Tolkien",
		"title": "Lord of the Rings"
	},
	"headers": {
		"Accept": "*/*",
		"Content-Length": "200",
		"Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
		"Host": "localhost:8081",
		"User-Agent": "insomnia/13.0.2"
	},
	"json": null,
	"origin": "172.xxx.xxx.xxx",
	"url": "http://localhost:8081/post"
}
```

   - Unlike the `GET` response, the `POST` response now includes a populated `form` object with the submitted fields.

1. Explore the other output tabs: **Headers**, **Cookies**, and **Timeline**.

```
# Headers tab output
Server: gunicorn/19.9.0
Date: Thu, 02 Jul 2026 09:50:24 GMT
Connection: keep-alive
Content-Type: application/json
Content-Length: 427
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

##### Create a POST Request with JSON Data

1. Create another **HTTP Request** via the **+** icon, as before.
2. Set the method to `POST` and label the request, e.g. `POST Request with JSON` -- labels are for reference only and independent of the actual request type.
3. Set the URL to `https://httpbin.org/post` or `http://localhost:8081/post`.
4. Under the **Body** dropdown, select **JSON** as the text input type; a text area appears for the body content.
5. Enter the following JSON body and press **Send**:

```json
{
    "title": "Lord of the Rings",
    "author": "JRR Tolkien",
    "published" : {
        "year": 1954,
        "month": "july",
        "day" : 29
    }
}
```

   - Note: if the response's `json` field shows `null` instead of the parsed object, remove any extra indentation Insomnia may have auto-inserted into the body and re-enter it (select all, clear, then use Tab for indentation) -- stray leading whitespace can break JSON parsing on the server.
   - Expected response:

```json
{
	"args": {},
	"data": "{\n    \"title\": \"Lord of the Rings\",\n    \"author\": \"JRR Tolkien\",\n    \"published\" : {\n        \"year\": 1954,\n        \"month\": \"july\",\n        \"day\" : 29\n    }\n}",
	"files": {},
	"form": {},
	"headers": {
		"Accept": "*/*",
		"Content-Length": "181",
		"Content-Type": "application/json",
		"Host": "localhost:8081",
		"User-Agent": "insomnia/13.0.2"
	},
	"json": null,
	"origin": "172.xxx.xxx.xxx",
	"url": "http://localhost:8081/post"
}
```

   - The exercise expects the parsed body to also appear in the `json` field alongside the raw `data` string; in this run `json` stayed `null` even after re-entering the body, which points at the indentation/whitespace issue noted above rather than a problem with the request itself.
6. Filter the response body to drill into the JSON payload:
   - `$.json.published.year`:

```
$.json.published.year
```

```json
[
	1954
]
```

   - Bracket notation is also valid, e.g. `$[json][published][day]`:

```json
[
  29
]
```


### Principles of API Development

#### REST Best Practices

A REST API is easy to create, but planning the architecture up front is what makes it robust, reliable, and able to perform well under load. The following best practices help with that.

- **KISS (keep it simple, stupid)** -- a single API endpoint should do one specific job and do it well, not perform too many tasks at once.
  - Bad design example: one endpoint that both finds the current item of the day, clears its status, and randomly picks a new item -- this overloads the endpoint with responsibilities, and a random pick might not reflect the actually most popular item.
  - Better design: split the work into two focused calls, each updating a single menu item's status (see code example below). This removes any chance of accidentally picking the wrong item and keeps each endpoint simple and focused.
- **Filtering, ordering, and pagination** -- always let clients narrow and reshape large result sets rather than returning everything at once.
  - Filtering: accept query-string parameters so a client can request a subset, e.g. only appetizers or only mains, instead of the full collection.
  - Ordering: let clients rearrange results in ascending or descending order.
  - Pagination: deliver results in smaller chunks instead of thousands of records at once; the client controls the page number and page size (e.g. requesting 4 items from page 10 of 16 total pages).
- **Versioning** -- breaking changes to an API's response can break client applications, so use versioning to stay safe.
  - Decide per change whether it needs a new version or can be handled as a modification to the existing representation.
  - As a rule of thumb, support only two versions of any given resource at a time, since maintaining many versions in parallel is complex, error-prone, and costly.
- **Caching** -- an API should be cacheable to reduce load on the database, so always implement caching and send the relevant HTTP headers in responses to minimize repeated client calls.
  - Cache a resource's result the first time it is requested, then serve the cached result on subsequent calls instead of hitting the database again.
  - Only refresh the cache when the underlying data changes (a menu item is modified or added); until then, repeated requests are served from cache, saving computing power.
- **Rate limiting and monitoring** -- protect the API and keep it healthy over time.
  - Rate limiting caps how many times a client can call the API within a period (per minute, hour, day, or even per 30 days) to prevent abuse.
  - Monitor latency to ensure clients get good response times.
  - Monitor status codes, especially the `4xx` and `5xx` ranges, to catch problems early.
  - Monitor network bandwidth to detect abuse of the API.

```http
# KISS: two focused PATCH calls instead of one endpoint that does everything

# 1. Manager clears the previous "item of the day" (item 16)
PATCH /menu-items/16
Content-Type: application/json

{ "status": "Off" }

# 2. Manager manually sets the new "item of the day" (item 21)
PATCH /menu-items/21
Content-Type: application/json

{ "status": "On" }

# Pagination: request page 10 of 16, 4 items per page
GET /menu-items?page=10&perpage=4
```

#### Security and Authentication in REST APIs

APIs make data accessible not just to your own apps but to third-party clients too, which is exactly what makes them a risk: since they are publicly reachable, they give outside applications a path to your server and database, so securing them is essential.

- **SSL (Secure Socket Layer)** -- encrypts data in transit between the browser and the web server.
  - With SSL certificates installed correctly, API endpoints are served over HTTPS instead of plain HTTP.
  - Always check that an API's endpoint starts with `https://`, not `http://`.
- **Signed URLs** -- restrict which clients can call an API, e.g. only a project's own mobile app and website.
  - A signed URL includes a **signature**, a piece of text attached to the request that the server verifies to confirm the call comes from an authentic source, granting limited, time-boxed access to a specific resource.
  - HMAC (Hash-based Message Authentication Code) is a popular, easy-to-use signing mechanism: it runs a secret message through a digest algorithm together with a secret key to produce the signature, which ensures both authenticity and integrity of the message.
- **Authentication** -- verifies who is calling the API.
  - Basic (HTTP) authentication requires the client to send a username and password with every single call, which is both inconvenient and less secure.
  - Token-based authentication is preferred instead: the client sends its username and password once to a sign-in endpoint and receives a unique token in return.
    - Every subsequent API call includes that token in an HTTP header instead of the raw credentials.
    - The server validates the token, extracts the encoded information, matches it to an existing user, and then performs the request on that user's behalf.
    - Tokens can be generated with an ad hoc policy from the backend framework, or with an industry-standard format like JWT (JSON Web Token).
  - Two HTTP status codes are central to authentication:
    - `401 Unauthorized` -- the username/password (or token) do not match; the server cannot proceed.
    - `403 Forbidden` -- the credentials are valid and identity is confirmed, but the identified user lacks permission to perform the requested action.
- **CORS (Cross-Origin Resource Sharing) and firewalls** -- control which origins and clients may reach the API at the network/browser level.
  - CORS headers can restrict an API to accept calls only from specific domains instead of from anywhere.
  - A firewall can further restrict access to only specific IP addresses at the server level.

```http
# Token-based authentication: header sent with every call after sign-in
GET /api/menu-items HTTP/1.1
Authorization: Token xxx

# CORS: restrict an API response to a single trusted origin
Access-Control-Allow-Origin: https://www.littlelemon.com
```

#### Access Control

API responses can carry sensitive data (e.g. a customer's delivery address), so not every caller should be able to reach every endpoint -- for the Little Lemon project, order-detail APIs should only be reachable by manager and delivery-crew accounts, and anyone else should be denied. Access control is what lets you specify which users can access which parts of an API and which data they can see.

- **Roles and privileges** are the building blocks of an access control system.
  - A **privilege** is permission to perform one particular task.
  - A **role** is a named collection of privileges assigned to a type of user.
  - Example roles for the Little Lemon project:
    - **Customer** -- browse menu items, add items to the cart, place orders, add food reviews, browse their own orders.
    - **Manager** -- add/edit/delete menu items, browse all orders, browse customer data, assign orders to the delivery crew, browse transaction data.
    - **Delivery crew** -- browse orders assigned to them, update the status of an assigned order.
  - Larger projects can define further roles (administrators, senior managers, HR accounts, etc.); the more detailed and specific each role's privileges are, the better the resulting access control system.
- **Authorization vs. authentication** -- authorization is just another term for access control, and it is a distinct concept from authentication.
  - Authentication verifies identity and gets a user in.
  - Authorization determines what an already-authenticated user is allowed to do (or prevented from doing).
- **Handling users who need multiple roles' worth of privileges** -- e.g. a general manager who must be able to do everything an accountant, an HR representative, and a normal manager can do. Two design approaches:
  - Create one combined role with all the necessary privileges bundled in, then update/edit that role's privileges over time as needs change -- keeps a single role tailored and up to date.
  - Assign a user multiple task-specific roles instead (accountant, HR, manager), so each role stays narrowly scoped to its own team, and the general manager is simply granted all three roles.
    - This composition approach means a new privilege added to one role (e.g. accountant) automatically propagates to any user holding that role, including the general manager.
- Investing time in designing roles and privileges up front is not optional polish -- it avoids costly debugging and refactoring later, and a well-designed access control system saves the whole project time and money in the long run.

#### Authentication vs. Authorization

- APIs expose backend data to third-party clients, so without proper security anyone could tamper with the data or read sensitive information.
- Authentication and authorization both control access, but they are not the same thing.

##### Authentication

- Authentication verifies a user's credentials, e.g. logging in with a username and password.
- On a match, the site sets cookies in the browser; later requests send those cookies in the HTTP headers, and the server recognizes them plus server-side session data, so no re-login is needed until logout.
- Token-based API authentication:
  1. Client sends username and password.
  2. Server returns a bearer token; the client includes it on every later call, and the server verifies it before deciding whether to allow the action -- that decision is authorization.
- Invalid credentials return `401 Unauthorized`.

**Authentication process: getting an access token**

![Diagram of the process of getting an access token](./assets/authentication-and-authorization-1.png)

**Authenticated API calls**

![Diagram of an authenticated API call](./assets/authentication-and-authorization-2.png)

##### Authorization

- Authorization checks, after authentication, whether the user has the privileges to perform a given task.
- Server-side, this is done by assigning the user to one or more groups; after token verification, the server checks group membership for the requested action.
- Missing the required group returns `403 Forbidden`.
- This layer ensures only privileged users can access or modify data, preventing data corruption and breaches.

**API authorization**

![Diagram of API authorization](./assets/authentication-and-authorization-3.png)

##### Implementing Authorization

- Privileges are the individual tasks a user can perform -- the building blocks of authorization.
- Identify the needed privileges first; for a bookshop: browse books, add books, edit books, delete books, place orders.
- Not every user gets every privilege -- e.g. customers can't add/edit books, but managers can.
- Distribute privileges across roles, then check role/group membership in each endpoint's backend code to allow or deny the action.

##### User Groups in Django

- The Django admin panel has built-in support for user groups, split into **Users** and **Groups** sections.

![Django admin panel with two sections for users and groups](./assets/authentication-and-authorization-4.png)

- Create roles (`Manager`, `Editor`, `Customer`, `Admin`, etc.) via **Groups -> Add**; Django lists available privileges based on the project's models, e.g. for a bookshop:

![Django admin panel with bookshop privileges listed](./assets/authentication-and-authorization-5.png)

- Example: an `Editor` role with its privileges.

![Django admin panel with Editor role and privileges](./assets/authentication-and-authorization-6.png)

- Example: a `Customer` role with different privileges.

![Django admin panel with Customer role and privileges](./assets/authentication-and-authorization-7.png)

- Groups can be edited anytime as the project grows.

![Django admin panel with two user roles](./assets/authentication-and-authorization-8.png)

- Defining groups isn't enough by itself -- views still need code that checks group membership and acts on it, covered later in the course.

### Writing Your First API

#### BookAPI List Project

- Project brief: a bookstore needs a website and mobile app so managers can add/edit books quickly and visitors can browse the collection -- both are served by the same underlying API.
- Data model: a `Book` model backs the storage table and bridges the data with the business logic.
  - `title` -- `CharField`, `max_length=255`.
  - `author` -- `CharField`, same specs as `title`.
  - `price` -- `DecimalField`, `max_digits=5`, `decimal_places=2`.
  - `inventory` -- optional `PositiveSmallIntegerField` indicating whether a book is in stock.
- Endpoints, following REST conventions:
  - `GET /api/books` -- returns every book in the database; the `inventory` field lets the client distinguish books in stock from books out of stock.
  - `GET /api/books/{bookId}` -- returns a single book.
    - `404` if the requested id doesn't exist.
    - `200` on success; the payload is a single JSON object, not wrapped in square brackets, since it is one resource, not an array element.
  - `POST /api/books` -- creates a new book from the request payload.
    - `201` plus the newly created book on success.
    - `400` plus an error message if required data (e.g. the author) is missing.
  - `PUT /api/books/{bookId}` and `DELETE /api/books/{bookId}` -- edit and delete a single book, reusing the same detail URL pattern (`api/books/<pk>`).
- Converting a model instance to a JSON response:
  - `model_to_dict` (from `django.forms.models`) turns a retrieved model instance into a dict.
  - `JsonResponse` (from `django.http`) serializes that dict into the HTTP response.
- Parsing the request body: a `POST`/`PUT` payload arrives as either a raw JSON string or a form URL-encoded string.
  - `QueryDict` (from `django.http`) parses that raw body into a Python dictionary-like object so individual fields become accessible.
- Recap: define the model first, then the collection/detail endpoints, then the model-to-JSON conversion, then the create/edit/delete handlers that parse the request body -- planning the steps up front minimizes debugging once you start writing the actual view code.

```python
# models.py
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.PositiveSmallIntegerField(blank=True, null=True)
```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("api/books", views.books),            # collection: GET, POST
    path("api/books/<int:pk>", views.book_detail),  # detail: GET, PUT, DELETE
]
```

```python
# views.py
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, QueryDict

from .models import Book


def books(request):
    if request.method == "GET":
        # GET /api/books -> list all books
        return JsonResponse(list(Book.objects.values()), safe=False)

    if request.method == "POST":
        # POST /api/books -> create a book from the JSON/form payload
        payload = QueryDict(request.body)
        title, author = payload.get("title"), payload.get("author")
        if not title or not author:
            return HttpResponseBadRequest()  # 400: required data missing
        book = Book.objects.create(title=title, author=author, price=payload.get("price"))
        return JsonResponse(model_to_dict(book), status=201)


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponseNotFound()  # 404

    if request.method == "GET":
        return JsonResponse(model_to_dict(book))  # 200, single object, not a list

    if request.method == "PUT":
        payload = QueryDict(request.body)
        book.title = payload.get("title", book.title)
        book.author = payload.get("author", book.author)
        book.save()
        return JsonResponse(model_to_dict(book))

    if request.method == "DELETE":
        book.delete()
        return JsonResponse({}, status=204)
```

#### Organizing an API Project

- Upfront planning and organization make a project maintainable, saving effort later when extending it, adding features, or debugging.
- Split a big app into multiple apps, each decoupled and dealing with one particular set of related concerns -- an essential step for staying productive with Django.
  - Break the overall goal into smaller sub-goals first, then create one app per sub-goal, instead of building a single app that does everything.
  - Without this split, an app keeps absorbing new features until it becomes unmanageable: further features take longer to add, bugs become harder to isolate, and the project can turn into one large, hard-to-touch block.
- Once a project has multiple apps, several other practices keep it healthy:
  - Use a virtual environment instead of the global environment for dependencies, since projects differ in which packages -- and which package versions -- they need; a shared global environment creates version conflicts.
    - `uv` (this guide's tool of choice) creates and manages a project's virtual environment together with its dependency lockfile (`pyproject.toml` + `uv.lock`) in one step, and is fast.
    - `pipenv` is a lighter-weight alternative that achieves the same per-project isolation via a `Pipfile`/`Pipfile.lock` pair.
  - Version an API when upgrading it, since a new version's response can differ from the old one and would otherwise break existing clients.
    - Keep the old, working API intact and add the new version as a separate app, rather than modifying the old app in place, so client developers have time to migrate.
  - Record dependencies and their exact version numbers so the project doesn't break on deployment or for a new contributor picking it up.
    - With `uv`, `pyproject.toml` and `uv.lock` already track dependencies and their inter-dependencies precisely, so no separate requirements file is needed day-to-day; `uv export --format requirements-txt > requirements.txt` can still produce one for tools that expect that format.
    - With `pipenv`, the `Pipfile.lock` plays the same tracking role; it too removes the day-to-day need for a `requirements.txt`, though `pipenv` can bootstrap a project's dependencies from an existing `requirements.txt` the first time.
    - With plain `pip` (no lockfile tool), generate that file manually with `pip3 freeze > requirements.txt`.
  - Give each app its own resource folder (static files, templates) instead of one shared folder, to avoid naming conflicts and manage files more efficiently.
  - Split one large settings file into several smaller files included from the main settings file (e.g. via the `django-split-settings` package), instead of a single long file that's hard to edit and search.
  - Keep business logic in the models rather than the views, so the logic lives in one organized place; models become more powerful, decoupled, and reusable, and less code is needed overall.

```bash
# uv: dependencies are already locked in pyproject.toml + uv.lock;
# export a requirements.txt only if some tool needs that format
uv export --format requirements-txt > requirements.txt

# plain pip: no lockfile, so freeze the environment manually
pip3 freeze > requirements.txt
```

#### Consequences of a Poorly Designed API Project

Skipping conventions, error checks, security checks, and performance planning has concrete costs. Main failure modes:

- **Data breach** -- caused by weak security checks, missing authentication/authorization, wrong file permissions, or no SSL.
  - Fix: solid authorization layer, proper security checks, double-check sensitive endpoints before production.
- **Data corruption** -- caused by missing authentication/authorization or missing input validation/sanitization.
  - Fix: validate and sanitize all input before processing or saving, on top of auth checks.
- **Wasted compute and memory** -- caused by unoptimized code/logic, unoptimized queries or model relationships, missing indexes, no caching.
  - Fix: optimize code and database access before deploying to production.
- **Wasted bandwidth** -- caused by missing caching headers/policy, missing pagination and filtering.
  - Fix: send proper caching headers; implement filtering and pagination.
- **Bad user experience** -- caused by ignoring naming conventions, wrong HTTP status codes, ignoring `Accept` headers, missing pagination/sorting/searching/filtering, weak error checking.
  - Fix: follow naming conventions, implement filtering/sorting/searching/pagination, keep error checking and tests to avoid unexpected `5xx`s.
- **Breaking client applications** -- caused by no versioning system, so a new API's request/response shape can break existing clients instantly.
  - Fix: version the API instead of changing an existing version in place (see [Organizing an API Project](#organizing-an-api-project)).
- **Failure to manage the app** -- caused by one big Django app with all business logic in the views.
  - Fix: split into multiple smaller, decoupled apps; move reusable business logic into the models.

#### XML and JSON Response Types

- Clients should always be able to request their preferred content type via the `Accept` request header (see [HTTP Methods, Status Codes and Response Types](#http-methods-status-codes-and-response-types)); this section compares the two formats seen most often: JSON and XML.
- Request headers for each format:
  - JSON -- `Accept: application/json`
  - XML -- `Accept: application/xml` or `Accept: text/xml`
- The same `GET` request renders the same underlying data differently depending on which `Accept` header is sent:

![An API request for a JSON response](./assets/XML-and-JSON-response-types-1.png)

![An API request for an XML response](./assets/XML-and-JSON-response-types-2.png)

- Data conversion in Django REST Framework (DRF): built-in renderers convert data to JSON and display it in the browsable API viewer; third-party renderer classes add XML or YAML support.
- JSON vs. XML tradeoffs:
  - **Format style** -- JSON is a lightweight, dependency-free key-value format; XML is a tag-based format similar to HTML that can represent more complex, attribute-rich data while staying readable.
  - **Size and bandwidth** -- JSON is smaller and uses less bandwidth; XML is lengthier and uses more.
  - **Performance** -- generating and parsing JSON is faster and uses less memory and compute than XML.
  - **Comments** -- XML supports comments; JSON has no comment syntax.
  - **Popularity** -- JSON is especially popular with JavaScript developers, since it parses directly into a native object.

```json
// JSON: key-value pairs
{
  "author": "Jack London",
  "title": "Seawolf"
}
```

```xml
<!-- XML: tag-based, no key-value pairs -->
<?xml version="1.0" encoding="UTF-8"?>
<root>
   <author>Jack London</author>
   <title>Seawolf</title>
</root>
```

```json
// JSON: arrays stay compact
{
  "items": [1, 2, 3, 4, 5]
}
```

```xml
<!-- XML: arrays need one element per item -- much more verbose -->
<?xml version="1.0" encoding="UTF-8"?>
<root>
   <items>
      <element>1</element>
      <element>2</element>
      <element>3</element>
      <element>4</element>
      <element>5</element>
   </items>
</root>
```

#### Exercise: Build a Simple API

Folder: [`lab/02-booklist-api/`](./lab/02-booklist-api/) ([`Instructions.md`](./lab/02-booklist-api/Instructions.md)).

- Goal: build a plain-Django (no DRF) Booklist API with endpoints to list books and add a new book, following the [BookAPI List Project](#bookapi-list-project) design.
- Scenario: a bookshop manager needs to add books from the website/app; the manager and visitors need to browse the collection.
- Project layout: a Django project `BookList` with a single app `BookListAPI`.
- The starter project used `pipenv` (`Pipfile`); replaced with `uv` (`pyproject.toml` + `uv.lock`), consistent with the rest of this guide.

```bash
# Set up the environment with uv instead of pipenv
cd 04_APIs/lab/02-booklist-api/BookList
uv venv --python 3.11
uv add django djangorestframework djangorestframework-xml djoser
uv sync

# Migrations and dev server
uv run python manage.py makemigrations BookListAPI
uv run python manage.py migrate
uv run python manage.py createsuperuser   # username: admin, password: books@123!
uv run python manage.py runserver 8080
```

- `models.py` -- `Book` model with the three required fields plus the optional `inventory` field from the exercise's "Additional Step", and a `Meta.indexes` entry on `price`:

```python
# BookListAPI/models.py
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]
```

- `admin.py` -- register `Book` so it appears in the Django admin panel:

```python
# BookListAPI/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

- `BookListAPI/urls.py` (new file) -- app-level URL for the collection endpoint:

```python
# BookListAPI/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('books', views.books),
]
```

- `BookList/urls.py` -- wire the app's URLs under `/api/`:

```python
# BookList/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BookListAPI.urls')),
]
```

- `views.py` -- one function-based view handling `GET` (list) and `POST` (create); `csrf_exempt` since API clients don't send a CSRF token:

```python
# BookListAPI/views.py
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Book


@csrf_exempt
def books(request):
    if request.method == 'GET':
        # GET /api/books -> list all books
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})

    elif request.method == 'POST':
        # POST /api/books -> create a book from the form-encoded payload
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        book = Book(title=title, author=author, price=price, inventory=inventory)
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)
        return JsonResponse(model_to_dict(book), status=201)
```

- Verified end to end with `uv run python manage.py runserver 8080` and `curl`:

```bash
# GET -- empty collection initially
curl http://127.0.0.1:8080/api/books
# {"books": []}

# POST -- create a book
curl -X POST http://127.0.0.1:8080/api/books \
     -d "title=Northanger Abbey" -d "author=Jane Austen" -d "price=18.20" -d "inventory=5"
# {"id": 1, "title": "Northanger Abbey", "author": "Jane Austen", "price": "18.20", "inventory": "5"} -- 201 Created

# GET -- new book now listed
curl http://127.0.0.1:8080/api/books
# {"books": [{"id": 1, "title": "Northanger Abbey", "author": "Jane Austen", "price": "18.20", "inventory": 5}]}

# POST with a required field missing -> 400
curl -X POST http://127.0.0.1:8080/api/books -d "author=NoTitleAuthor" -d "price=1.00"
# {"error": "true", "message": "required field missing"}
```

#### Debugging your API

- Debugging is the process of finding and fixing code errors efficiently instead of guessing; it also builds a better understanding of how the program actually works.
- VS Code (Visual Studio Code) ships a built-in debugger for Django projects.
  - Open the project in VS Code, select the Python interpreter for the project's virtual environment from the command palette, then open the debugger panel from the sidebar icon.
  - On first use, click the panel's **create a launch.json file** link, then:
    - pick **Python** > **Django** from the configuration list.
  - Two run options are available: **Start Debugging** and **Run Without Debugging**.
    - Start Debugging activates the virtual environment and starts the dev server automatically, so it does not need to be started manually.
- Key debugging concepts:
  - A **breakpoint** is a line where execution intentionally pauses so variable values can be inspected at that point; toggle one by clicking the red dot beside a line number.
  - The **watch** list tracks chosen variables and shows their values as they change; add a variable via the plus icon in the watch panel.
- The debug toolbar appears once execution pauses at a breakpoint and offers six controls:
  - **Continue/Pause** -- runs to the next breakpoint.
  - **Step Over** -- executes the current line and pauses at the next one, without entering called functions.
  - **Step Into** -- enters a called function and pauses there.
  - **Step Out** -- returns to the caller's line from inside a function.
  - **Restart** -- restarts the debugging session.
  - **Stop** -- ends the debugging session and stops the dev server.
- Worked example: a view meant to return even numbers displayed nothing in the browser.
  - A breakpoint on the line appending a number to the result never triggered, meaning the remainder was never equal to `0`.
  - Adding `remainder` to the watch list and stepping through showed its value increasing by `0.5` per iteration -- impossible for a true modulo remainder.
  - Root cause: the code used the division operator (`/`) instead of the modulo operator (`%`).
  - After fixing the operator, removing the breakpoints, and restarting, the endpoint correctly returned only even numbers.

```python
# views.py -- before fix: '/' instead of '%' means remainder is never 0, so nothing is ever appended
def numbers(request):
    evens = []
    for number in range(20):
        remainder = number / 2       # bug: division instead of modulo
        if remainder == 0:
            evens.append(number)
    return JsonResponse({'evens': evens})


# views.py -- after fix: modulo operator correctly identifies even numbers
def numbers(request):
    evens = []
    for number in range(20):
        remainder = number % 2       # fixed: modulo
        if remainder == 0:
            evens.append(number)
    return JsonResponse({'evens': evens})
```

#### Browser Tools and Extensions for API Development

- Every browser ships a developer console with tools for debugging API calls made from a website's JavaScript; the examples below use Chrome, but equivalent tools exist in every major browser.
  - Open DevTools (Developer Tools) with 
    - `Ctrl+Shift+I` on Windows/Linux 
    - or `Cmd+Option+I` on macOS.
- The **Network** tab records every network request the page makes.
  - Use the **Fetch/XHR** filter to show only API calls, hiding unrelated assets like images and stylesheets.
  - Trigger a test call by pasting a `fetch(url)` line into the **Console** tab and pressing Enter -- any valid API URL works; the call then appears in the Network tab's list.
  - Selecting a recorded call and opening its **Headers** tab shows every request and response header involved.
  - **Preview** renders the response body in a formatted, readable style; **Response** shows the same body as raw, unformatted output.
  - **Initiator** points to the exact line of JavaScript that triggered the call, which is useful for tracing a request back to its source.
  - The **Disable cache** checkbox at the top of the panel forces every request to skip the browser cache, guaranteeing a fresh response instead of a cached one.
  - The **Clear** button next to the record button removes all currently recorded calls at any time.

```bash
# Run a local httpbin instance in Docker to test API calls
docker run -p 8081:80 kennethreitz/httpbin
```

- JSON responses viewed directly in the browser -- e.g. the local httpbin instance at `http://localhost:8081/get` -- render as unformatted, hard-to-read text by default.
  - Installing a JSON formatter extension (available in every major browser's extension store) automatically pretty-prints JSON responses when visiting an API endpoint directly in the browser.

```javascript
// Paste into the DevTools Console to trigger a GET call visible in the Network tab
fetch('http://localhost:8081/get');
```

#### Mock APIs

- A mock API imitates a real API endpoint with fake data, letting client application developers start building against it before the real API exists.
  - The data structure is correct, but values are fake and no business logic runs -- the endpoint just returns a pre-generated, hard-coded response.
- Benefits:
  - Both API and client developers can immediately see what data an endpoint returns, without waiting for the real implementation.
  - Client developers code against the mock's data shape right away instead of blocking on the API developers.
  - Once the real API is ready, client developers swap the mock endpoints for the real ones -- easier to build and maintain throughout development.
- Creating a mock API takes two steps:
  1. Create the mock data.
  2. Create mock API endpoints that serve it.
- Free tools (search "Mock API Data Generator" / "Mock API Endpoints" for more):
  - [**Mockaroo**](https://www.mockaroo.com) -- fake-data generator.
  - [**Mockapi**](https://mockapi.io/) -- mock API endpoint hosting.


## 2. Django REST Framework

### Introduction to Django REST Framework (DRF)

#### What Is the Django REST Framework (DRF)?

- DRF (Django REST Framework) is a toolkit built on top of Django that speeds up API development.
  - It bridges the regular Django app, the Django web framework, and the ORM (Object Relational Mapping) library that talks to the database.
  - Django's built-in templating system suits web pages, but APIs need to exchange other data types like JSON and XML, which is where DRF adds value.
- Integrating DRF into an existing Django app is straightforward: a few settings changes give a fully functional DRF-powered app almost instantly.
- Serialization and deserialization are core DRF benefits.
  - Serialization converts database models and other non-ORM objects into native Python datatypes, ready to render as JSON, XML, or other content types, so you don't hand-write the model-to-API transformation.
  - Deserialization is the reverse: it converts incoming request data back into models and validates user input to prevent data corruption.
  - DRF ships with a number of built-in serializers to help with this conversion.
- Built-in viewset classes make it quick to create a functional CRUD (create, read, update, delete) API, with full support for the necessary HTTP methods out of the box, and can still be extended for custom workflows.
- DRF provides its own request and response objects, wrapping the regular Django HTTP request/response but offering more flexibility for processing data in and out.
- The `status` module gives human-readable HTTP status codes (e.g. `status.HTTP_200_OK`, `status.HTTP_404_NOT_FOUND`), so responses don't need raw numeric codes like `200` or `404`.
- DRF includes a browsable API viewer for sending different HTTP methods with data and inspecting the output without an external tool like Insomnia; it's limited in features but useful for quick experimentation.
- DRF also has strong support for modern API authentication, including social authentication, letting users authenticate and authorize through an external provider like Facebook to consume the API, without building that layer from scratch.

```python
from rest_framework import status
from rest_framework.response import Response

# Human-readable status codes instead of raw numbers (200, 404, ...)
return Response(data, status=status.HTTP_200_OK)
return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
```

#### Installing and Setting Up DRF

- Choosing a Python package/environment manager affects setup effort.
  - Plain pip requires manually managing dependencies and setting up/configuring the virtual environment.
  - [uv](https://docs.astral.sh/uv/) is a fast all-in-one package and project manager: it creates and manages the virtual environment automatically (in `.venv`), tracks dependencies in `pyproject.toml`/`uv.lock`, and runs commands inside that environment with `uv run`, so there is far less manual configuration.
- Project setup steps, run from the terminal:
  - `uv init BookList` to scaffold the project (creates `pyproject.toml`), then `cd BookList`.
  - `uv add django djangorestframework` to add DRF (Django REST Framework) and Django as dependencies; this creates the virtual environment and installs both packages automatically.
  - `uv run django-admin startproject BookList .` to create the Django project, then `uv run python manage.py startapp BookListAPI` to create the app.
- Configuring DRF only requires adding `"rest_framework"` to `INSTALLED_APPS` in `settings.py`; the new `BookListAPI` app must be added to the same list.
- Creating an endpoint (e.g. `/books`) means: write a view in `BookListAPI/views.py` using DRF's `Response` class (an improved version of the plain Django `HttpResponse`) wrapped with the `@api_view` decorator, which is what lets the view work with `Request`/`Response` objects.
- Routing the endpoint: define it in a new `BookListAPI/urls.py`, then include that file from the project's root `urls.py` via `include()` from `django.urls`, so it's reachable under a URL prefix like `/api/`.
- Running `uv run python manage.py runserver` exposes the endpoint, e.g. at `http://127.0.0.1:8000/api/books`, which can be tested with a tool like Insomnia.
  - A GET request returns the list of books.
  - A POST request is rejected ("method not allowed") by default, because `@api_view` only accepts GET unless told otherwise.
  - Passing the allowed methods explicitly, e.g. `@api_view(['GET', 'POST'])`, makes DRF accept POST too; the same applies for PUT and DELETE.

```bash
cd .../path/to/my/project
uv init BookList
cd BookList
uv add django djangorestframework
uv run django-admin startproject BookList .
uv run python manage.py startapp BookListAPI

# To get the env shell
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

```python
# settings.py
INSTALLED_APPS = [
    # ...
    "rest_framework",
    "BookListAPI",
]

# BookListAPI/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view()
def books(request):
    return Response(["Book 1", "Book 2"], status=status.HTTP_200_OK)

# BookListAPI/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.books),
]

# BookList/urls.py (project root)
from django.urls import include, path

urlpatterns = [
    # ...
    path("api/", include("BookListAPI.urls")),
]
```

```bash
uv run python manage.py runserver 8080
# API available at http://127.0.0.1:8080/api/books/
# Test with Insomnia or curl
```

#### Better API View with Decorators

- The `@api_view` decorator (from `rest_framework.decorators`) is what makes a plain function usable as a DRF (Django REST Framework) view, and it brings several benefits over a regular Django function-based view.
- Returning DRF's `Response` (from `rest_framework.response`) instead of Django's plain `HttpResponse` is what unlocks the browsable API: with `HttpResponse` the `/api/books` endpoint just renders plain text, but with `Response` under `@api_view` it renders as a polished, browsable HTML interface.
- The decorator lets a view support multiple HTTP methods by passing them as a list, e.g. `@api_view(['GET', 'POST'])`; POST data arrives via `request.data`.
  - Once POST is allowed, the browsable API page shows POST in its list of allowed methods and adds a form at the bottom of the page for submitting a JSON body directly from the browser, no external tool like Postman or Insomnia needed.
  - The page's OPTIONS button shows metadata about the endpoint, such as which renderers it uses and what data it accepts; a GET button/refresh reloads the page, and a format dropdown (e.g. `json`) lets you view the raw response instead of the rendered page.
- Additional per-view policy decorators build on `@api_view`, placed below it:
  - `@throttle_classes` applies throttling/rate-limiting, capping how many requests a client can make in a given period.
  - `@authentication_classes` and `@permission_classes` restrict the endpoint so only authenticated (and authorized) users can call it.

```python
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    throttle_classes,
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response

@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def books(request):
    if request.method == "POST":
        return Response({"message": "Book added", "data": request.data})
    return Response(["Book 1", "Book 2"])
```

#### Different Types of Routing in DRF

- DRF (Django REST Framework) supports several ways to do URL mapping/routing in an API project, beyond the traditional style, to save development time.
- All routing is done in the `urls.py` file of the Django app.

##### Regular routes

- Maps a single function from `views.py` to an endpoint; requires importing `path` from `django.urls`.
- The `@api_view` decorator controls which HTTP methods the function view accepts, e.g. `@api_view(['GET', 'POST'])` for both GET and POST.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books),  # maps `books` to /api/books
]
```

##### Routing to a class method

- Map a single method of a class by declaring it `@staticmethod` first, then referencing it as `views.ClassName.method_name` in `urls.py`.

```python
class Orders():
    @staticmethod
    @api_view()
    def listOrders(request):
        return Response({'message': 'list of orders'}, 200)
```

```python
from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.Orders.listOrders)
]
```

##### Routing class-based views

- Classes that extend `APIView` (or a generic view) have HTTP-verb-specific methods (`get`, `put`, `post`, `delete`, `patch`), so the whole class is mapped once instead of mapping each method individually.
- Whichever of those methods the class defines determines which HTTP verbs the endpoint accepts.

```python
class BookView(APIView):
    def get(self, request, pk):
        return Response({"message": "single book with id " + str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({"title": request.data.get('title')}, status.HTTP_200_OK)
```

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:pk>', views.BookView.as_view())
]
```

- Result: `/api/books/{bookId}` now accepts GET and PUT (and would accept POST/DELETE/PATCH too, if those methods were defined).

##### Routing classes that extend viewsets

- Classes extending `viewsets.ViewSet` expose their own set of methods (`list`, `create`, `retrieve`, `update`, `partial_update`, `destroy`) instead of HTTP-verb method names.
  - `list()` returns all items; `retrieve()` returns a single item.

```python
class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "All books"}, status.HTTP_200_OK)

    def create(self, request):
        return Response({"message": "Creating a book"}, status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        return Response({"message": "Updating a book"}, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({"message": "Displaying a book"}, status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response({"message": "Partially updating a book"}, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({"message": "Deleting a book"}, status.HTTP_200_OK)
```

- Each viewset method must be explicitly mapped to an HTTP verb per route, unlike `APIView`.

```python
urlpatterns = [
    path('books', views.BookView.as_view(
        {
            'get': 'list',
            'post': 'create',
        })
    ),
    path('books/<int:pk>', views.BookView.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        })
    )
]
```

- Result: `/api/books` accepts GET and POST; `/api/books/1` accepts GET, PUT, PATCH, and DELETE.

##### Routing with the SimpleRouter class in DRF

- For a `ViewSet` class, a built-in router auto-generates the verb-to-method mapping, avoiding the manual `as_view({...})` mapping from the previous section.
- `trailing_slash=False` is needed to avoid a trailing slash on the generated endpoints (the default adds one).

```python
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```

- Result: same `api/books` and `api/books/1` endpoints/methods as the manual mapping above.

##### Routing with the DefaultRouter class in DRF

- `DefaultRouter` works like `SimpleRouter` but additionally creates an API root view listing all available endpoints, reachable at `http://127.0.0.1:8000/api/`.

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```

![API root view with all the available endpoints](./assets/root-view-api-drf.png)

#### Generic Views and ViewSets in DRF

- DRF (Django REST Framework) ships generic views and ViewSets to scaffold a functioning CRUD (create, read, update, delete) API without starting from scratch, cutting down boilerplate.
- All the examples below share one model and serializer:

  ```python
  # models.py
  from django.db import models

  class MenuItem(models.Model):
      title = models.CharField(max_length=255)
      price = models.DecimalField(max_digits=6, decimal_places=2)
      inventory = models.PositiveSmallIntegerField()
  ```

  ```python
  # serializers.py
  from rest_framework import serializers
  from .models import MenuItem

  class MenuItemSerializer(serializers.ModelSerializer):
      class Meta:
          model = MenuItem
          fields = ['id', 'title', 'price', 'inventory']
  ```

##### ViewSets

- ViewSets are class-based views with a method-naming convention that enables one-line routing; import via `from rest_framework import viewsets`.
- `ViewSet` is the base class (extends `APIView`), giving browsable API views out of the box. You write the business logic yourself:

  | Class method | Supported HTTP method | Purpose |
  |---|---|---|
  | `list()` | GET | Display resource collection |
  | `create()` | POST | Create new resource |
  | `retrieve()` | GET | Display a single resource |
  | `update()` | PUT | Completely replace a single resource |
  | `partial_update()` | PATCH | Partially update a single resource |
  | `destroy()` | DELETE | Delete a single resource |

  ```python
  # views.py
  from rest_framework import viewsets, status
  from rest_framework.response import Response
  from .models import MenuItem
  from .serializers import MenuItemSerializer

  class MenuItemViewSet(viewsets.ViewSet):
      def list(self, request):
          items = MenuItem.objects.all()
          serializer = MenuItemSerializer(items, many=True)
          return Response(serializer.data)

      def retrieve(self, request, pk=None):
          item = MenuItem.objects.get(pk=pk)
          serializer = MenuItemSerializer(item)
          return Response(serializer.data)

      def create(self, request):
          serializer = MenuItemSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```

  - Notice `list()`, `retrieve()`, and `create()` all convert model instances to/from JSON by hand with `MenuItemSerializer` -- that manual work is exactly what `ModelViewSet` removes below.

- `ModelViewSet` extends `ViewSet` and automatically handles CRUD operations: just supply a `queryset` and a `serializer_class`, no manual database code needed.

  ```python
  # views.py
  from rest_framework import viewsets
  from .models import MenuItem
  from .serializers import MenuItemSerializer

  class MenuItemView(viewsets.ModelViewSet):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer
  ```

- `ReadOnlyModelViewSet` only supports `list()` and `retrieve()` (GET); no POST, PUT, PATCH, or DELETE.

  ```python
  # views.py
  from rest_framework import viewsets
  from .models import MenuItem
  from .serializers import MenuItemSerializer

  class ReadOnlyMenuItemView(viewsets.ReadOnlyModelViewSet):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer
  ```

- Any of the three ViewSets above is wired up the same way, with a router (see [Routing with the DefaultRouter class in DRF](#different-types-of-routing-in-drf)):

  ```python
  # urls.py
  from rest_framework.routers import DefaultRouter
  from .views import MenuItemView

  router = DefaultRouter(trailing_slash=False)
  router.register('menu-items', MenuItemView, basename='menu-items')
  urlpatterns = router.urls
  ```

  - This exposes `GET`/`POST` on `/menu-items` and `GET`/`PUT`/`PATCH`/`DELETE` on `/menu-items/<pk>`.

##### Generic views

- Generic views are class-based views that each provide one piece of CRUD functionality; import via `from rest_framework import generics`. All of them require a `queryset` and a `serializer_class`.

  | Generic view class | Supported method | Purpose |
  |---|---|---|
  | `CreateAPIView` | POST | Create a new resource |
  | `ListAPIView` | GET | Display resource collection |
  | `RetrieveAPIView` | GET | Display a single resource |
  | `DestroyAPIView` | DELETE | Delete a single resource |
  | `UpdateAPIView` | PUT, PATCH | Replace or partially update a single resource |
  | `ListCreateAPIView` | GET, POST | Display resource collection and create a new resource |
  | `RetrieveUpdateAPIView` | GET, PUT, PATCH | Display a single resource and replace/partially update it |
  | `RetrieveDestroyAPIView` | GET, DELETE | Display a single resource and delete it |
  | `RetrieveUpdateDestroyAPIView` | GET, PUT, PATCH, DELETE | Display, replace/update, and delete a single resource |

- Composite views can be built either by extending multiple single-purpose views or the equivalent combined view; both are equivalent, and -- like `ModelViewSet` -- need only a `queryset` and `serializer_class`:

  ```python
  # views.py
  from rest_framework import generics
  from .models import MenuItem
  from .serializers import MenuItemSerializer

  class MenuItemView(generics.ListAPIView, generics.CreateAPIView):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer

  # equivalent to:
  class MenuItemView(generics.ListCreateAPIView):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer

  # single-resource counterpart, for GET/PUT/PATCH/DELETE on one item:
  class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer
  ```

- Unlike ViewSets, generic views map to URLs individually with `path()`, not through a router:

  ```python
  # urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
      path('menu-items', views.MenuItemView.as_view()),
      path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
  ]
  ```

##### Authentication and selective authentication

- To require authentication for all calls on a generic-view class, set `permission_classes = [IsAuthenticated]`.
- To require it only for some methods (e.g. everything but GET), override `get_permissions()`:

  ```python
  # views.py
  from rest_framework import generics
  from rest_framework.permissions import IsAuthenticated
  from .models import MenuItem
  from .serializers import MenuItemSerializer

  class MenuItemView(generics.ListCreateAPIView):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer

      def get_permissions(self):
          permission_classes = []
          if self.request.method != 'GET':
              permission_classes = [IsAuthenticated]
          return [permission() for permission in permission_classes]
  ```

  - Result: GET is open to everyone; POST, PUT, PATCH, and DELETE require authentication.

##### Return items for the authenticated user only

- This example introduces a second model, owned by a user:

  ```python
  # models.py
  from django.contrib.auth.models import User
  from django.db import models

  class Order(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      total = models.DecimalField(max_digits=6, decimal_places=2)
      date = models.DateField(auto_now_add=True)
  ```

  ```python
  # serializers.py
  from rest_framework import serializers
  from .models import Order

  class OrderSerializer(serializers.ModelSerializer):
      class Meta:
          model = Order
          fields = ['id', 'user', 'total', 'date']
  ```

- Override `get_queryset()` to scope results to `self.request.user`:

  ```python
  # views.py
  class OrderView(generics.ListCreateAPIView):
      queryset = Order.objects.all()
      serializer_class = OrderSerializer
      permission_classes = [IsAuthenticated]

      def get_queryset(self):
          return Order.objects.all().filter(user=self.request.user)
  ```

  - `queryset` is still required as the class attribute DRF introspects for metadata, but every actual request goes through `get_queryset()` instead, so each user only ever sees their own orders.

##### Override default behavior

- Generic views automate CRUD, but any default method (`get()`, `post()`, `put()`, `patch()`, `delete()`) can still be overridden, e.g. to return a static response instead of the resource:

  ```python
  # views.py
  from rest_framework.response import Response

  class OrderView(generics.ListCreateAPIView):
      queryset = Order.objects.all()
      serializer_class = OrderSerializer

      def get(self, request, *args, **kwargs):
          return Response('new response')
  ```

#### Function and Class-Based Views

- Function-based views are plain functions in the views file; class-based views group related logic (and HTTP-verb handlers) into a class. Each style has its own strengths.
  - Function-based views: easy to implement, more readable, and decorators (like `@api_view`) are simpler to apply, making them good for a quick one-off endpoint.
  - Class-based views: less code and duplication overall, classes can be extended to reuse common functionality and add features later, and each HTTP verb gets its own method.
- To create a class-based view in DRF (Django REST Framework), extend `APIView` (from `rest_framework.views`) and import `Response` (from `rest_framework.response`).
  - Name methods after the HTTP verbs they handle, e.g. `get()` and `post()`.
  - Map the whole class to a URL once in `urls.py` with `.as_view()`; there is no need to map each method separately, unlike function-based views.
  - A method only exists on the endpoint if the class defines it: with no `post()`, the endpoint rejects POST requests until one is added.
- Query string parameters (e.g. `/api/books?author=Hemingway`) are read via `request.query_params.get('author')` (the DRF-recommended synonym for `request.GET`, clearer since query parameters can accompany any HTTP method, not just GET).
  - If `author` is present, filter to that author's books; otherwise return all books.
- POST/PUT payloads (JSON or form URL-encoded data sent to the API) are read via `request.data.get('title')`.
  - Because DRF views are browsable, POST/PUT payloads can be tested directly from the browser: open the endpoint, scroll to the bottom, enter the JSON payload in the content box, and click the corresponding method button.
- A separate class (e.g. `Book`) can manipulate a single item by accepting the primary key (`pk`) as an extra parameter on its methods, e.g. `get(self, request, pk)` and `put(self, request, pk)`; this class is mapped to a URL pattern that captures the `pk`, such as `/api/books/<int:pk>`.
- Just like the `@api_view` decorator, class-based views support throttling and authentication policies, covered later in the course.

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book

class BookList(APIView):
    def get(self, request):
        author = request.query_params.get('author')
        books = Book.objects.all()
        if author:
            books = books.filter(author=author)
        return Response([{"title": b.title, "author": b.author} for b in books])

    def post(self, request):
        title = request.data.get('title')
        return Response({"message": f"Received book: {title}"})

class BookDetail(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return Response({"id": book.id, "title": book.title, "author": book.author})

    def put(self, request, pk):
        title = request.data.get('title')
        return Response({"message": f"Updated book {pk} with title: {title}"})
```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BookList.as_view()),
    path('books/<int:pk>', views.BookDetail.as_view()),
]
```

- Calling these endpoints, e.g. with `curl` (the browsable API works the same way from a browser):

```bash
# GET all books
curl http://127.0.0.1:8000/api/books

# GET books filtered by author (query string parameter)
curl "http://127.0.0.1:8000/api/books?author=Hemingway"

# POST a new book (JSON payload)
curl -X POST http://127.0.0.1:8000/api/books \
  -H "Content-Type: application/json" \
  -d '{"title": "The Old Man and the Sea"}'

# GET a single book by primary key (pk)
curl http://127.0.0.1:8000/api/books/1

# PUT to update a single book by primary key
curl -X PUT http://127.0.0.1:8000/api/books/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title"}'
```

#### Django Debug Toolbar

- Django Debug Toolbar is a smart debugging tool considered essential for Django development; it displays live information about the current project setup, request, and database queries.
- Setup steps, run from the project directory:
  - `uv add django-debug-toolbar` to install it into the project's virtual environment.
  - Add `"debug_toolbar"` to `INSTALLED_APPS` in `settings.py`.
  - Add `"debug_toolbar.middleware.DebugToolbarMiddleware"` to `MIDDLEWARE` in `settings.py`, just below `INSTALLED_APPS`.
  - Add an `INTERNAL_IPS` list containing `"127.0.0.1"` to `settings.py`; this setting does not exist there by default, so it must be created.
  - Map the toolbar's URLs in the project's root `urls.py`.
- Visiting any endpoint (e.g. `/api/books`) then shows the toolbar on the right side of the screen.
  - It can be hidden with the "hide" link at the top, and individual sections can be toggled on/off with their checkboxes.
- Key sections of the toolbar:
  - Settings: shows every setting from `settings.py` and other settings used across the project/installed apps; copy a name and value from here to override it in `settings.py`.
  - Headers: shows all header information sent with the request and generated in the response.
  - SQL: lists the SQL queries executed for the endpoint, useful for spotting and fixing unnecessary or excessive queries during performance tuning.
  - Static files: shows the static files loaded for the request and those used by installed apps; APIs don't usually serve static files, but it's worth knowing about.
  - Cache: shows applications using the cache, which reduces server load (covered later in the course).
  - Profiling: unchecked by default; shows the full call stack for the request, from the entry point through intermediate function calls to the class/function-based view and back out to the generated response.
- The toolbar only appears during development when using the browsable API; it does not show up on production API calls or when client apps consume the API directly.

```python
# settings.py
INSTALLED_APPS = [
    # ...
    "debug_toolbar",
]

MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]
```

```python
# urls.py (project root)
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + debug_toolbar_urls()
```

![Debug Toolbar on the right side of the browsable API](./assets/debug_toolbar.png)

#### Restaurant Menu API Project with DRF

- This walkthrough builds a fully functional CRUD (create, read, update, delete) API, "LittleLemonAPI," using generic views, with only a few lines of code.
- Project setup:
  - Create a new app, e.g. `uv run python manage.py startapp LittleLemonAPI`, and add both `"rest_framework"` and the new app to `INSTALLED_APPS` in `settings.py` (DRF, Django REST Framework, won't work without the former).
  - Define the model in `models.py` with the `title`, `price`, and `inventory` fields, then run makemigrations/migrate.
- A serializer converts model instances to Python datatypes for JSON/XML output, and converts an incoming HTTP request body back into a model instance; there are other serializer types, covered later, but a simple `ModelSerializer` is enough here, with every model field listed.
- Views reuse DRF's generic view classes instead of writing CRUD logic from scratch:
  - `MenuItemView` extends `generics.ListCreateAPIView`, which displays the resource collection (GET) and accepts new records (POST); it just needs a `queryset` (all records via the model) and a `serializer_class`.
  - `SingleMenuItemView` extends `generics.RetrieveUpdateDestroyAPIView`, which fetches/displays a single record (GET), updates it (PUT/PATCH), and deletes it (DELETE); it reuses the same `queryset` and `serializer_class` as `MenuItemView`.
- Routing: map `MenuItemView` and `SingleMenuItemView` in a new `urls.py` inside the app, then include that file from the project's root `urls.py` under the `api/` prefix.
- Testing the result:
  - `GET /api/menu-items` initially returns no records.
  - Because `MenuItemView` extends `ListCreateAPIView`, the browsable API page for that endpoint includes a form (title, price, inventory) for POSTing new records; after adding one, `GET /api/menu-items` returns it.
  - `GET /api/menu-items/1` (via `SingleMenuItemView`) displays a single record, with a form to update it and a button to delete it; GET, PUT, PATCH, and DELETE all work against this endpoint without extra code.

```python
# models.py
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
```

```python
# serializers.py
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
```

```python
# views.py
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

```python
# LittleLemonAPI/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]
```

```python
# urls.py (project root)
from django.urls import include, path

urlpatterns = [
    # ...
    path('api/', include('LittleLemonAPI.urls')),
]
```

![Single Menu Item API](./assets/single_menu_item_api.png)

#### Exercise: Book List API with DRF

Folder: [`lab/03-booklist-api-drf/`](./lab/03-booklist-api-drf/), instructions: [`Instructions.md`](./lab/03-booklist-api-drf/Instructions.md).

- Converted the plain-Django BookList project into a DRF (Django REST Framework) API:
  - Defined the `Book` model (`title`, `author`, `price`) in `models.py`.
  - Added `serializers.py` with a `BookSerializer` (`ModelSerializer`) exposing `id`, `title`, `author`, `price`.
  - Added `views.py` with `BookView` (`generics.ListCreateAPIView`, for GET/POST on the collection) and `SingleBookView` (`generics.RetrieveUpdateAPIView`, for GET/PUT on a single book by `pk`), both backed by `Book.objects.all()` and `BookSerializer`.
  - Added the app-level `urls.py` mapping `books` to `BookView` and `books/<int:pk>` to `SingleBookView`.
  - Included the app's `urls.py` from the project-level `urls.py` under the `api/` prefix.
  - Ran migrations and verified the API: added three books through the browsable API's POST form (`The Prophet`, `Siddhartha`, `The Great Gatsby`), confirmed `GET /api/books` lists all of them, and confirmed `GET /api/books/<id>` returns a single book.
- Replaced the project's `Pipfile`/`Pipfile.lock` with a standalone `uv` project (`pyproject.toml`/`uv.lock`), scoped to this lab folder with its own `.venv`, independent of the repo's root-level environment.

Shell commands, run from inside `lab/03-booklist-api-drf/BookList/`:

```bash
# One-time setup: create the project's own virtual environment and install dependencies
uv sync

# Making migrations
uv run python manage.py makemigrations
uv run python manage.py migrate

# Start the dev server
uv run python manage.py runserver 8080
# Browsable API: http://127.0.0.1:8080/api/books
```

Solution code for `models.py`:

```python
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
```

Solution code for `serializers.py`:

```python
from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # ModelSerializer derives the fields and validation from the Book model
    # itself (instead of declaring each field by hand like a plain
    # Serializer would), and it implements create()/update() out of the
    # box, converting between Book instances and JSON automatically.
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']
```

Solution code for `views.py`:

```python
from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class BookView(generics.ListCreateAPIView):
    # ListCreateAPIView bundles "list all" (GET) and "create" (POST) for a
    # collection endpoint, so /books supports both without writing get()/
    # post() by hand -- chosen because the collection only ever needs to
    # be listed and appended to, never updated or deleted as a whole.
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView):
    # RetrieveUpdateAPIView bundles "fetch one" (GET) and "update" (PUT/
    # PATCH) for a single resource, matching the /books/<pk> endpoint --
    # DestroyAPIView is deliberately left out of the inheritance here, so
    # this endpoint does not support DELETE.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

Solution code for `urls.py` (app-level):

```python
from django.urls import path

from . import views

urlpatterns = [
    path('books', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view(), name='SingleBook'),
]
```

Solution code for `urls.py` (project-level):

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BookListDRF.urls')),
]
```

![Browsable API](./assets/booklist_api_drf_result.png)

![Database Contents](./assets/booklist_db_result.png)

#### Additional Resources

- [Django rest framework toolkit for building web APIs](https://www.django-rest-framework.org/)
- [Django debug toolbar documentation](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [Django Debug toolbar source code](https://github.com/jazzband/django-debug-toolbar)
- [DRF router documentation](https://www.django-rest-framework.org/api-guide/routers/)


### Django REST Framework Essentials

#### Serializers

- Serializers are DRF (Django REST Framework)'s tool for data conversion, its most popular feature: they turn Django model instances/querysets into a readable format like JSON or XML, and do the reverse (deserialization) by parsing incoming JSON and mapping it onto a model, validating the data along the way to keep it clean and consistent.
- Without a serializer, a view that returns a queryset directly has DRF auto-convert every field of the model, including any sensitive ones; a serializer is what lets you choose (and hide) fields.
- Practical setup, using a `MenuItem` model with `title`, `price`, and `inventory` fields:
  - Create a `serializers.py` file in the Django app to hold all serializer code.
  - Declare a `Serializer` subclass with one field per model field to expose; only the fields listed here appear in the API output, e.g. omitting `price`/`inventory` hides them.
  - A view returning multiple records must pass `many=True` when instantiating the serializer, since converting a list/queryset differs from converting a single object; a single-record view omits `many=True`.
- Fetching a single record by primary key with the plain `Model.objects.get(pk=...)` throws a server error (HTTP 500) for a non-existent ID; using Django's `get_object_or_404()` shortcut instead raises `Http404`, which DRF automatically turns into a proper JSON 404 response (`{"detail": "Not found."}`).

```python
# serializers.py
from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    # We can comment out these following fields, if desired
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory = serializers.IntegerField()
```

```python
# views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view()
def single_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)
```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-items/<int:pk>', views.single_item),
]
```

#### Model Serializers

- `ModelSerializer` is an easier way to convert Django model instances to JSON than the plain `Serializer` from the previous section: less code, same result.
  - Swapping a plain `Serializer` for a `ModelSerializer` (for the same `MenuItem` model with `title`, `price`, and `inventory` fields) requires no changes to `views.py` -- both the collection and single-item endpoints keep working as before.
- Renaming an output field: declare a new field on the serializer with the desired name and point it at the original model field via the `source` argument (e.g. exposing `inventory` as `stock`), then list the new field name -- not the original -- in `Meta.fields`, or it raises an error.
- Adding a calculated field (not backed directly by a model field): declare a `SerializerMethodField`, then define a `get_<field_name>` method that computes and returns its value from the model instance; that field name must also be added to `Meta.fields`.
  - Example: a `price_after_tax` field computed as the product's price plus 10% tax, using `Decimal` from Python's `decimal` module for the arithmetic.

```python
# serializers.py
from decimal import Decimal

from rest_framework import serializers

from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax']

    def get_price_after_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
```

#### Relationship Serializers

- Real projects usually have related data across multiple tables, connected through model fields; DRF (Django REST Framework) needs specific handling to convert these related models to JSON correctly.
- Setup: a new `Category` model is connected to `MenuItem` via a foreign key, with `on_delete=models.PROTECT` so a category cannot be deleted while menu items still reference it. Migrations must be created and applied before continuing.
- By default, a related field doesn't appear in the API output at all unless it's explicitly added to the serializer's `Meta.fields` -- once added, it shows the raw foreign key ID, not anything more descriptive.
- Displaying the category's name instead of its ID:
  - Adding a `StringRelatedField` for `category` relies on the related model's `__str__` method to produce the value, so `Category` needs a `__str__` method defined; without it, the field's output doesn't change.
  - This still runs one extra SQL query per menu item to fetch the related category -- inefficient for a list of many items.
- Fixing that N+1 query problem: add `select_related('category')` to the view's queryset, so Django fetches the related categories in the same SQL query instead of a separate one per row.
- Showing the full category object (not just its name): declare a separate `CategorySerializer` and nest it as the `category` field on `MenuItemSerializer`, replacing the `StringRelatedField`; this embeds the category's own fields (e.g. `id`, `title`) under each menu item.

```python
# models.py
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
```

```python
# serializers.py
from rest_framework import serializers

from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'category']
```

```python
# views.py
from rest_framework import generics

from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
```

#### Other Types of Serializers in DRF

##### Nested Fields

Visiting the `menu-items` endpoint can show `category` as a nested object with its `id`, `title`, and `slug`, in two ways:

![Menu-items endpoint displaying the category with a nested field with id, title and slug](./assets/other-types-of-serializers-1.png)

- **Method 1 -- explicit nested serializer:** declare a `CategorySerializer` and set it as the `category` field on `MenuItemSerializer` (as in the previous section).
- **Method 2 -- `depth` option:** instead of nesting a serializer field, set `depth = 1` on `MenuItemSerializer`'s `Meta` class; DRF then expands every relationship on that serializer to show all of the related model's fields, with no other code changes. The API output is identical to Method 1.

```python
# Method 1: serializers.py
from decimal import Decimal
from rest_framework import serializers

from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
```

```python
# Method 2: serializers.py
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = CategorySerializer()  -- no longer needed

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']
        depth = 1

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
```

Nesting related fields this way gives clients more information per response and saves them a separate API call to fetch each related object's details.

##### Displaying a Related Field as a Hyperlink

A related field can also be rendered as a hyperlink, e.g. `http://127.0.0.1:8000/api/category/{categoryId}` for `category`, via `HyperlinkedRelatedField` or `HyperlinkedModelSerializer`.

**Method 1: `HyperlinkedRelatedField`**

- Step 1 -- add a detail view and URL for the related model, so the hyperlink has somewhere to resolve to:

  ```python
  # views.py
  from django.shortcuts import get_object_or_404
  from rest_framework.decorators import api_view
  from rest_framework.response import Response

  from .models import Category
  from .serializers import CategorySerializer

  @api_view()
  def category_detail(request, pk):
      category = get_object_or_404(Category, pk=pk)
      serialized_category = CategorySerializer(category)
      return Response(serialized_category.data)
  ```

  ```python
  # urls.py
  path('category/<int:pk>', views.category_detail, name='category-detail')
  ```

  > Convention: the view name must be `<related-field-name>-detail` -- `category-detail` for the `category` field, `user-detail` for a `user` field, and so on.

- Step 2 -- set `category` to a `HyperlinkedRelatedField`, giving it a `queryset` (to resolve the related object) and a `view_name` (to build the URL); `view_name` can be omitted if the convention from Step 1 was followed:

  ```python
  # serializers.py
  from .models import Category

  class MenuItemSerializer(serializers.ModelSerializer):
      stock = serializers.IntegerField(source='inventory')
      price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
      category = serializers.HyperlinkedRelatedField(
          queryset=Category.objects.all(),
          view_name='category-detail'
      )

      class Meta:
          model = MenuItem
          fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

      def calculate_tax(self, product: MenuItem):
          return product.price * Decimal('1.1')
  ```

- Step 3 -- pass the request into the serializer's context, which DRF needs to build absolute hyperlinks:

  ```python
  serialized_item = MenuItemSerializer(items, many=True, context={'request': request})
  ```

  ![Menu-items endpoint displays the category field as a hyperlink](./assets/other-types-of-serializers-2.png)

  ![Category details that display after clicking on hyperlink](./assets/other-types-of-serializers-3.png)

**Method 2: `HyperlinkedModelSerializer`**

- Simpler alternative: make `MenuItemSerializer` extend `serializers.HyperlinkedModelSerializer` instead of `serializers.ModelSerializer`. Output is identical to Method 1, with less code.
- The `category-detail` URL pattern from Step 1 is still required.

```python
# serializers.py
class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
```

```python
# urls.py
urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-items/<int:id>', views.single_item),
    path('category/<int:pk>', views.category_detail, name='category-detail'),
]
```

#### Deserialization and Validation

- Deserialization reverses serialization: it happens when a client sends data to an API endpoint and DRF maps that data onto an existing model.
- Adding POST support to an existing GET-only view, continuing with the Little Lemon project's `menu_items` function:
  - Add `'POST'` to the `@api_view()` decorator's method list, alongside `'GET'`.
  - Branch on `request.method` inside the function: keep the existing GET logic, and add a branch for POST.
- Deserializing and validating the POST payload, inside the POST branch:
  - Instantiate the serializer with the incoming payload: `MenuItemSerializer(data=request.data)`.
  - Call `serializer.is_valid()` to run the serializer's built-in validation; it checks that every required field (per `Meta.fields`) is present, and raises an error describing what's missing or invalid, so the client can correct and resubmit.
  - Once valid, either:
    - read the validated payload without persisting it, via `serializer.validated_data`, or
    - persist it with `serializer.save()`.
  - After `save()`, `serializer.data` reflects the saved record, including its new `id`; accessing `.data` before `save()` raises an error -- use `.validated_data` if the payload is needed before saving.
- Handling the `category` field on POST, once GET and POST both use the same `MenuItemSerializer`:
  - A first POST attempt fails with "category field is required", because `category` is nested via `CategorySerializer()`, which by default expects input too.
  - Since `category` should only ever be used for output (showing category details on GET), mark it `read_only=True` on `MenuItemSerializer` rather than removing it -- removing it would also hide it from GET responses.
  - After that fix, POST succeeds, but every new record ends up saved with whatever `category` the model's default applies, since `category` is no longer accepted as input.
- Letting POST choose the category, so a client isn't stuck with a hardcoded default:
  - Add a `category_id` field to `MenuItemSerializer` and list it in `Meta.fields`, so POST can set the category directly (see code comments below for why a plain `IntegerField` is enough).
  - Mark it `write_only=True`: otherwise GET responses would show both `category` (the nested object) and `category_id` (the same id, duplicated) -- redundant, since the id already appears inside `category`.

![GET /api/menu-items response after the fix, showing POST and GET as allowed methods and category nested read-only in each item](./assets/deserialization_validation.png)

- Tip: rather than stretching one serializer to cover every GET/POST shape, it's often cleaner to define separate serializers per use case and select the one that fits each view.

```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data)
```

```python
# serializers.py
from decimal import Decimal

from rest_framework import serializers

from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    # No source= needed: Django stores a FK's raw id as `<field>_id` on the model
    # (MenuItem.category_id), so this field lines up with it directly.
    # Looser than PrimaryKeyRelatedField(queryset=...): an id for a category that
    # doesn't exist fails at save() with a database error, not a clean is_valid() one.
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
```

#### Renderers

- Renderers control the format an API's output is displayed in; DRF ships two built in:
  - `JSONRenderer`
  - and `BrowsableAPIRenderer` (the interactive HTML view used throughout this course) -- and supports third-party ones for anything else (XML, YAML, JSONP, ...).
- The active renderer list lives in `settings.py` under `REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES']`; adding, removing, or commenting out an entry changes what the API can output, with no view code changes needed.
- A client picks the output format by sending an `Accept` request header (e.g. `application/json`, `text/html` (browsable API), `application/xml`); if no `Accept` header is sent, DRF falls back to the first renderer in the list.
  - Browsers send `text/html` by default, which is why visiting an endpoint in a browser shows the browsable API instead of raw JSON.
  - Tools like Insomnia send no `Accept` header unless one is added explicitly, so they get plain JSON until `Accept: text/html` (or the desired type) is set.

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # comment out to force JSON-only output
        'rest_framework_xml.renderers.XMLRenderer',  # third party: uv add djangorestframework-xml
    ],
}
```

```text
# Accept header sent by the client -> renderer DRF uses (given the classes above)
application/json  -> JSONRenderer (plain JSON)
text/html -> BrowsableAPIRenderer (only while it's enabled in the list above)
application/xml -> XMLRenderer (requires djangorestframework-xml installed + listed)
(no Accept header) -> first renderer in the list, JSONRenderer
```

#### Different Types of Renderers

Beyond the built-in `JSONRenderer`/`BrowsableAPIRenderer` and the third-party `XMLRenderer` covered earlier, DRF (Django REST Framework) supports several other renderers worth knowing.

##### TemplateHTMLRenderer

For endpoints that need to render actual HTML (e.g. an invoice page), `TemplateHTMLRenderer` passes the serialized data into an HTML template rendered with Django's own templating language (DTL, Django Templating Language).

```python
# views.py
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view()
@renderer_classes([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    # `data` becomes the template context; template_name is looked up under
    # <app>/templates/, e.g. LittleLemonAPI/templates/menu-items.html
    return Response({'data': serialized_item.data}, template_name='menu-items.html')
```

```html
<!-- LittleLemonAPI/templates/menu-items.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Menu Items</title>
</head>
<body>
    <table width="100%" style="text-align: left;">
        <tr>
            <th>Item</th>
            <th>Price</th>
            <th>Price After Tax</th>
            <th>Stock</th>
        </tr>
        {% for item in data %}
        <tr>
            <td>{{ item.title }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.price_after_tax }}</td>
            <td>{{ item.stock }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

```python
# settings.py -- fixes a "TemplateDoesNotExist" error if Django can't find the templates directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # add this line
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
# Or, if TEMPLATES is already defined and only DIRS is missing:
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']
```

```python
# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-items/<int:id>', views.single_item),
    path('menu', views.menu),  # -> http://127.0.0.1:8000/api/menu
]
```

![Menu-items endpoint displays menu items in formatted HTML table](./assets/different-types-of-renderers-1.png)

##### StaticHTMLRenderer

For endpoints that just need to return a fixed HTML string, with no template or DTL involved.

```python
# views.py
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response

@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
    return Response(data)
```

```python
# urls.py
path('welcome', views.welcome)  # -> http://127.0.0.1:8000/api/welcome
```

![Welcome to the Little Lemon API Project greeting](./assets/different-types-of-renderers-2.png)

##### CSV Renderer

CSV (comma-separated values) puts one record per line with fields comma-separated. DRF has no built-in CSV renderer, so it needs a third-party package.

```bash
pipenv install djangorestframework-csv
uv add djangorestframework-csv
```

```python
# views.py -- add directly below @api_view() on the existing menu_items view
from rest_framework_csv.renderers import CSVRenderer

@api_view()
@renderer_classes([CSVRenderer])
def menu_items(request):
    ...
```

Visiting `http://127.0.0.1:8000/api/menu-items` in a REST client like Insomnia now returns CSV:

![API endpoint output in Insomnia](./assets/different-types-of-renderers-3.png)

##### YAML Renderer

Same pattern as CSV, for YAML output.

```bash
pipenv install djangorestframework-yaml
uv add djangorestframework-yaml
```

```python
# views.py -- add directly below @api_view() on the existing menu_items view
from rest_framework_yaml.renderers import YAMLRenderer

@api_view()
@renderer_classes([YAMLRenderer])
def menu_items(request):
    ...
```

![API endpoint output in Insomnia that displays the menu items](./assets/different-types-of-renderers-4.png)

##### Global Settings

Instead of importing and decorating each view individually, register renderers globally in `settings.py` so any endpoint can serve them based on the client's `Accept` header.

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
        'rest_framework_yaml.renderers.YAMLRenderer',
    ]
}
```

```text
# Client Accept header -> response format, once the renderers above are registered globally
Accept: text/csv         -> CSV
Accept: application/yaml -> YAML
```

#### Exercise: Restaurant Menu API with Serialization

Folder: [`lab/04-menuitem-api-serialization/`](./lab/04-menuitem-api-serialization/).

- Defined the `MenuItem` model (`title`, `price`, `inventory`) and ran `makemigrations`/`migrate` to create its table.
- Added `serializers.py` with a `MenuItemSerializer(ModelSerializer)`; used `extra_kwargs` to enforce `price >= 2` and `inventory >= 0` at validation time, without writing a custom `validate_*` method.
- Wired up `views.py` with two generic views sharing the same queryset/serializer:
  - `MenuItemsView(ListCreateAPIView)` for `GET` (list) and `POST` (create) on `/api/menu-items`.
  - `SingleMenuItemView(RetrieveUpdateDestroyAPIView)` for `GET`/`PUT`/`DELETE` on `/api/menu-items/<pk>`.
- Uncommented the two routes in the app-level `urls.py` to expose both views.
- Registered `XMLRenderer` (from `djangorestframework-xml`) alongside the default JSON and browsable-API renderers in `settings.py`, so `?format=xml` / `?format=json` both work.
- Replaced the project's `Pipfile`/`Pipfile.lock` with a standalone `uv` project (`pyproject.toml`/`uv.lock`), scoped to this lab folder with its own `.venv`, independent of the repo's root-level environment.
- Ran the flow end-to-end against the dev server to confirm each piece: `POST` a valid item (succeeds), `POST` an out-of-range item such as `inventory: -1` (rejected with a 400 and the `extra_kwargs` error messages), `GET` the list and a single item, `PUT` an update, `DELETE` an item, and `GET /api/menu-items?format=xml` vs `?format=json`.

Shell commands, run from inside `lab/04-menuitem-api-serialization/LittleLemon/`:

```bash
# One-time setup: create the project's own virtual environment and install dependencies
uv sync

# Create and apply the migration for the new MenuItem model
uv run python manage.py makemigrations
uv run python manage.py migrate

# Start the dev server
uv run python manage.py runserver 8080
# Browsable API: http://127.0.0.1:8080/api/menu-items
```

`models.py`:

```python
from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
```

`urls.py` (app-level):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]
```

`views.py`:

```python
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# GET (list) + POST (create) on /api/menu-items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# GET + PUT + DELETE on /api/menu-items/<pk>
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

`serializers.py`:

```python
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        # Field-level validation without custom validate_<field> methods:
        # POSTing/PUTing a value outside these bounds returns a 400 with an
        # explanatory error message for that field.
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory': {'min_value': 0}
        }
```

`settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',  # dependency: djangorestframework-xml (see pyproject.toml)
    ]
}
```

Testing the API with `curl` (the browsable API's HTML forms work the same way from a browser):

```bash
# GET -- empty collection initially
curl http://127.0.0.1:8080/api/menu-items
# []

# POST -- create a menu item
curl -X POST http://127.0.0.1:8080/api/menu-items \
  -H "Content-Type: application/json" \
  -d '{"title": "Grilled Fish", "price": "8.50", "inventory": 20}'
# {"id":1,"title":"Grilled Fish","price":"8.50","inventory":20} -- 201 Created

# GET -- new item now listed
curl http://127.0.0.1:8080/api/menu-items
# [{"id":1,"title":"Grilled Fish","price":"8.50","inventory":20}]

# POST -- inventory below the extra_kwargs min_value -> 400
curl -X POST http://127.0.0.1:8080/api/menu-items \
  -H "Content-Type: application/json" \
  -d '{"title": "Lemon Dessert", "price": "1.50", "inventory": -1}'
# {"price":["Ensure this value is greater than or equal to 2."],
#  "inventory":["Ensure this value is greater than or equal to 0."]}

# GET a single item by pk
curl http://127.0.0.1:8080/api/menu-items/1
# {"id":1,"title":"Grilled Fish","price":"8.50","inventory":20}

# PUT -- update the item
curl -X PUT http://127.0.0.1:8080/api/menu-items/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Grilled Fish", "price": "9.00", "inventory": 15}'
# {"id":1,"title":"Grilled Fish","price":"9.00","inventory":15}

# DELETE the item
curl -X DELETE http://127.0.0.1:8080/api/menu-items/1
# 204 No Content

# GET the same collection rendered as XML vs. JSON
curl "http://127.0.0.1:8080/api/menu-items?format=xml"
# <?xml version="1.0" encoding="utf-8"?><root><list-item>...</list-item></root>
curl "http://127.0.0.1:8080/api/menu-items?format=json"
# [{"id": ...}]
```

#### Additional Resources

- [XML renderer, XML support for Django REST framework](https://jpadilla.github.io/django-rest-framework-xml/)
- [YAML renderer, YAML support for Django REST framework](https://jpadilla.github.io/django-rest-framework-yaml/)
- [JSONP renderer, JSONP support for Django REST framework](https://jpadilla.github.io/django-rest-framework-jsonp/)

## 3. Advanced API Development

### Filtering, Ordering, Searching

#### Filtering and Searching

- Filtering lets a client request a subset of an API's results (e.g. only the appetizers category, only items priced $7-$15, only titles containing "pizza") based on query-string criteria, instead of the endpoint always returning the full collection.
- Two ways to support this:
  - Return everything and let the client filter locally: quick to build, but doesn't scale -- pulling thousands or millions of records out of the database and over the network just to keep a handful is wasteful and slow.
  - Filter server-side based on query parameters: more work to build, but keeps the load off the server and the response small, and client applications don't need their own filtering logic.
- Filtering the `menu_items` view by category and price, using DRF's `request.query_params` (works like `request.GET`, but is available consistently across HTTP methods):
  - `?category=<title>` -- `category` is a foreign key on `MenuItem`, so filtering on the related model's `title` field needs a double underscore to cross the relationship: `items.filter(category__title=category_name)`.
  - `?to_price=<value>` -- despite the name, this filters for an exact match on `price` (`items.filter(price=to_price)`), not a "less than or equal to" range -- a *field lookup* like `price__lte=to_price` would be needed for that instead.
  - Both filters can be combined in one request by joining query parameters with `&`, e.g. `?category=main&to_price=15`.
- Filtering by a `search` query parameter: `title__contains=search` matches the search text anywhere in the title, case-sensitively.
  - Other field lookups work the same way for different match rules: `startswith` anchors the match to the start of the title, and `icontains`/`istartswith` are the case-insensitive versions of `contains`/`startswith`.
- Field lookups act as Django's comparison operators for filtering; the full list is in Django's field lookups documentation, linked in this lesson's Additional Resources.

```python
# views.py
from rest_framework import status

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()

        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')

        if category_name:
            items = items.filter(category__title=category_name)  # e.g. ?category=main
        if to_price:
            items = items.filter(price=to_price)  # e.g. ?to_price=15 -> price == 15
        if search:
            items = items.filter(title__contains=search)  # e.g. ?search=Choc (case-sensitive)

        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)
```

Example requests against the filtered/searched endpoint:

```text
# All items in the "main" category
http://127.0.0.1:8000/api/menu-items?category=main

# Items priced exactly 15
http://127.0.0.1:8000/api/menu-items?to_price=15

# Both filters combined
http://127.0.0.1:8000/api/menu-items?category=main&to_price=15

# Titles containing "Choc" (case-sensitive, e.g. matches "Chocolate Cake" but not "chocolate cake")
http://127.0.0.1:8000/api/menu-items?search=Choc
```

#### Ordering

- Ordering (sorting) a query set by a query-string parameter, using Django's own `order_by()` rather than a third-party package: `django-filters` offers more advanced filtering/sorting/searching, but is built mainly for class-based views; since `menu_items` is a function-based view (via `@api_view`), Django's native ordering support is enough with just a few lines.
- Single-field ordering: read `?ordering=<field>` and pass it straight to `items.order_by(ordering)`, added just before the items are serialized.
  - `?ordering=price` sorts ascending (lowest price first).
  - `?ordering=-price` sorts descending -- `order_by()` treats a leading `-` on a field name as "descending" on that field, so no extra code is needed to support it.
- Multi-field ordering: `?ordering=price,inventory` should sort by `price` first and use `inventory` as a tiebreaker, both ascending. `order_by()` already accepts multiple field arguments (no loop needed), so it's enough to split the `ordering` string on commas and unpack the resulting list into `order_by()`.
  - The same leading `-` convention applies per field, so `?ordering=price,-inventory` sorts by `price` ascending, then by `inventory` descending for ties.

```python
# views.py
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()  
        # ...
        ordering = request.query_params.get('ordering')
        if ordering:
            ordering_fields = ordering.split(',')  # e.g. "price,-inventory" -> ['price', '-inventory']
            items = items.order_by(*ordering_fields)

        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
# ...
```

Example requests against the ordered endpoint:

```text
# Ascending by price (cheapest first)
http://127.0.0.1:8000/api/menu-items?ordering=price

# Descending by price (most expensive first)
http://127.0.0.1:8000/api/menu-items?ordering=-price

# Price ascending, inventory ascending as a tiebreaker
http://127.0.0.1:8000/api/menu-items?ordering=price,inventory

# Price ascending, inventory descending as a tiebreaker
http://127.0.0.1:8000/api/menu-items?ordering=price,-inventory
```

#### Importance of Data Validation

Validation checks that user-submitted data is well-formed, meets requirements, and is safe to persist. Serializers in DRF (Django REST Framework) provide several built-in techniques for it. A few example rules for the Little Lemon menu items, before getting into the code:

| Field   | Value           | Status                                                                |
| ------- | --------------- | ---------------------------------------------------------------------|
| `price` | `0`             | Invalid -- a menu item's price cannot be `0`.                        |
| `stock` | negative value  | Invalid -- a menu item's stock cannot be lower than `0`.              |
| `title` | duplicate value | Invalid -- there should not be more than one menu item with the same title. |

Beyond these common rules, a project can add its own: in Little Lemon, `price` additionally can't be less than `2.0`, and an attempt to add an item below that raises an error.

##### Validation in DRF

Starting point -- the `MenuItemSerializer` and `CategorySerializer` from the earlier sections:

```python
# serializers.py
from decimal import Decimal
from rest_framework import serializers

from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
```

What follows are four ways to add validation to fields on `MenuItemSerializer`.

##### Method 1: Conditions on the Field

Pass validation arguments directly when declaring a field, e.g. `min_value` to reject a `price` below `2.0`:

```python
price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)
```

POSTing a `price` of `1` to `/menu-items` now fails with a 400.

![400 - Bad Request error. Price - ensure this value is greater than or equal to 2](./assets/importance-of-data-validation-1.png)

##### Method 2: `extra_kwargs` on the Meta Class

For a field that isn't declared explicitly above `Meta`, the same validation can be added via `extra_kwargs`, which accepts extra properties/validators per field name (remove the field declaration from Method 1 first):

```python
class Meta:
    model = MenuItem
    fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
    extra_kwargs = {
        'price': {'min_value': 2},
    }
```

Sending the same POST call as before triggers the same error as Method 1. Adding a second rule -- `stock` (via `source='inventory'`) can't go below `0` -- just adds another key to `extra_kwargs`:

```python
'stock': {'source': 'inventory', 'min_value': 0}
```

Full `MenuItemSerializer` with both rules:

```python
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'stock': {'source': 'inventory', 'min_value': 0},
        }

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
```

A negative `stock` in a POST now fails too:

![400 - Bad Request error. Stock - ensure this value is greater than or equal to 0](./assets/importance-of-data-validation-2.png)

##### Method 3: `validate_<field>()` Methods

A `validate_<field_name>()` method on the serializer receives that field's submitted value and can raise `serializers.ValidationError` with a custom message; the name has to match exactly (`validate_price` for `price`, `validate_stock` for `stock`).

```python
def validate_price(self, value):
    if value < 2:
        raise serializers.ValidationError('Price should not be less than 2.0')
    return value  # must return the value once it passes validation

def validate_stock(self, value):
    if value < 0:
        raise serializers.ValidationError('Stock cannot be negative')
    return value
```

Sending invalid `price` and `stock` values now returns both custom messages:

![400 - Bad Request. Price, should not be less than 2.0. Stock, inventory cannot be negative](./assets/importance-of-data-validation-3.png)

##### Method 4: The `validate()` Method

`validate()` receives all of a serializer's input fields at once (as `attrs`), so it's the place to validate several fields together or cross-check them against each other. It replaces `validate_price`/`validate_stock` from Method 3 when used.

```python
def validate(self, attrs):
    if attrs['price'] < 2:
        raise serializers.ValidationError('Price should not be less than 2.0')
    if attrs['inventory'] < 0:
        raise serializers.ValidationError('Stock cannot be negative')
    return super().validate(attrs)
```

Note `attrs['inventory']`, not `attrs['stock']`: `validate()` sees the model's actual field name, not the serializer's renamed `stock` field.

![400 - Bad Request error. Non field errors, price should not be less than 2.0](./assets/importance-of-data-validation-4.png)

##### Where This Code Goes, and Validation Order

The four methods above are alternatives, not meant to run together (each one's write-up says to remove the previous one), but they all live in the same place: inside `MenuItemSerializer`, above `class Meta`. Methods can technically go anywhere in the class body -- Python doesn't enforce an order -- but keeping them above `Meta` matches this project's convention and keeps them next to the fields they validate.

```python
class MenuItemSerializer(serializers.ModelSerializer):
    # Method 1: field declared with a validation kwarg directly
    price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)

    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    # Method 3: validate_<field_name> -- one per field, DRF finds them by name
    def validate_price(self, value):
        if value < 2:
            raise serializers.ValidationError('Price should not be less than 2.0')
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('Stock cannot be negative')
        return value

    # Method 4: validate() -- sees every field at once, for cross-field checks
    def validate(self, attrs):
        if attrs['price'] < 2:
            raise serializers.ValidationError('Price should not be less than 2.0')
        if attrs['inventory'] < 0:
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        # Method 2: extra_kwargs -- equivalent to Method 1, but for fields
        # not declared explicitly above
        extra_kwargs = {
            'price': {'min_value': 2},
            'stock': {'source': 'inventory', 'min_value': 0},
        }

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
```

When `serializer.is_valid()` runs, DRF calls into this in a fixed order:

1. **Per-field built-in validators run first** -- this is where `min_value=2` on the field declaration (Method 1) or `'min_value': 2` in `extra_kwargs` (Method 2) gets checked, before any custom code runs.
2. **`validate_<field_name>(self, value)`** (Method 3) -- DRF looks for a method with exactly that name for each field and, if found, calls it with the value that already passed step 1. It must `return value` (or a transformed value); returning `None` would overwrite the field with `None`.
3. **`validate(self, attrs)`** (Method 4) -- called once, after every field has individually passed steps 1-2, with a dict of all validated values (`attrs`). This is the only place that can compare two fields against each other. It must `return attrs`.

Only if all three stages pass does `is_valid()` return `True` and `validated_data`/`save()` become usable -- any `ValidationError` raised along the way short-circuits validation and gets collected into the 400 response.

##### Unique Validation

To reject duplicate entries, DRF provides `UniqueValidator` for a single field and `UniqueTogetherValidator` for a combination of fields. Import whichever is needed (both are used below):

```python
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
```

**`UniqueValidator`** -- enforcing a unique `title` on `MenuItem`, either via `extra_kwargs`:

```python
extra_kwargs = {
    'title': {
        'validators': [UniqueValidator(queryset=MenuItem.objects.all())],
    },
}
```

or declared directly on the field:

```python
title = serializers.CharField(
    max_length=255,
    validators=[UniqueValidator(queryset=MenuItem.objects.all())]
)
```

A duplicate `title` now gets rejected:

![400 - Bad Request error, title field must be unique.](./assets/importance-of-data-validation-5.png)

**`UniqueTogetherValidator`** -- enforcing a unique `(title, price)` combination instead, so two items can share a title as long as their price differs. It's declared directly on `Meta`, not inside `extra_kwargs`:

```python
class Meta:
    ...
    validators = [
        UniqueTogetherValidator(
            queryset=MenuItem.objects.all(),
            fields=['title', 'price'],
        ),
    ]
```

A duplicate `(title, price)` pair now gets rejected:

![400 - Bad Request, non field errors. The fields title, price must make a unique set.](./assets/importance-of-data-validation-6.png)

#### Data Sanitization

Sanitization cleans data of potential threats before it's stored or displayed. Without it, an API is exploitable via attacks like SQL injection, or client applications via cross-site scripting (XSS) or session hijacking through injected JavaScript -- data validation alone doesn't catch these. Django sanitizes some of this automatically, but a project can still need additional, project-specific sanitization.

##### Sanitizing HTML and JavaScript

Unless HTML input is actually intended, always check for HTML tags in submitted data and neutralize them by converting special characters into HTML entities -- attackers can use `<script>` tags to inject JavaScript, or `<img>` tags to add unwanted trackers.

For example, if a menu item title of `Tomato Pasta <script>alert('hello')</script>` isn't sanitized, that `<script>` tag executes wherever the title is later displayed. An `alert('hello')` is harmless, but the same technique can inject genuinely malicious code.

The third-party `bleach` package handles this: it converts HTML special characters like `<` and `>` into HTML entities, so the browser no longer renders them as tags.

```bash
pipenv install bleach
uv add bleach
```

```python
# serializers.py
import bleach
```

Sanitizing a single field with a `validate_<field>()` method, e.g. `title`, added above the `Meta` class in `MenuItemSerializer`:

```python
def validate_title(self, value):
    return bleach.clean(value)
```

Sending a POST to `/menu-items` with HTML tags in `title` now stores the sanitized (HTML-entity-encoded) version instead of the raw tag:

![Script tag has been converted to HTML](./assets/data-sanitization_img1_new.png)

Without sanitization, the input is stored exactly as submitted:

![Script tag hasn't been converted to HTML](./assets/data-sanitization_img2_new.png)

Sanitizing from inside `validate()` instead makes it possible to clean multiple fields from one place, alongside any other cross-field validation:

```python
def validate(self, attrs):
    attrs['title'] = bleach.clean(attrs['title'])
    if attrs['price'] < 2:
        raise serializers.ValidationError('Price should not be less than 2.0')
    if attrs['inventory'] < 0:
        raise serializers.ValidationError('Stock cannot be negative')
    return super().validate(attrs)
```

##### Preventing SQL Injection

SQL injection happens when an attacker gets their own SQL embedded into input data to run malicious queries against the database.

Preventing it is straightforward: avoid raw SQL unless it's genuinely necessary, and when it is, escape parameters using string placeholders -- never place the placeholder inside quotation marks, or the protection is lost. Assuming `limit = request.GET.get('limit')`:

| Approach | `MenuItem.objects.raw(...)` call | Why |
| --- | --- | --- |
| Correct -- parameterized, unquoted placeholder | `MenuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s', [limit])` | `%s` is passed unquoted; the parameter is bound securely as part of query execution instead of being spliced into the text. |
| Incorrect -- string formatting | `MenuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s' % limit)` | `limit` is inserted into the query string via `%` formatting *before* execution, so it's never escaped and stays vulnerable to injection. |
| Incorrect -- placeholder inside quotes | `MenuItem.objects.raw("SELECT * FROM LittleLemonAPI_menuitem LIMIT '%s'", [limit])` | Wrapping `%s` in quotes turns it into a string literal in SQL, defeating the point of a parameterized query. |

#### Pagination

- Pagination breaks a large result set into smaller chunks instead of returning everything at once: without it, a client that only wants the latest 10 orders out of 1000 still gets all 1000 records back, wasting database load and bandwidth on both ends.
- The client controls chunk size and position via two query parameters: `perpage` (how many records per page) and `page` (which page to fetch). E.g. with `perpage=2`:

| Page | Records (`perpage=2`) |
| --- | --- |
| 1 | 1, 2 |
| 2 | 3, 4 |
| 3 | 5, 6 |
| 4 | 7, 8 |

- Security tip: cap the maximum `perpage` a client can request, to prevent abuse of the endpoint.
  - Example: with a max of 10 records per page, a client wanting 20 records covering 21-40 needs two calls -- `perpage=10&page=3` for records 21-30, then `perpage=10&page=4` for records 31-40.
  - If a client asks for more than the maximum in a single call (e.g. 50, when the max is 10), respond with a 400 Bad Request instead of silently truncating or ignoring the limit.
- Implementing pagination in the `menu_items` view, using Django's built-in `Paginator`:
  - Read `perpage` and `page` from the query string, defaulting to `2` and `1` respectively when the client doesn't supply them.
  - Build a `Paginator(items, per_page=perpage)` just before serializing (`per_page` is `Paginator`'s own keyword argument name, not related to the `perpage` query parameter), then fetch the requested page with `paginator.page(number=page)`.
  - Requesting a page number that doesn't exist raises `EmptyPage`; wrap the call in `try`/`except EmptyPage` and return an empty list in that case, instead of letting the exception propagate as a server error.
- Testing: `GET /menu-items` with no query string returns the default of 2 items per page; `GET /menu-items?perpage=3&page=1` returns 3 items.

```python
# views.py -- add just before serializing `items` in the GET branch of menu_items
from django.core.paginator import EmptyPage, Paginator

perpage = request.query_params.get('perpage', default=2)
page = request.query_params.get('page', default=1)

paginator = Paginator(items, per_page=perpage)
try:
    items = paginator.page(number=page)
except EmptyPage:
    items = []
```

Example requests against the paginated endpoint:

```text
# Default page size (2 items), first page
http://127.0.0.1:8000/api/menu-items

# 3 items per page, first page -> items 1-3
http://127.0.0.1:8000/api/menu-items?perpage=3&page=1

# 3 items per page, second page -> items 4-6
http://127.0.0.1:8000/api/menu-items?perpage=3&page=2

# A page number beyond the available items -> EmptyPage, empty list returned
http://127.0.0.1:8000/api/menu-items?perpage=3&page=99

# Combined with filtering, searching, and ordering from the sections above
http://127.0.0.1:8000/api/menu-items?category=main&ordering=-price&perpage=5&page=1
```

##### Complete `menu_items` View

Putting filtering, searching, ordering, and pagination together, `menu_items` now looks like this in full:

```python
# views.py
from django.core.paginator import EmptyPage, Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()

        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)

        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price=to_price)
        if search:
            items = items.filter(title__contains=search)
        if ordering:
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)
```

#### More on Filtering and Pagination

The previous sections implemented filtering, searching, and pagination by hand in a function-based view. DRF (Django REST Framework) also ships filter backend and pagination classes that add the same features to a class-based view with just a few lines of configuration.

##### Scaffolding the Project

- Step 1 -- a `ModelViewSet` gives a full CRUD endpoint for menu items in a few lines:

  ```python
  # views.py
  from rest_framework import viewsets

  from .models import MenuItem
  from .serializers import MenuItemSerializer

  class MenuItemsViewSet(viewsets.ModelViewSet):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer
  ```

- Step 2 -- map it in `urls.py`, exposing only the `GET` actions (`list` for the collection, `retrieve` for a single item):

  ```python
  # urls.py
  from django.urls import path

  from . import views

  urlpatterns = [
      path('menu-items', views.MenuItemsViewSet.as_view({'get': 'list'})),
      path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get': 'retrieve'})),
  ]
  ```

- Step 3 -- register the filtering backends in `settings.py`, under `DEFAULT_FILTER_BACKENDS`:

  ```python
  # settings.py
  REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': [
          'rest_framework.renderers.JSONRenderer',
          'rest_framework.renderers.BrowsableAPIRenderer',
          'rest_framework_xml.renderers.XMLRenderer',
      ],
      'DEFAULT_FILTER_BACKENDS': [
          'django_filters.rest_framework.DjangoFilterBackend',  # third-party package: pip install django-filter
          'rest_framework.filters.OrderingFilter',
          'rest_framework.filters.SearchFilter',
      ],
  }
  ```

With these three steps in place, `http://127.0.0.1:8000/api/menu-items` lists every item and `http://127.0.0.1:8000/api/menu-items/1` retrieves a single one.

##### Ordering and Sorting

`OrderingFilter` adds sorting support just by listing which fields are sortable, via `ordering_fields` on the view set:

```python
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
```

Visiting `http://127.0.0.1:8000/api/menu-items` now shows a filter button in the browsable API:

![Filter button option at menu-items endpoint](./assets/more-on-filtering-and-pagination-1.png)

Clicking it opens a popup with ascending/descending ordering options for each listed field:

![Pop up with ascending and descending ordering options for price and inventory](./assets/more-on-filtering-and-pagination-2.png)

The same sorting is also available directly as a query string, including by both fields at once: `http://127.0.0.1:8000/api/menu-items?ordering=price,inventory`.

##### Pagination

Two settings in the `REST_FRAMEWORK` section of `settings.py` turn on pagination for every view using the built-in pagination classes:

```python
# settings.py -- inside REST_FRAMEWORK
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE': 2,
```

`PAGE_SIZE` sets how many items DRF shows per page. Visiting the menu items endpoint now shows a paginated, differently-shaped response, with page numbers available under the filter button; only 2 records show per page because of the `PAGE_SIZE` setting above.

![Paginated API output that shows two records](./assets/more-on-Filtering-and-Searching-img1.png)

##### Search

`search_fields` on the view set turns on searching by that field:

```python
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    search_fields = ['title']
```

Opening the menu-items endpoint and clicking the filter button now also shows a search field, usable together with ordering:

![Menu-items endpoint with ordering option and search field](./assets/more-on-filtering-and-pagination-4.png)

DRF's default search lookup is `icontains` -- a case-insensitive "contains" match. Searching for `illa` matches every title containing those letters in any case, so both "Vanilla" and "VANILLA" come up.

##### Searching in Nested Fields

To search a related field too, e.g. the menu item's `category` title, use the naming convention `<related_model>__<field_name>` (a double underscore, the same relationship-traversal syntax used for filtering): the related model here is `category` and the field is `title`, so the search field is `category__title`.

```python
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    search_fields = ['title', 'category__title']
```

Clients can now search across both menu item titles and category titles, with pagination and ordering still working alongside search:

![Pagination and ordering working with the search feature](./assets/more-on-filtering-and-pagination-5.png)

Testing search via `curl`: `SearchFilter` reads the term from a `search` query parameter by default, applied with `icontains` across every field in `search_fields`, OR'd together (a match in either field is enough):

```bash
# Search across both title and category__title
curl "http://127.0.0.1:8000/api/menu-items?search=illa"
# matches "Vanilla" / "VANILLA" in title, case-insensitively

# Combine search with ordering
curl "http://127.0.0.1:8000/api/menu-items?search=illa&ordering=-price"

# Search also hits category__title, e.g. items in a category titled "Main"
curl "http://127.0.0.1:8000/api/menu-items?search=main"
```

#### Caching

- Caching serves a saved result instead of recomputing one on every request, cutting server load and bandwidth use; it's also one reason REST APIs are designed to be cacheable in the first place.
  - Motivating scenario: a restaurant's website gets featured on a popular blog, traffic spikes, and without caching the database and web server can't keep up and go down.
- A REST API is a layered architecture, and caching can happen at each layer along a typical request's path: client -> firewall -> reverse proxy -> web server -> database server, and back.
- **Database server** -- most modern databases run a query cache, storing SQL queries and their results in memory and serving from there when nothing relevant has changed, instead of re-running the query.
  - Relying on this alone is still costly: the application has to connect to the database for every request to retrieve even a cached result, and a database engine only accepts a fixed number of connections for a given amount of RAM/CPU.
- **Web server** -- server-side scripts can cache a response themselves once they're confident the underlying data hasn't changed, storing it outside the database (flat files, a separate database, or a tool like Redis or Memcached).
  - Example: 1,000 hits/minute against data that only changes once a day means up to 1,440,000 potential database hits per day; caching the result once and serving it from cache until the data changes (then flushing and re-caching) avoids nearly all of them.
- **Reverse proxy** -- traffic-heavy setups run multiple web servers behind a reverse proxy; the web server sends caching headers on its response, and the reverse proxy caches the result for the duration those headers specify, serving it directly so the web servers behind it don't get overloaded.
- **Client** -- reverse proxies or web servers can send caching headers telling the client (browser or app) how long to cache a response; the client then decides whether to reuse that cached copy or make a fresh call.
  - This layer is largely outside the server's control, which is why a solid server-side caching strategy still matters most.

#### Extra: What Is a Reverse Proxy?

- A reverse proxy is a server that sits in front of your web server(s) and intercepts incoming requests before they reach them -- the opposite of a normal ("forward") proxy, which sits in front of clients and hides them from the servers they talk to.
- In the request flow from the Caching section above (client -> firewall -> reverse proxy -> web server -> database -> back), clients only ever talk to the reverse proxy; they don't know or care which actual web server handles the request.
- Common jobs a reverse proxy takes on:
  - **Load balancing** -- with multiple web servers behind it, it distributes incoming requests across them so no single server gets overwhelmed.
  - **Caching** -- as covered above, it can cache a web server's response according to the caching headers that server sends, and serve repeat requests straight from cache without bothering the web server again.
  - **TLS/SSL termination** -- handling HTTPS itself, so backend servers don't have to.
  - Compression, and hiding backend server details/IPs for security.
  - Common examples: **nginx**, **HAProxy**, **Traefik**, and cloud load balancers (e.g. AWS ALB) are all typically deployed as reverse proxies.
- In a typical Django deployment, the reverse proxy doesn't talk to Django directly. It sits in front of a WSGI/ASGI server (e.g. **Gunicorn**, **uWSGI**, or **Daphne**/**Uvicorn** for async), which is what actually runs the Django app and handles the HTTP protocol details:

  ```text
  client -> reverse proxy (nginx, etc.) -> Gunicorn worker 1 (Django)
                                         -> Gunicorn worker 2 (Django)
                                         -> Gunicorn worker 3 (Django)
  ```

  - The reverse proxy load-balances across those Gunicorn processes/instances (multiple workers on one machine, or spread across several machines). Django itself is just the application code running inside each worker -- it doesn't listen on a port or manage connections on its own outside of `manage.py runserver`, which is dev-only and not meant for production traffic.
- Summary: reverse proxy = the thing clients connect to; load balancing = one of the jobs it does when there's more than one backend instance to spread requests across.

#### Exercise: Restaurant Menu API with Filtering, Ordering, and Searching

Folder: [`lab/05-menuitem-api-filtering/`](./lab/05-menuitem-api-filtering/), instructions: [`Instructions.md`](./lab/05-menuitem-api-filtering/Instructions.md).

- Added a `Category` model (`slug`, `title`) and gave `MenuItem` a `category` foreign key (`on_delete=models.PROTECT`, `default=1`), establishing a many-to-one relationship between menu items and categories.
- Added `serializers.py` with `CategorySerializer` (`ModelSerializer`, exposing `id`/`title`) and `MenuItemSerializer`: `category` is nested and read-only (for display), while a separate `category_id` (`write_only`) lets clients set the relation on create -- the same read/write split used in the DRF Essentials sections earlier in this file.
- Added `views.py` with two `ListCreateAPIView`s sharing the pattern from the previous exercise: `CategoriesView` for `GET`/`POST` on `/categories`, and `MenuItemsView` for `GET`/`POST` on `/menu-items`, the latter also declaring `ordering_fields`, `filterset_fields`, and `search_fields`.
- Uncommented the two routes in the app-level `urls.py`.
- Registered `OrderingFilter` and `SearchFilter` in `settings.py`'s `DEFAULT_FILTER_BACKENDS`, plus `PageNumberPagination` with `PAGE_SIZE: 3`.
  - Note: `filterset_fields` on `MenuItemsView` has no effect here, since it requires `django_filters.rest_framework.DjangoFilterBackend` to be registered too, and only `OrderingFilter`/`SearchFilter` are -- confirmed below, where `?price=6.00` returns every item, unfiltered. `ordering_fields` and `search_fields` don't need that backend and work as expected.
- Replaced the project's `Pipfile`/`Pipfile.lock` with a standalone `uv` project (`pyproject.toml`/`uv.lock`), scoped to this lab folder with its own `.venv`, independent of the repo's root-level environment.
- Ran the flow end-to-end against the dev server: created 3 categories and the 9 menu items from the walkthrough, confirmed pagination returns 3 items per page (`count: 9`, `next` pointing at page 2), confirmed `?ordering=price`/`?ordering=-price` sort ascending/descending, confirmed `?search=Pasta` matches only the two pasta dishes, and confirmed `?price=6.00` is silently ignored as expected.

Shell commands, run from inside `lab/05-menuitem-api-filtering/LittleLemon/`:

```bash
# One-time setup: create the project's own virtual environment and install dependencies
uv sync

# Create and apply the migrations for the new Category and MenuItem models
uv run python manage.py makemigrations
uv run python manage.py migrate

# Start the dev server
uv run python manage.py runserver 8080
# Browsable API: http://127.0.0.1:8080/api/categories and http://127.0.0.1:8080/api/menu-items
```

`models.py`:

```python
from django.db import models


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    # PROTECT: a category can't be deleted while menu items still reference
    # it; default=1 lets existing rows survive the migration that adds this
    # column to an already-populated table.
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self) -> str:
        return self.title
```

`serializers.py`:

```python
from rest_framework import serializers

from .models import Category, MenuItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    # Split read/write: `category` nests the full object for GET responses,
    # `category_id` is the plain FK id accepted on POST (see the
    # Deserialization and Validation section earlier for why a plain
    # IntegerField works here without a source= override).
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'category', 'category_id']
```

`views.py`:

```python
from rest_framework import generics

from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']  # ?ordering=price / ?ordering=-inventory
    filterset_fields = ['price', 'inventory']  # inert without DjangoFilterBackend -- see note above
    search_fields = ['title']  # ?search=<text>, case-insensitive "contains"
```

`urls.py` (app-level):

```python
from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
]
```

`settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3,
}
```

Testing with `curl`:

```bash
# Seed 3 categories
curl -X POST http://127.0.0.1:8080/api/categories -H "Content-Type: application/json" -d '{"title": "Main", "slug": "main"}'
curl -X POST http://127.0.0.1:8080/api/categories -H "Content-Type: application/json" -d '{"title": "Desserts", "slug": "desserts"}'
curl -X POST http://127.0.0.1:8080/api/categories -H "Content-Type: application/json" -d '{"title": "Appetizers", "slug": "appetizers"}'

# Seed a menu item, linked to category id 1 ("Main")
curl -X POST http://127.0.0.1:8080/api/menu-items -H "Content-Type: application/json" \
  -d '{"title": "Beef Pasta", "price": "6.00", "inventory": 20, "category_id": 1}'
# {"id":1,"title":"Beef Pasta","price":"6.00","inventory":20,"category":{"id":1,"title":"Main"}}

# After adding all 9 items from the walkthrough: 3 per page (PAGE_SIZE), with a `next` link
curl http://127.0.0.1:8080/api/menu-items
# {"count":9,"next":"http://127.0.0.1:8080/api/menu-items?page=2","previous":null,"results":[...3 items...]}

# Ascending / descending by price
curl "http://127.0.0.1:8080/api/menu-items?ordering=price"
curl "http://127.0.0.1:8080/api/menu-items?ordering=-price"

# Search by title (case-insensitive contains)
curl "http://127.0.0.1:8080/api/menu-items?search=Pasta"
# {"count":2, ... "results":[{"title":"Beef Pasta",...},{"title":"Tomato Pasta",...}]}

# filterset_fields has no effect: DjangoFilterBackend isn't registered, so this returns all 9, unfiltered
curl "http://127.0.0.1:8080/api/menu-items?price=6.00"
```

#### Additional Resources

- [Overview of security in Django](https://docs.djangoproject.com/en/4.1/topics/security/)
- [Memcached: Open source, high-performance, distributed memory object caching system](https://memcached.org/)
- [Redis: Open source, in-memory data store used by developers as a database, cache, streaming engine and message broker](https://redis.io/)

### Securing an API in Django REST Framework

#### Token-Based Authentication in DRF

- APIs expose back-end data to third parties, which risks breaches or corruption if left wide open; some endpoints are meant to be public, but others -- especially anything that modifies data -- should only be reachable by authenticated clients.
- Password-based authentication sends the username and password with every single API call; it works, but resending credentials constantly is both inconvenient and less secure.
- Token-based authentication instead sends credentials once: if they're valid, the server issues a token (a long, hard-to-guess string of letters, digits, and symbols) with a server-controlled lifetime.
  - The client attaches this token to a header on every later request instead of the username/password.
  - DRF (Django REST Framework)'s `TokenAuthentication` class, from the `rest_framework.authtoken` app, validates the token, checks it hasn't expired, and resolves which user it belongs to -- the request then runs as that user.
- Setting up token auth:
  - Add `'rest_framework.authtoken'` to `INSTALLED_APPS` in `settings.py`, then run migrations to create its table.
  - Create an admin user with `python manage.py createsuperuser`, and log into `/admin`, where tokens for every user are listed and new ones can be created manually (the "+"/"Add" button).
- Protecting an endpoint: an `@api_view` function is public by default -- adding `@permission_classes([IsAuthenticated])` (from `rest_framework.permissions`, applied via the `permission_classes` decorator from `rest_framework.decorators`) makes it reject unauthenticated requests with "Authentication credentials were not provided."
- Turning on token authentication so that permission check actually has something to authenticate against: set `DEFAULT_AUTHENTICATION_CLASSES` to `TokenAuthentication` in the `REST_FRAMEWORK` section of `settings.py`.
  - The token then has to be sent as `Authorization: Token <token>` -- note the scheme name is literally `Token`, not the more common `Bearer` (in a REST client like Insomnia, this means setting the auth type's prefix field to `Token`).
- Generating tokens from an endpoint instead of the admin panel: DRF ships `obtain_auth_token`, a ready-made view mapped to a `POST`-only URL. Posting a valid `username`/`password` (as form data) to it returns that user's token in the response -- useful for any user created via code, not just through the admin panel.

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

```python
# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view()
@permission_classes([IsAuthenticated])  # rejects requests with no valid token
def secret(request):
    return Response({'message': 'Some secret message'})
```

```python
# urls.py
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # ...
    path('secret', views.secret),
    path('api-token-auth', obtain_auth_token),  # POST username/password -> {"token": "..."}
]
```

```bash
# One-time setup
python manage.py migrate
python manage.py createsuperuser

# Get a token for a user (form-encoded POST)
curl -X POST http://127.0.0.1:8000/api/api-token-auth -d "username=<user>&password=<pass>"
# {"token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4"}

# Use the token to call a protected endpoint
curl http://127.0.0.1:8000/api/secret -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4"
```

#### User Roles

- Authentication alone isn't enough: an authenticated user could still call `DELETE` on a menu item, or `PATCH` someone else's order, if nothing checks whether they're actually *allowed* to. That check -- privileges/roles, not just identity -- is authorization, and Django's built-in user group system gives a straightforward way to build that layer.
- Setting up groups and users in the Django admin (`/admin`):
  - Create a group named `Manager` (no individual permissions need to be selected for this approach -- membership itself is what's checked).
  - Create two users, e.g. `johndoe` (the manager) and `jimmydoe` (a plain customer).
  - On `johndoe`'s admin page, add him to the `Manager` group under the Groups section; leave `jimmydoe` out of it.
- Building the protected view, the same pattern as the earlier `secret` view -- `@api_view()` + `@permission_classes([IsAuthenticated])`, mapped in `urls.py`: at first this only checks that *some* authenticated user is calling it, so both `johndoe` and `jimmydoe` can see the manager-only message, which is wrong.
- Fixing it: inside the view, check whether `request.user` belongs to the `Manager` group via `request.user.groups.filter(name='Manager').exists()`, and only return the message if that's `True`; otherwise respond with a 403.
- Testing with the token flow from the previous section: get a token for each user via `POST /api/api-token-auth`, then `GET` the manager view with each token -- `johndoe`'s token now gets the message, `jimmydoe`'s gets a 403.

```python
# views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({'message': 'Only Manager should see this'})
    return Response({'message': 'You are not authorized'}, status=status.HTTP_403_FORBIDDEN)
```

```python
# urls.py
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # ...
    path('secret', views.secret),
    path('manager-view', views.manager_view),
    path('api-token-auth', obtain_auth_token),  # POST username/password -> {"token": "..."}
]
```

```bash
# Get a token for each user (as in the previous section)
curl -X POST http://127.0.0.1:8000/api/api-token-auth -d "username=johndoe&password=<pass>"
curl -X POST http://127.0.0.1:8000/api/api-token-auth -d "username=jimmydoe&password=<pass>"

# johndoe is in the Manager group -> 200, sees the message
curl http://127.0.0.1:8000/api/manager-view -H "Authorization: Token <johndoe's token>"

# jimmydoe is not in the Manager group -> 403
curl http://127.0.0.1:8000/api/manager-view -H "Authorization: Token <jimmydoe's token>"
```

#### Setting up API Throttling

- Throttling limits how often a client can call an endpoint within a time window, protecting the API's compute and bandwidth from abuse; DRF ships built-in throttle classes for it.
- Two built-in throttle classes cover the common cases:
  - `AnonRateThrottle` -- applies when there's no token on the request (anonymous/unauthenticated calls).
  - `UserRateThrottle` -- applies when there's a valid token (authenticated calls).
- Rates are set globally in `settings.py`, under `DEFAULT_THROTTLE_RATES` in the `REST_FRAMEWORK` dict, as `'<scope>': '<count>/<period>'` (period is `second`, `minute`, `hour`, or `day`), e.g. `'anon': '2/minute'` or `'anon': '20/day'`.
- Applying a throttle class to a specific view uses the `@throttle_classes([...])` decorator (from `rest_framework.decorators`) alongside `@api_view()`.
  - With `AnonRateThrottle` and `'anon': '2/minute'` set, a 3rd call within a minute is rejected with a "Request was throttled" message and a countdown until the next call is allowed.
  - The same pattern with `UserRateThrottle` and `'user': '5/minute'` throttles authenticated calls after 5 requests in a minute.
- Giving one specific endpoint a different rate than the global default, instead of changing it for every authenticated endpoint: subclass `UserRateThrottle` in a new `throttles.py` file with a custom `scope` name, give that scope its own entry in `DEFAULT_THROTTLE_RATES`, then use the subclass instead of `UserRateThrottle` in that view's `@throttle_classes`.
  - Testing this, calls 1-10 succeed and the 11th is throttled, confirming the endpoint now follows its own `10/minute` limit rather than the global `5/minute` used for authenticated calls elsewhere.

```python
# throttles.py
from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'
```

```python
# views.py
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .throttles import TenCallsPerMinute

@api_view()
@throttle_classes([AnonRateThrottle])  # -> /api/throttle-check
def throttle_check(request):
    return Response({'message': 'successful'})

@api_view()
@throttle_classes([TenCallsPerMinute])  # -> /api/throttle-check-auth, 10/minute instead of the global 5/minute
def throttle_check_auth(request):
    return Response({'message': 'successful'})
```

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user': '5/minute',
        'ten': '10/minute',
    },
}
```

```bash
# Anonymous: first 2 calls in a minute succeed, the 3rd is throttled
curl http://127.0.0.1:8000/api/throttle-check
curl http://127.0.0.1:8000/api/throttle-check
curl http://127.0.0.1:8000/api/throttle-check
# {"detail": "Request was throttled. Expected available in 59 seconds."}

# Authenticated, using the custom "ten" scope: calls 1-10 succeed, the 11th is throttled
for i in $(seq 1 11); do
  curl http://127.0.0.1:8000/api/throttle-check-auth -H "Authorization: Token <token>"
done
```

#### API Throttling for Class-Based Views

Builds on the throttling basics from [Setting up API Throttling](#setting-up-api-throttling): shows how to apply the same rate limits to a class-based view instead of a function-based one, add conditional throttling per HTTP method, and reuse a custom throttle class.

##### Project Scaffolding

A `ModelViewSet` gives a full CRUD endpoint for menu items in a few lines:

```python
# views.py
from rest_framework import viewsets

from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

Mapped in `urls.py`, exposing only the `GET` actions (`list` for the collection, `retrieve` for a single item):

```python
# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsViewSet.as_view({'get': 'list'})),
    path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get': 'retrieve'})),
]
```

With these in place, `http://127.0.0.1:8000/api/menu-items` lists every item and `http://127.0.0.1:8000/api/menu-items/1` retrieves a single one.

##### Add Support for Throttling

DRF (Django REST Framework) ships ready-to-use throttling classes -- registering them globally in `settings.py` turns throttling on for every view by default:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
}
```

##### Throttling for Class-Based Views

Class-based views don't use the `@throttle_classes` decorator that function-based views do. Instead, `throttle_classes` is a public class attribute, set directly on the view set:

```python
# views.py
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class MenuItemsViewSet(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

This throttles `menu-items` for both anonymous and authenticated users, at rates set the same way as before, in `DEFAULT_THROTTLE_RATES`:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user': '10/minute',
    },
}
```

Visiting `http://127.0.0.1:8000/api/menu-items` a 3rd time within a minute (as an anonymous user) now returns an HTTP 429 -- 2 calls succeed, and the one after that is throttled:

![Error message: Request was throttled. Expected available in 58 seconds.](./assets/throttling-for-class-based-views.png)

An authenticated user (with a valid token) sees the same message, but only after 10 successful calls -- matching the `user` rate above.

##### Conditional Throttling

Throttling can also be scoped to specific HTTP methods, e.g. throttling `POST` but leaving `GET` unlimited, by overriding `get_throttles()` instead of setting `throttle_classes` as a plain class attribute (so that line is removed from the class body). On a `ModelViewSet`, `POST` requests are handled by the `create` action and `GET` list requests by the `list` action, both exposed via `self.action`:

```python
# views.py
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []
        return [throttle() for throttle in throttle_classes]
```

This limits `POST` calls to `menu-items` to 10 per minute (the `user` rate), while `GET` calls go through unthrottled.

##### Custom Throttling Classes

A custom throttle class defined earlier in the course, like `TenCallsPerMinute` in `throttles.py`, plugs in the same way as the built-in ones -- import it and add it to `throttle_classes`:

```python
# views.py
from .throttles import TenCallsPerMinute

class MenuItemsViewSet(viewsets.ModelViewSet):
    throttle_classes = [TenCallsPerMinute]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

##### Real-World Examples of API Rate Limits

A few popular services and their published rate limits, for a sense of scale:

| Service | Anonymous | Authenticated |
| --- | --- | --- |
| Facebook Graph API | -- (no anonymous access) | 200/hour |
| Instagram API | -- (no anonymous access) | 200/hour |
| Instagram Messenger API | -- (no anonymous access) | 100/second |
| WhatsApp Messaging API | -- (no anonymous access) | 80/second |

#### Introduction to Djoser library for Better Authentication

- Getting authentication and authorization wrong risks data breaches or corruption, but hand-building a full authentication layer for every DRF (Django REST Framework) project from scratch is slow and repetitive. Djoser is a package that provides a ready-made set of authentication endpoints (registration, login, password reset, etc.) with just a few lines of configuration.
- Installing and registering it:
  - `pipenv install djoser` (or `uv add djoser`), then add `'djoser'` to `INSTALLED_APPS` in `settings.py` -- it must come *after* `'rest_framework'`.
  - A `DJOSER` settings dict configures it, e.g. `USER_ID_FIELD` picks which field on the user model identifies a user in Djoser's responses (defaults to the primary key; `username` is used here). `LOGIN_FIELD` can switch the field used to log in from `username` to `email` if preferred -- left at its default in this walkthrough.
  - `TokenAuthentication` (added to `DEFAULT_AUTHENTICATION_CLASSES` earlier in this course) still applies; adding `SessionAuthentication` alongside it lets the Django admin session and Djoser's browsable API work at the same time -- safe to remove later before going to production.
  - In the project's `urls.py`, two `include()` lines mount Djoser's user-management endpoints and its token endpoints, both under an `auth/` prefix.
- The full set of endpoints Djoser adds under `http://127.0.0.1:8000/auth/`:

  | Endpoint | Methods | Purpose |
  | --- | --- | --- |
  | `users/` | GET, POST | List all users, or register a new one -- creating a user via `POST` needs no token. |
  | `users/me/` | GET, PUT, PATCH, DELETE | View, update, or delete the *authenticated* user's own account, identified by their token rather than an id in the URL. |
  | `users/confirm/` | POST | Activate a newly registered account, submitting the `uid`/`token` pair Djoser emailed on registration. |
  | `users/resend_activation/` | POST | Resend the activation email, e.g. if it expired or never arrived. |
  | `users/set_password/` | POST | Change the authenticated user's password (current + new password). |
  | `users/reset_password/` | POST | "Forgot password" flow -- sends a reset email containing a `uid`/`token` pair. |
  | `users/reset_password_confirm/` | POST | Second half of that flow -- submit the new password with the `uid`/`token` from the email. |
  | `users/set_username/` | POST | Change the authenticated user's username. |
  | `users/reset_username/` | POST | "Forgot username" flow -- sends a reset email with a `uid`/`token` pair. |
  | `users/reset_username_confirm/` | POST | Submit the new username along with the `uid`/`token` from that email. |
  | `token/login/` | POST | Exchange a username/password for an auth token. |
  | `token/logout/` | POST | Invalidate the current token (server-side logout). |

  - `users/confirm/` is this project's name for the activation step; some Djoser versions/docs call the same action `users/activation/` instead -- same purpose, just a naming difference across versions.
  - Visiting `users/` to add a new user through the browsable API first requires logging into the Django admin as a superuser.
  - The browsable API's "Extra actions" button (next to "Options" and the HTTP method button) surfaces common operations for the endpoint being viewed; "Options" itself lists the parameters and HTTP methods that endpoint accepts.
  - `token/login/` also has a browsable-API form with `username`/`password` fields, for generating a token without a separate client like Insomnia.
- Djoser also supports JWT (JSON Web Token)-based authentication as an alternative to plain tokens, covered later in the course.

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',  # must come after rest_framework
]

DJOSER = {
    'USER_ID_FIELD': 'username',
    # 'LOGIN_FIELD': 'email',  # optional: log in with email instead of username
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # lets Django admin login work alongside the browsable API
    ],
}
```

```python
# urls.py
urlpatterns = [
    # ...
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
```

```bash
# Register a new user -- no token required
curl -X POST http://127.0.0.1:8000/auth/users/ -d "username=jimmydoe&password=<pass>"

# Log in to get a token
curl -X POST http://127.0.0.1:8000/auth/token/login/ -d "username=jimmydoe&password=<pass>"
# {"auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4"}

# Get the authenticated user's own details
curl http://127.0.0.1:8000/auth/users/me/ -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4"
```

#### Registration and Authentication Endpoints with JWT

- JWT (JSON Web Token) is a popular alternative to DRF's built-in token authentication, provided by the `djangorestframework-simplejwt` package.
- Setup:
  - `pipenv install djangorestframework-simplejwt~=5.2.1` (or `uv add "djangorestframework-simplejwt~=5.2.1"`).
  - Add `'rest_framework_simplejwt'` to `INSTALLED_APPS`, and `'rest_framework_simplejwt.authentication.JWTAuthentication'` to `DEFAULT_AUTHENTICATION_CLASSES` in `settings.py`.
  - In `urls.py`, map `TokenObtainPairView` (issues tokens) and `TokenRefreshView` (renews an access token), both from `rest_framework_simplejwt.views`.
- Two tokens come out of a successful login, each with a different job:
  - **Access token** -- sent with every API call to authenticate; expires quickly (5 minutes by default in Simple JWT, configurable in `settings.py`, and deliberately kept short for security).
  - **Refresh token** -- used to obtain a new access token once the old one expires, without the client logging in again. Since an access token can't be manually invalidated before it expires, revoking a refresh token (blacklisting it) is the way to force a client to stop being able to regenerate access.
- Testing the flow:
  - `POST /api/token` with `username`/`password` (form data) returns `access` and `refresh` tokens.
  - Protected endpoints are called with `Authorization: Bearer <access token>` -- note the scheme is `Bearer` here, unlike DRF's own `TokenAuthentication`, which uses `Authorization: Token <token>`.
  - Once the access token expires, calls with it fail; `POST /api/token/refresh` with `refresh=<refresh token>` (form data) returns a fresh `access` token to use instead.
- Blacklisting a refresh token so it can no longer be used:
  - Add `'rest_framework_simplejwt.token_blacklist'` to `INSTALLED_APPS`, then run `python manage.py migrate` (restarting the dev server afterward) to create its tables.
  - Map `TokenBlacklistView` (also from `rest_framework_simplejwt.views`) in `urls.py`.
  - `POST /api/token/blacklist` with `refresh=<refresh token>` returns an empty 200 response; that refresh token is now blacklisted, and a later `POST /api/token/refresh` with it fails.

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

```python
# urls.py
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # ...
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('token/blacklist', TokenBlacklistView.as_view()),
]
```

```bash
# Log in -> access + refresh tokens
curl -X POST http://127.0.0.1:8000/api/token -d "username=<user>&password=<pass>"
# {"access": "<access token>", "refresh": "<refresh token>"}

# Call a protected endpoint with the access token
curl http://127.0.0.1:8000/api/secret -H "Authorization: Bearer <access token>"

# After the access token expires, get a new one via the refresh token
curl -X POST http://127.0.0.1:8000/api/token/refresh -d "refresh=<refresh token>"
# {"access": "<new access token>"}

# Blacklist the refresh token -- it can no longer be used to refresh
curl -X POST http://127.0.0.1:8000/api/token/blacklist -d "refresh=<refresh token>"
```

#### User Account Management

- Builds on [Introduction to Djoser library for Better Authentication](#introduction-to-djoser-library-for-better-authentication) and [User Roles](#user-roles) to register new users through Djoser and let a super admin manage group membership through a custom endpoint. Not using JWT here, so it's worth cleaning up the JWT-specific settings and URL patterns from the previous section if they're still in `settings.py`/`urls.py`.
- User registration is already fully working via Djoser's `users/` endpoint, with no extra code needed:
  - `POST` with `username`, `email`, and `password` (no token required) creates the account, as long as the username isn't taken.
  - `GET` behaves differently depending on who's asking: a superuser sees every user's full details, but a regular authenticated user only sees their own `username`/`email` -- both still need a valid token to call it at all.
- Adding a super-admin-only endpoint to add or remove a user from the `Manager` group, since Djoser doesn't provide one:
  - Restrict it with `IsAdminUser` (from `rest_framework.permissions`), which only allows staff/admin users through -- a normal user's token gets rejected.
  - The view reads a `username` from the request body, looks that user up with `get_object_or_404` (404 if it doesn't exist), and either adds or removes them from the `Manager` group depending on the HTTP method (`POST` to add, `DELETE` to remove) -- missing `username` returns a 400.

```python
# views.py
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

@api_view(['POST', 'DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data.get('username')
    if not username:
        return Response({'message': 'error: username is required'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)
    manager_group = Group.objects.get(name='Manager')

    if request.method == 'POST':
        user.groups.add(manager_group)
    elif request.method == 'DELETE':
        user.groups.remove(manager_group)
    return Response({'message': 'okay'})
```

```python
# urls.py
urlpatterns = [
    # ...
    path('groups/manager/users', views.managers),
]
```

```bash
# Add a user to the Manager group -- only works with a super admin token
curl -X POST http://127.0.0.1:8000/api/groups/manager/users \
  -H "Authorization: Token <super admin token>" -d "username=johndoe"

# A normal user's token gets rejected (IsAdminUser)
curl -X POST http://127.0.0.1:8000/api/groups/manager/users \
  -H "Authorization: Token <regular user token>" -d "username=johndoe"

# Remove a user from the Manager group
curl -X DELETE http://127.0.0.1:8000/api/groups/manager/users \
  -H "Authorization: Token <super admin token>" -d "username=johndoe"
```

## 4. Final Project
