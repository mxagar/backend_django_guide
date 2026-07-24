# Exercise: Connect Django to MySQL

## Lab Assets

A basic Django project and app are provided (`myproject`, with an app called `myapp`), managed with `uv`.

- Any Python 3.9+ should work for this lab.
- To install dependencies and create the project's virtual environment:

```bash
uv sync
```

`uv` reads `pyproject.toml`/`uv.lock`, installs the pinned dependencies (Django and `mysqlclient`), and creates the `.venv` automatically -- no separate activation step is needed since every command is run through `uv run`.

## Goal

Create and connect to a MySQL database that can be used inside a Django project.

### Objectives

- Create new MySQL database credentials.
- Update the Django project settings to enable a connection with MySQL.

## Introduction

So far, you've worked with the default SQLite database inside a Django project. In this lab, you'll create and connect to an external MySQL database instead.

This lab requires you to modify `settings.py`, and to run commands from the command-line console inside the VS Code terminal (Terminal > New Terminal, if not already open).

The project `myproject` and the app `myapp` are already set up for you.

Follow the steps below and check the output at every step.

## Steps

> Note: MySQL must already be installed on your local machine, with an admin user set up. To keep things simple, this lab starts with the `root` user.
>
> - Username: `root`
> - Password: whatever was set during your MySQL installation (if you don't recall setting one, the default is often blank).

### Step 1: Log into the MySQL shell

```bash
mysql -u root -p
```

Press Enter, then enter the password when prompted.

> Note: depending on your machine, you may need admin privileges for this command, e.g. `sudo mysql -u root -p`.

### Step 2: Create a database

```sql
CREATE DATABASE menu_db;
```

> Note: MySQL commands must end with a semicolon (`;`).

### Step 3: Verify the database was created

```sql
SHOW DATABASES;
```

Confirm the output includes `menu_db`.

### Step 4: Reconnect from the VS Code terminal

In VS Code's integrated terminal, log back into the MySQL shell the same way as Step 1:

```bash
mysql -u root -p
```

> Note: the default password used in this lab is `root`.

### Step 5: Confirm the databases are visible here too

```sql
SHOW DATABASES;
```

Confirm the same databases appear as in Step 3.

### Step 6: Create a second database

```sql
CREATE DATABASE menu_items;
```

### Step 7: Verify it was created

```sql
SHOW DATABASES;
```

Confirm `menu_items` now appears in the list.

### Step 8: Create a dedicated MySQL user (optional)

You can either use the default `root` user, or create a new one dedicated to this project:

```sql
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
```

### Step 9: Grant privileges to the new user

```sql
GRANT ALL ON *.* TO 'admindjango'@'localhost';
```

### Step 10: Apply the privilege changes

```sql
FLUSH PRIVILEGES;
```

> Note: `mysqlclient`, the MySQL database connector, is already declared as a dependency in `pyproject.toml`.

### Step 11: Exit the MySQL shell

```sql
exit
```

### Step 12: Update `DATABASES` in `settings.py`

Open `myproject/settings.py` and replace the default `DATABASES` value with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'menu_db',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'admindjango',
        'PASSWORD': 'employee@123!',
    }
}
```

Replace the database name, user, and password with your actual values if you used different ones.

### Step 13: Register the app

In the same file, update `INSTALLED_APPS` to include your app:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```

Save `settings.py`.

### Step 14: Run the migrations

In the VS Code terminal, from the folder containing `manage.py` (and outside the MySQL shell):

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

If the MySQL settings are correct, the migration output should complete successfully -- your Django project is now connected to MySQL.
