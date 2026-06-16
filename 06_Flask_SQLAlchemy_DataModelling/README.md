# Flask SQLAlchemy Data Modelling

This guide covers the database layer of Python web applications: PostgreSQL, `psycopg2`, SQLAlchemy, Flask-SQLAlchemy, migrations, CRUD workflows, relationships, and the Fyyur capstone-style project.

## Contents

- [Introduction](#introduction)
- [Interacting with Databases](#interacting-with-databases)
  - [Overview](#overview)
  - [Relational Databases](#relational-databases)
  - [Primary Keys and Foreign Keys](#primary-keys-and-foreign-keys)
  - [SQL Primer](#sql-primer)
  - [TCP/IP, Connections, Sessions, and Transactions](#tcpip-connections-sessions-and-transactions)
  - [Installing and Using PostgreSQL](#installing-and-using-postgresql)
  - [DB-API and psycopg2](#db-api-and-psycopg2)
  - [psycopg2 Exercises](#psycopg2-exercises)
- [SQLAlchemy Basics](#sqlalchemy-basics)
  - [Overview](#overview-1)
  - [Layers of Abstraction](#layers-of-abstraction)
  - [SQL Expressions and the ORM](#sql-expressions-and-the-orm)
  - [Connecting Flask-SQLAlchemy](#connecting-flask-sqlalchemy)
  - [Defining Models](#defining-models)
  - [Creating Tables and Inserting Records](#creating-tables-and-inserting-records)
  - [Interactive Mode](#interactive-mode)
  - [Data Types and Constraints](#data-types-and-constraints)
- [SQLAlchemy ORM in Depth](#sqlalchemy-orm-in-depth)
  - [Querying Models](#querying-models)
  - [Object Lifecycle](#object-lifecycle)
- [Migrations](#migrations)
  - [Introduction](#introduction-1)
  - [Lab 02 Example Structure and Code](#lab-02-example-structure-and-code)
  - [Flask-Migrate Workflow](#flask-migrate-workflow)
  - [Migration Exercise Summary](#migration-exercise-summary)
- [Build a CRUD App with SQLAlchemy Part 1](#build-a-crud-app-with-sqlalchemy-part-1)
  - [Introduction](#introduction-2)
  - [Reading Todo Items](#reading-todo-items)
  - [Model View Controller](#model-view-controller)
  - [Handling User Input](#handling-user-input)
  - [AJAX and JSON Controllers](#ajax-and-json-controllers)
  - [Sessions in Controllers](#sessions-in-controllers)
- [Build a CRUD App with SQLAlchemy Part 2](#build-a-crud-app-with-sqlalchemy-part-2)
  - [Updating and Deleting Todo Items](#updating-and-deleting-todo-items)
  - [Lab 03 Example Structure and Code](#lab-03-example-structure-and-code)
  - [Modeling Relationships](#modeling-relationships)
  - [CRUD on Lists and Todos](#crud-on-lists-and-todos)
  - [Many-to-Many Relationships](#many-to-many-relationships)
- [Project: Fyyur](#project-fyyur)
  - [Project Structure](#project-structure)
  - [Completed Fyyur Example Structure and Code](#completed-fyyur-example-structure-and-code)
  - [Implementation Checklist](#implementation-checklist)
  - [Data Handling with Flask-WTF](#data-handling-with-flask-wtf)
  - [Development Setup](#development-setup)
  - [Acceptance Criteria](#acceptance-criteria)


## Introduction

- Backend web applications often need a persistent database, a database driver, an abstraction layer, and application code that turns HTTP requests into safe database operations.
- This module uses Python, Flask, PostgreSQL, `psycopg2`, SQLAlchemy, Flask-SQLAlchemy, Flask-Migrate, and Alembic.
- PostgreSQL stores the data, `psycopg2` provides the Python Database API (DB-API) connection, SQLAlchemy provides Core and Object Relational Mapper (ORM) abstractions, and Flask-SQLAlchemy integrates those abstractions with Flask.
- The main learning path moves from direct SQL execution to ORM models, migrations, CRUD controllers, relationships, and a final project.

## Interacting with Databases

### Overview

- A web application should treat the database as a separate service with its own connection lifecycle, schema, constraints, and transaction behavior.
- SQL is useful even when using an ORM because it explains what the ORM eventually sends to the database.
- PostgreSQL can be used through terminal tools, graphical clients, or Python libraries.

### Relational Databases

- A relational database stores data in tables made of rows and columns.
- Each table should model one kind of entity, such as a todo item, artist, venue, show, user, or booking.
- Normalization keeps each fact in one place so updates do not create inconsistent duplicate data.
- Relationships connect rows across tables:
  - One-to-many: one parent row owns or groups many child rows.
  - Many-to-many: rows on both sides can connect through an association table.

### Primary Keys and Foreign Keys

- A primary key uniquely identifies one row in a table.
- A foreign key stores the primary key of a row in another table and gives the database enough information to enforce referential integrity.
- Foreign keys make joins reliable because they define the intended relationship between tables.

```sql
CREATE TABLE todolists (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL
);

CREATE TABLE todos (
  id SERIAL PRIMARY KEY,
  description VARCHAR NOT NULL,
  complete BOOLEAN NOT NULL DEFAULT false,
  list_id INTEGER NOT NULL REFERENCES todolists(id)
);
```

### SQL Primer

- SQL statements describe the action to perform and the table or rows affected by that action.
- `SELECT` reads data, `INSERT` creates rows, `UPDATE` changes existing rows, and `DELETE` removes rows.
- `WHERE` narrows the rows affected by a statement, and `ORDER BY` controls the order of returned rows.

```sql
SELECT id, description, complete
FROM todos
WHERE complete = false
ORDER BY id;
```

For a broader SQL refresher, see [the earlier database module](../02_Databases/README.md).

### TCP/IP, Connections, Sessions, and Transactions

- Database clients communicate with PostgreSQL over a network connection, usually through Transmission Control Protocol/Internet Protocol (TCP/IP).
- A connection is the communication channel between the client and database server.
- A session is the server-side context attached to a connection.
- A transaction groups database operations into a single unit of work.
- Atomicity, Consistency, Isolation, and Durability (ACID) describe the reliability guarantees expected from transactions.
- A transaction should be committed when all related operations succeed and rolled back when any operation fails.

### Installing and Using PostgreSQL

- PostgreSQL should be installed locally or made available through a managed database service.
- Common command-line programs include:
  - `createdb` to create a database.
  - `dropdb` to delete a database.
  - `psql` to open an interactive PostgreSQL shell.
  - `pg_ctl` to start, stop, or restart a local PostgreSQL server.

```bash
createdb todoapp
psql todoapp
```

Useful `psql` commands:

```text
\l          -- list databases
\c todoapp  -- connect to a database
\dt         -- list tables
\d todos    -- describe a table
\q          -- quit
```

### DB-API and psycopg2

- Python database drivers commonly implement the DB-API contract so application code can use a consistent connection and cursor workflow.
- `psycopg2` is a PostgreSQL driver for Python.
- A connection represents the database session, and a cursor executes SQL statements and fetches results.
- Parameterized SQL prevents user input from being treated as executable SQL.

```python
import psycopg2

connection = psycopg2.connect("dbname=todoapp")
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO todos (description, complete) VALUES (%s, %s)",
    ("Review SQLAlchemy models", False),
)
connection.commit()

cursor.execute("SELECT id, description, complete FROM todos ORDER BY id")
rows = cursor.fetchall()

cursor.close()
connection.close()
```

### psycopg2 Exercises

- The basic workflow is: connect, create a cursor, execute SQL, commit changes, fetch results when needed, and close resources.
- DDL statements such as `CREATE TABLE` change the schema and should be committed.
- DML statements such as `INSERT`, `UPDATE`, and `DELETE` change rows and should also be committed when they succeed.
- Query methods return different amounts of data:
  - `fetchone()` returns a single row.
  - `fetchmany(size)` returns up to `size` rows.
  - `fetchall()` returns all remaining rows.

```python
import psycopg2
from psycopg2 import sql

connection = psycopg2.connect("dbname=todoapp")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS todos")
cursor.execute(
    """
    CREATE TABLE todos (
      id SERIAL PRIMARY KEY,
      description VARCHAR NOT NULL,
      complete BOOLEAN NOT NULL DEFAULT false
    )
    """
)

table_name = "todos"
query = sql.SQL("INSERT INTO {} (description) VALUES (%s)").format(
    sql.Identifier(table_name)
)
cursor.execute(query, ("Create a DB-API example",))
connection.commit()

cursor.execute("SELECT id, description, complete FROM todos")
print(cursor.fetchall())

cursor.close()
connection.close()
```

## SQLAlchemy Basics

### Overview

- SQLAlchemy sits above the DB-API driver and offers two major styles:
  - SQLAlchemy Core builds SQL expressions in Python.
  - SQLAlchemy ORM maps Python classes to database tables.
- Flask-SQLAlchemy provides Flask-friendly configuration, a shared `db` object, model base classes, and query helpers.

![SQLAlchemy ORM](./assets/alchorm.png)

### Layers of Abstraction

- The driver, dialect, connection pool, engine, SQL expression layer, and ORM each solve a different problem.
- The dialect translates SQLAlchemy operations into database-specific SQL.
- The connection pool reuses database connections instead of opening a new connection for every request.
- The engine coordinates the dialect and pool and acts as the main interface to the database.

![Layers of abstraction in SQLAlchemy](./assets/sqla.png)

![Diagram showing SQLAlchemy layers of abstraction](./assets/sqlalchemy-layers-of-abstraction.png)

### SQL Expressions and the ORM

- SQLAlchemy Core expressions represent SQL statements as Python objects.
- The ORM lets application code work with Python objects while SQLAlchemy handles SQL generation and row mapping.
- A mapped class usually corresponds to a table, and each instance usually corresponds to a row.

![Classes and database tables are similar](./assets/pysql.png)

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/todoapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False)
```

### Connecting Flask-SQLAlchemy

- `SQLALCHEMY_DATABASE_URI` describes the database dialect, driver, credentials, host, port, and database name.
- A local PostgreSQL URI commonly starts with `postgresql://`.
- Configuration should live in a predictable place, such as `app.config` for small examples or a dedicated `config.py` file for larger apps.

![Diagram showing parts of a database connection URI](./assets/database-connection-uri-parts.png)

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@localhost:5432/todoapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
```

### Defining Models

- Models inherit from `db.Model`.
- Columns are declared with `db.Column`.
- SQLAlchemy column types include `Integer`, `String`, `Text`, `Boolean`, `DateTime`, `Float`, and database-specific types.
- Constraints such as `primary_key`, `unique`, `nullable`, `default`, `index`, and `ForeignKey` protect the shape of the data.

```python
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
```

### Creating Tables and Inserting Records

- `db.create_all()` creates tables for declared models when the app context is active.
- In production projects, migrations are preferred because they preserve a history of schema changes.
- New ORM objects are staged with `db.session.add()` and written with `db.session.commit()`.
- `db.session.rollback()` returns the session to a clean state after a failed transaction.

```python
with app.app_context():
    db.create_all()

    todo = Todo(description="Create tables from models")
    db.session.add(todo)
    db.session.commit()
```

### Interactive Mode

- The Python interpreter is useful for checking model definitions, creating sample rows, and practicing query calls.
- Import the Flask app and database object, enter the application context, and then run ORM operations.

```python
from app import app, db, Todo

with app.app_context():
    Todo.query.order_by(Todo.id).all()
```

### Data Types and Constraints

- Data types should match the values the application actually stores.
- `nullable=False` is useful for required data that should never be missing.
- `unique=True` prevents duplicate values for fields such as usernames or emails.
- Foreign key constraints should be paired with relationship configuration when the application needs object navigation.

![SQLAlchemy Core versus SQLAlchemy ORM](./assets/sqlalchemy-layers.png)

![SQLAlchemy layers and responsibilities](./assets/sql-alchemy-layers-responsibilities.png)

![Classes in Python vs. Tables](./assets/classes-tables.png)

![Creating an instance of your database](./assets/db-instance.png)

## SQLAlchemy ORM in Depth

### Querying Models

- `Model.query` builds ORM queries against a model class.
- Common query methods include `all()`, `first()`, `get()`, `filter()`, `filter_by()`, `order_by()`, `limit()`, and `count()`.
- `filter_by()` is convenient for equality checks on column names.
- `filter()` accepts SQLAlchemy expressions and supports comparisons, `like`, `ilike`, `in_`, `is_`, and other operators.

```python
Todo.query.all()
Todo.query.filter_by(complete=False).all()
Todo.query.filter(Todo.description.ilike("%sql%")).order_by(Todo.id).all()
```

[SQLAlchemy query cheat sheet](./assets/query-cheat-sheet.pdf)

### Object Lifecycle

- A transient object has been constructed in Python but is not attached to a session.
- A pending object has been added to a session but not committed.
- A persistent object is associated with a session and represents a database row.
- A deleted object is marked for deletion and removed when the transaction commits.
- A detached object is no longer associated with a live session.

```python
todo = Todo(description="Learn the ORM lifecycle")  # transient
db.session.add(todo)                                # pending
db.session.commit()                                 # persistent
db.session.delete(todo)                             # deleted
db.session.commit()
```

## Migrations

### Introduction

- Migrations record schema changes as versioned files instead of relying on one-time table creation.
- Alembic is the migration engine used by Flask-Migrate.
- Flask-Migrate integrates Alembic commands into the Flask command-line interface.
- Migration files should be reviewed before they are applied because autogeneration can miss intent.

![Migrations](./assets/migrations.png)

Exercise code: [`lab/02_todo_app/`](./lab/02_todo_app/).

- Purpose: practice adding Flask-Migrate to a small todo application.
- Major steps: configure the database URI, initialize migrations, generate migration revisions, apply upgrades, and inspect generated files.
- Important outputs: a `migrations/` directory and revision files under `migrations/versions/`.
- Assumption: PostgreSQL is running and a `todoapp` database exists.

### Lab 02 Example Structure and Code

```text
lab/02_todo_app/
└── todoapp/
    ├── app.py
    ├── migrations/
    │   ├── alembic.ini
    │   ├── env.py
    │   └── versions/
    └── templates/
        └── index.html
```

- `app.py` defines the Flask app, configures the PostgreSQL connection, creates the `db` object, and attaches Flask-Migrate with `Migrate(app, db)`.
- `Todo` is the first mapped model; it stores an integer primary key, a required description, and a boolean completion flag.
- The `/todos/create` route is intended to receive a submitted description, create a `Todo`, commit it, and return JSON.
- The `/` route renders `templates/index.html` with all todo records from the database.
- The migrations folder records schema changes generated from the SQLAlchemy models.

```python
from flask import Flask, jsonify, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/todoapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)


@app.route("/todos/create", methods=["POST"])
def create_todo():
    description = request.get_json()["description"]
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return jsonify({"id": todo.id, "description": todo.description})


@app.route("/")
def index():
    return render_template("index.html", data=Todo.query.all())
```

- The example keeps the migration setup close to the model so `flask db migrate` can inspect `db.metadata`.
- `SQLALCHEMY_TRACK_MODIFICATIONS` is disabled because Flask-SQLAlchemy's event system is not needed for this app.
- The route returns the inserted row's generated `id`, which is useful when a JavaScript frontend needs to add the new item to the page without reloading.

### Flask-Migrate Workflow

```bash
export FLASK_APP=app.py
flask db init
flask db migrate -m "create todo tables"
flask db upgrade
```

- `flask db init` creates the Alembic migration environment.
- `flask db migrate` compares model metadata with the current database schema and creates a revision file.
- `flask db upgrade` applies unapplied revisions to the database.
- Later model changes should create new migration revisions instead of editing already-applied revisions.

### Migration Exercise Summary

- Part 1 configures the Flask app, database object, and migration object.
- Part 2 initializes Alembic and checks the generated migration folder.
- Part 3 creates a migration after defining or changing models.
- Part 4 applies the migration to the database and validates the resulting tables.

```python
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/todoapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

## Build a CRUD App with SQLAlchemy Part 1

### Introduction

- CRUD applications Create, Read, Update, and Delete records.
- Flask routes act as controllers: they receive requests, call model/session logic, and return templates or JSON responses.
- The todo app demonstrates how a single-page interface can stay in sync with SQLAlchemy-backed state.

### Reading Todo Items

- Reading data usually starts by querying model objects and passing them into a template.
- Jinja templates can loop through ORM objects and render their fields.
- Ordering in the query keeps the rendered list stable.

```python
@app.route("/")
def index():
    todos = Todo.query.order_by(Todo.id).all()
    return render_template("index.html", todos=todos)
```

### Model View Controller

- Model View Controller (MVC) separates responsibilities:
  - Models describe data and persistence behavior.
  - Views render data for users.
  - Controllers handle requests and coordinate model/view work.
- Flask does not force MVC terminology, but the separation still helps keep routes, templates, and model logic understandable.

![Model-View-Controller Diagram](./assets/mcv.png)

### Handling User Input

- Flask can read user input from route parameters, query strings, form bodies, or JSON request bodies.
- Server-side code must validate and normalize input before storing it.
- Form submissions work well for full-page HTML workflows.
- JSON requests work well for asynchronous JavaScript interactions.

![Three methods of getting user data in Flask](./assets/get-user-data.png)

```python
from flask import request, redirect, url_for

@app.route("/todos/create", methods=["POST"])
def create_todo():
    description = request.form.get("description", "").strip()
    if description:
        db.session.add(Todo(description=description))
        db.session.commit()
    return redirect(url_for("index"))
```

### AJAX and JSON Controllers

- Asynchronous JavaScript can send JSON to Flask without reloading the page.
- The controller reads `request.get_json()`, validates the payload, commits the transaction, and returns JSON.
- On failure, the controller should roll back the session and return an error status.

```python
from flask import jsonify

@app.route("/todos/<int:todo_id>/set-completed", methods=["POST"])
def set_completed(todo_id):
    data = request.get_json() or {}
    todo = Todo.query.get_or_404(todo_id)
    todo.complete = bool(data.get("complete", False))

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"success": False}), 500

    return jsonify({"success": True, "id": todo.id, "complete": todo.complete})
```

### Sessions in Controllers

- The SQLAlchemy session tracks pending object changes during a request.
- A successful request should commit exactly the changes it intends to persist.
- A failed request should roll back before returning an error.
- Broad exception handling is acceptable around transaction boundaries when it is paired with rollback and a useful response.

## Build a CRUD App with SQLAlchemy Part 2

### Updating and Deleting Todo Items

- Updating loads an existing row, mutates its fields, and commits.
- Deleting loads an existing row, marks it for deletion, and commits.
- JavaScript frontends often use `fetch()` to call update and delete routes and then update the page.

```python
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)

    try:
        db.session.delete(todo)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"success": False}), 500

    return jsonify({"success": True, "deleted": todo_id})
```

Starter/final todo app code: [`lab/03_todo_app_final/`](./lab/03_todo_app_final/).

- Purpose: demonstrate a fuller CRUD todo app with lists, todos, migrations, templates, and a solution file.
- Major steps: create list and todo models, read todos by list, add todos, update completion state, delete todos, and manage related lists.
- Important inputs and outputs: HTML form data, JSON requests from JavaScript, rendered `index.html`, and JSON success/error responses.
- Relevant API choices: Flask routes, `request.form`, `request.get_json()`, SQLAlchemy sessions, model relationships, and Alembic migrations.

### Lab 03 Example Structure and Code

```text
lab/03_todo_app_final/
└── todoapp/
    ├── app.py
    ├── app_sol.py
    ├── requirements.txt
    ├── migrations/
    │   ├── alembic.ini
    │   ├── env.py
    │   └── versions/
    └── templates/
        └── index.html
```

- `app.py` is the working todo application; `app_sol.py` is the completed reference version.
- `TodoList` is the parent model and `Todo` is the child model.
- `Todo.list_id` is the foreign key that connects each todo item to one list.
- `TodoList.todos` provides object-level access from a list to its todo items.
- The app renders one active list at a time and uses JSON endpoints for create, update, and delete actions.

```python
class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey("todolists.id"), nullable=False)


class TodoList(db.Model):
    __tablename__ = "todolists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship("Todo", backref="list", lazy=True)
```

```python
@app.route("/lists/<list_id>")
def get_list_todos(list_id):
    lists = TodoList.query.all()
    active_list = TodoList.query.get(list_id)
    todos = Todo.query.filter_by(list_id=list_id).order_by("id").all()

    return render_template(
        "index.html",
        todos=todos,
        lists=lists,
        active_list=active_list,
    )
```

- The list route queries all lists for navigation, loads the active list for the page heading, and loads only the todos that belong to the active list.
- Creating a todo requires both the description and `list_id`; the new row is committed before its generated `id` can be returned to the browser.
- Deleting a list should also handle its child todos, either manually or through a relationship cascade.
- The solution file demonstrates the complete CRUD flow, including list creation, todo completion updates, todo deletion, and list deletion.

### Modeling Relationships

- A one-to-many relationship is appropriate when one parent owns many children, such as one todo list containing many todo items.
- A foreign key column stores the parent row's identifier on the child table.
- `db.relationship()` adds object-level navigation between related models.

![Relationships and Joins](./assets/manyvehciles.png)

![Parent Child Relationship](./assets/parent-child-rel.png)

![Referencing Foreign Key](./assets/referencing-foreign-key.png)

![Foreign Key Constraint](./assets/foreign-key-constraint.png)

```python
class TodoList(db.Model):
    __tablename__ = "todolists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship(
        "Todo",
        backref="list",
        lazy=True,
        cascade="all, delete-orphan",
    )


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey("todolists.id"), nullable=False)
```

### CRUD on Lists and Todos

- Creating a child row requires a valid parent identifier.
- Reading grouped data is easier when the parent model has a relationship to its children.
- Deleting a parent should either be blocked by existing children or intentionally cascade to delete the children.
- The todo app uses cascades so deleting a list can delete its todo items as part of the same object graph.

![MVC Flow](./assets/mvc2.png)

![CRUD Solution](./assets/crud_solution.png)

### Many-to-Many Relationships

- A many-to-many relationship needs an association table between the two entity tables.
- The association table stores foreign keys to both sides.
- Extra columns can be added to the association table when the relationship itself has data, such as a show date.

```python
artist_genres = db.Table(
    "artist_genres",
    db.Column("artist_id", db.Integer, db.ForeignKey("artists.id"), primary_key=True),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True),
)


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    genres = db.relationship("Genre", secondary=artist_genres, back_populates="artists")


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    artists = db.relationship("Artist", secondary=artist_genres, back_populates="genres")
```

## Project: Fyyur

Starter project: [`lab/01_fyyur_starter/`](./lab/01_fyyur_starter/).

Completed project: [`lab/04_fyyur_completed/`](./lab/04_fyyur_completed/).

- Purpose: replace mock data in a Flask booking application with real PostgreSQL-backed models and queries.
- Major steps: configure the database, define models, create migrations, implement create/list/detail/search controllers, and preserve the shape expected by existing templates.
- Important entities: venues, artists, and shows.
- Important workflows: create venues, create artists, create shows, search artists and venues, list shows, and render artist/venue detail pages.
- Relevant API choices: Flask, SQLAlchemy ORM, Flask-Migrate, PostgreSQL, Flask-WTF forms, WTForms field `.data`, and Bootstrap 3 templates.

### Project Structure

```text
lab/01_fyyur_starter/
├── app.py          # main Flask app, routes, controllers, and model section
├── config.py       # database URL and application configuration
├── forms.py        # Flask-WTF form definitions
├── requirements.txt
├── static/         # CSS, JavaScript, fonts, and images
└── templates/      # page, form, layout, and error templates
```

### Completed Fyyur Example Structure and Code

```text
lab/04_fyyur_completed/
├── app.py
├── config.py
├── forms.py
├── requirements.txt
├── static/
└── templates/
```

- The completed project keeps the starter templates and forms but replaces mock dictionaries with database-backed models and route helpers.
- `config.py` reads `DATABASE_URL` when present and otherwise defaults to a local PostgreSQL database named `fyyur`.
- `Venue`, `Artist`, and `Show` are normalized models: shows connect venues and artists with foreign keys.
- Genres are stored as a comma-separated string to fit the starter form shape, then converted back to lists when rendering templates.
- Detail pages serialize related shows into the dictionaries expected by `show_venue.html` and `show_artist.html`.

```python
class Venue(db.Model):
    __tablename__ = "venues"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, index=True)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(500), nullable=False, default="")
    shows = db.relationship(
        "Show",
        back_populates="venue",
        cascade="all, delete-orphan",
        lazy=True,
    )
```

```python
class Show(db.Model):
    __tablename__ = "shows"

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey("venues.id"), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, index=True)

    venue = db.relationship("Venue", back_populates="shows")
    artist = db.relationship("Artist", back_populates="shows")
```

```python
@app.route("/venues/search", methods=["POST"])
def search_venues():
    search_term = request.form.get("search_term", "").strip()
    matches = (
        Venue.query
        .filter(Venue.name.ilike(f"%{search_term}%"))
        .order_by(Venue.name)
        .all()
    )
    response = {
        "count": len(matches),
        "data": [{"id": venue.id, "name": venue.name} for venue in matches],
    }
    return render_template(
        "pages/search_venues.html",
        results=response,
        search_term=search_term,
    )
```

- `ilike()` gives case-insensitive partial matching for PostgreSQL-backed search.
- `get_or_404()` keeps missing detail pages consistent with Flask's normal 404 handling.
- Every create/edit/delete route commits on success and rolls back on failure.
- Upcoming and past shows are separated by comparing each `Show.start_time` to the current UTC time.

### Implementation Checklist

- Connect `config.py` to a PostgreSQL database.
- Define normalized SQLAlchemy models for venues, artists, and shows.
- Use Flask-Migrate to create and apply schema migrations.
- Replace mock data in controllers with real queries.
- Implement creation flows for venues, artists, and shows.
- Implement partial, case-insensitive search for artists and venues.
- Render venue and artist detail pages from real data.
- Separate past and upcoming shows by comparing show start time with the current time.
- Preserve the existing template data shape so frontend templates keep working.

### Data Handling with Flask-WTF

- Flask-WTF form objects expose submitted values through each field's `.data` attribute.
- Using form objects keeps validation and request parsing in one place.
- Controller code should translate form data into model objects, add the objects to the session, and commit the transaction.

```python
@app.route("/shows/create", methods=["POST"])
def create_show_submission():
    form = ShowForm()
    show = Show(
        artist_id=form.artist_id.data,
        venue_id=form.venue_id.data,
        start_time=form.start_time.data,
    )

    try:
        db.session.add(show)
        db.session.commit()
    except Exception:
        db.session.rollback()
        flash("An error occurred. Show could not be listed.")
    else:
        flash("Show was successfully listed.")

    return redirect(url_for("index"))
```

### Development Setup

```bash
cd 06_Flask_SQLAlchemy_DataModelling/lab/04_fyyur_completed
python -m venv env
source env/bin/activate
pip install -r requirements.txt
createdb fyyur
export FLASK_APP=app.py
export FLASK_ENV=development
flask db upgrade
python app.py
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.\env\Scripts\Activate.ps1
$env:DATABASE_URL = "postgresql://localhost:5432/fyyur"
```

### Acceptance Criteria

- The application connects to PostgreSQL and no longer depends on mock data.
- New artists, venues, and shows are persisted and visible through list, detail, and search pages.
- Venue results remain grouped by city and state.
- Search supports partial, case-insensitive matching.
- Venue and artist pages distinguish past shows from upcoming shows.
- Migrations create the complete schema with appropriate column types, constraints, defaults, and relationships.
- Referential integrity is preserved between venues, artists, and shows.
