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

### Principles of API Development

### Writing Your First API

## 2. Django REST Framework

### Introduction to Django REST Framework (DRF)

### Django REST Framework Essentials

## 3. Advanced API Development

### Filtering, Ordering, Searching

### Securing an API in Django REST Framework

## 4. Final Project


