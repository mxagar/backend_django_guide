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

APIs need to be secured because they give third-party clients access to backend data -- without proper security, anyone could tamper with the data or access sensitive information. Even once a client is allowed to access the data, you still need to control who is permitted to do what: that is what authentication and authorization handle. Although the two terms sound similar, they are not the same; this reading covers the difference between them and how to use each to protect API endpoints.

##### Authentication

Authentication is the process of verifying the credentials of a user.

- Logging into a website with a username and password is a typical example of authentication.
- When the username and password match, the website recognizes the user and sets cookies in the user's browser.
- On subsequent page visits, the browser sends those cookies in the HTTP request headers; the website recognizes them, together with server-side session data, and does not ask for credentials again until the user logs out.

Token-based authentication follows a similar two-step pattern in an API architecture:

1. The client identifies itself with a username and password.
2. The API server issues a bearer token, which the client then includes with every subsequent API call; the server verifies the token and decides whether to allow the requested action -- that decision step is authorization, covered below.

If the credentials are not valid, the client receives a `401 Unauthorized` HTTP status code.

This is like a first day at a new office: you submit your papers and documents once, receive an employee card, and from then on only the employee card is needed to get inside. Authentication works the same way.

The two steps of the API authentication process are shown below.

**Authentication process: getting an access token**

![Diagram of the process of getting an access token](./assets/authentication-and-authorization-1.png)

**Authenticated API calls**

![Diagram of an authenticated API call](./assets/authentication-and-authorization-2.png)

##### Authorization

However, even with an employee card, not all rooms or spaces in the office are accessible -- some areas are restricted to a specific group of people who have been given that privilege. Authorization works the same way: authentication lets you in, authorization lets you act, checking after authentication whether the user has the proper privileges to perform a given task.

- On the server side, this is typically implemented by assigning the user to one or more groups.
- After verifying the token, the server code checks whether the user belongs to the group required for that action.
- If not, the client receives a `403 Forbidden` HTTP status code.

**API authorization**

![Diagram of API authorization](./assets/authentication-and-authorization-3.png)

This extra authorization layer ensures that only users with the proper privileges can access and modify data. An authorization system is an important part of any API project, since it prevents data corruption and data breaches.

##### Implementing Authorization

Privileges are the individual tasks an API user can perform, and they are the building blocks of an authorization layer.

- As an API developer, first identify the privileges required by the project. For a bookshop, these might include:
  - Browse the books
  - Add new books
  - Edit books
  - Delete books
  - Place orders
- Not every user has every privilege -- for example, regular customers cannot add or edit books even once authenticated; only managers can.
- After identifying the privileges, distribute them across multiple roles.
- The authorization check itself happens in the backend code of each API endpoint that requires a role check: the developer verifies whether the user belongs to the appropriate group or role, then allows or denies the action accordingly.

##### User Groups in Django

The Django admin panel has built-in support for a user group system.

- Logging into the admin panel shows two distinct sections: **Users** and **Groups**.

![Django admin panel with two sections for users and groups](./assets/authentication-and-authorization-4.png)

- From there, you can create groups/roles such as `Manager`, `Editor`, `Customer`, or `Admin`, and assign privileges to each group.
- Clicking **Add** next to Groups opens a screen for creating a new group; Django automatically lists the privileges available based on the project's models. For example, a bookshop project shows the following available privileges:

![Django admin panel with bookshop privileges listed](./assets/authentication-and-authorization-5.png)

- On this screen you can create an `Editor` role and assign it privileges:

![Django admin panel with Editor role and privileges](./assets/authentication-and-authorization-6.png)

- Or create a `Customer` role with a different set of privileges:

![Django admin panel with Customer role and privileges](./assets/authentication-and-authorization-7.png)

- The admin panel lets you manage groups throughout the project's lifetime, adding or removing privileges as the project grows:

![Django admin panel with two user roles](./assets/authentication-and-authorization-8.png)

- Creating groups with privileges is not enough by itself: after creating the groups and assigning users to them, the function- or class-based views still need code that checks whether the authenticated user belongs to the required group(s) and acts on that check -- covered later in the course.

### Writing Your First API

## 2. Django REST Framework

### Introduction to Django REST Framework (DRF)

### Django REST Framework Essentials

## 3. Advanced API Development

### Filtering, Ordering, Searching

### Securing an API in Django REST Framework

## 4. Final Project
