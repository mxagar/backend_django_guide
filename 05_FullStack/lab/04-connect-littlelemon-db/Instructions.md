# Exercise: Connect the Little Lemon back-end to MySQL

## Lab Assets

A basic Django project and app are provided (`myproject`, with an app called `myapp`), managed with `uv`, along with an updated template and supporting files.

### Objectives

- Create new MySQL database credentials.
- Update the Django project settings to enable a connection with MySQL.
- Migrate models and update the database table.

## Introduction

This lab creates and connects to an external MySQL database for use inside a Django project: migrating models and populating the database with the booking times available on the Little Lemon website.

This is part one of the final assessment -- making the database connection. A later part builds the booking option on the Little Lemon website template using JavaScript, backed by this MySQL database.

### Initial Lab Instructions

This lab requires modifying:

- `settings.py`
- `models.py`

Run commands from the VS Code integrated terminal (Terminal > New Terminal, if not already open). The project `myproject` and the app `myapp` are already set up.

Follow the steps below and check the output at every step.

> Note: MySQL must already be installed locally, with the `root` user set up. To keep things simple, this lab starts with the `root` user's credentials (password `password` or blank -- press Enter for a blank password; the password won't be visible as it's typed).

## Steps

### Step 1: Log into the MySQL shell

```bash
mysql -u root -p
```

Press Enter, then enter the password when prompted.

> Note: depending on your machine, you may need admin privileges for this command, e.g. `sudo mysql -u root -p`.

### Step 2: Create a database

```sql
CREATE DATABASE reservations;
```

> Note: MySQL commands must end with a semicolon (`;`).

### Step 3: Verify the database was created

```sql
SHOW DATABASES;
```

Confirm the output includes `reservations`.

### Step 4: Sync the project's dependencies

In VS Code's terminal, navigate to the project directory and run:

```bash
uv sync
```

`uv` reads `pyproject.toml`/`uv.lock`, installs Django and `mysqlclient`, and creates the project's `.venv` automatically -- every command below runs through `uv run`, so there's no separate activation step.

### Step 5: Reconnect from the VS Code terminal

```bash
mysql -u root -p
```

> Note: the password here is the same as the one set for `root` on your local machine.

### Step 6: Confirm the database is visible here too

```sql
SHOW DATABASES;
```

Confirm `reservations` appears in the list.

### Step 7: Create a dedicated MySQL user

```sql
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
```

### Step 8: Grant privileges to the new user

```sql
GRANT ALL ON *.* TO 'admindjango'@'localhost';
```

> Note: full privileges are granted here for simplicity, but this isn't ideal practice in production.

### Step 9: Apply the privilege changes

```sql
FLUSH PRIVILEGES;
```

> Note: privileges assigned via `GRANT` don't strictly require `FLUSH PRIVILEGES`, but it's good practice to run it whenever you change privileges or reload the grant tables.

### Step 10: Exit the MySQL shell

```sql
exit
```

### Step 11: Register the app

Open `settings.py` and add `'myapp'` to `INSTALLED_APPS`.

### Step 12-13: Update `DATABASES` in `settings.py`

Replace the default `DATABASES` value with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reservations',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'admindjango',
        'PASSWORD': 'XXX',
    }
}
```

Save `settings.py`.

### Step 14: Run the migrations

From the directory containing `manage.py`:

```bash
uv run python manage.py makemigrations
```

### Step 15: Review the model

Open `models.py` and note the `Booking` model already defined there.

### Step 16: Apply the migrations

```bash
uv run python manage.py migrate
```

This creates the `Booking` table -- visible via a MySQL extension in VS Code, or the MySQL shell (next step).

### Step 17: Inspect the generated table

Log back into the MySQL shell with your credentials, then:

```sql
USE reservations;
SHOW TABLES;
DESCRIBE myapp_booking;
```

This lists all the tables Django created during migration (the one to focus on is `myapp_booking`), then shows the fields generated from the `Booking` model.

> Note: the table will be empty at this point -- it still needs to be populated.

## Conclusion

This was part one of the final assessment: connecting the Django application to a MySQL database and creating a table from the model. The next part uses this model to update the template.
