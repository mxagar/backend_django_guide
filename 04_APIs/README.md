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

### Django REST Framework Essentials

## 3. Advanced API Development

### Filtering, Ordering, Searching

### Securing an API in Django REST Framework

## 4. Final Project
