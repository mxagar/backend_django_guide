# Exercise: Submitting a form with JavaScript

## Lab Assets

A basic Django project and app are provided (`myproject`, with an app called `myapp`), managed with `uv`, along with a template and supporting files for the lab.

### Objectives

- Set up a JavaScript event to submit form data as a JSON object.
- Display a successful form submission alert using JavaScript.

## Introduction

The goal is to submit form data as a JSON object using JavaScript event handling, and display a submission alert.

### Initial Lab Instructions

This lab requires modifying:

- `views.py`
- `templates/menu_items.html`

Starter code has already been added to:

- `settings.py`
- `forms.py`
- `models.py`
- `urls.py` (app-level)
- `urls.py` (project-level)

Run commands from the VS Code integrated terminal (Terminal > New Terminal, if not already open). The project `myproject` and the app `myapp` are already preconfigured.

Follow the steps below and check the output at every step.

> Note: MySQL must already be installed locally, with the `root` user set up. To keep things simple, this lab starts with the `root` user's credentials (password `password` or blank -- press Enter for a blank password; the password won't be visible as it's typed).

## Steps

### Step 1: Check the MySQL settings

Open `settings.py` and confirm the MySQL configuration matches your local machine. Create the database name found there if it doesn't already exist locally -- otherwise Django will throw an error.

> Note: before touching the database, make sure the user configured in `settings.py` has all the privileges needed to access and modify it. Run the necessary commands to create that user and grant it access, if you haven't already.

### Step 2: Review the model and form

Open `models.py` to see the model created for this lab, then `forms.py` to see its matching form. Note that the form fields and model fields share the same names -- more on why shortly.

> Note: there are easier ways to build a form directly from a model using a `Meta` class (i.e. a `ModelForm`); this lab defines them separately, for clarity.

### Step 3: Sync the project's dependencies

```bash
uv sync
```

`uv` reads `pyproject.toml`/`uv.lock`, installs Django and `mysqlclient`, and creates the project's `.venv` automatically -- every command below runs through `uv run`, so there's no separate activation step.

### Step 4: Confirm the dependencies are installed

```bash
uv add django mysqlclient
```

(No-op if `uv sync` already installed them -- `uv add` is idempotent and just ensures both packages are declared and present.)

### Step 5: Run the migrations

From the directory containing `manage.py`:

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

> Note: if migration fails due to a conflict with existing rows lacking default values, choose the option to provide a one-off value (e.g. the string `null`) when prompted.

### Step 6: Implement `form_view()` in `views.py`

The necessary imports are already in place, and an empty `form_view()` function is ready to fill in. Implement it as follows:

- If `request.method` is `'POST'`:
  - Assign `MenuForm(request.POST)` to `form`.
  - If `form.is_valid()`:
    - Assign `form.cleaned_data` to `cd`.
    - Create a `Menu()` instance, passing `item_name=cd['item_name']`, `category=cd['category']`, `description=cd['description']`.
    - Call `.save()` on that instance.
    - Return `JsonResponse({'message': 'success'})`.
- Otherwise (or after the `POST` branch falls through), return `render()` with `request`, `'menu_items.html'`, and `{'form': form}`.

Save the file and check for errors.

> Note: the template name doesn't have to match the database/table name, which in this case is `menu_items`.

### Step 7: Add the template markup

Open `menu_items.html` and add the starter HTML:

```html
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Menu Items</title>
</head>
<body class="bg-light">
<div class="container pt-4">
    <h1>Menu Items</h1>
    <form method="POST" id="form">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
```

> Note: pay attention to the Bootstrap stylesheet included in the markup above.

### Step 8: Add the `<script>` tag

Below the HTML added in Step 7, add an opening and closing `<script>` tag -- the JavaScript in the next step goes inside it.

### Step 9: Add the JavaScript

Inside the `<script>` tags, implement the following (remember: unlike Python, JavaScript statements end with a semicolon):

- Create a constant `form` via `document.getElementById('form')`.
- Call `form.addEventListener('submit', submitHandler)`.
- Define `function submitHandler(e) { ... }`:
  - Call `e.preventDefault()`.
  - Call `fetch(form.action, { method: 'POST', body: new FormData(form) })`.
  - Chain `.then(response => response.json())`.
  - Chain `.then(data => { if (data.message === 'success') { alert('Success!'); form.reset(); } })`.

```html
<script>
    const form = document.getElementById('form');
    form.addEventListener('submit', submitHandler);

    function submitHandler(e) {
        e.preventDefault();

        fetch(form.action, { method: 'POST', body: new FormData(form) })
            .then(response => response.json())
            .then(data => {
                if (data.message === 'success') {
                    alert('Success!');
                    form.reset();
                }
            });
    }
</script>
```

Save `menu_items.html` and check for errors.

### Step 10: Run the server

```bash
uv run python manage.py runserver
```

Visit the local URL and confirm the form renders.

### Step 11: Submit the form

Enter an item name, category, and description, then submit. Confirm the "Success!" alert appears. Repeat for a few more entries.

### Step 12: Open the MySQL shell

```bash
mysql -u root -p
```

> Note: the password here is the same as the one set for `root`.

### Step 13: Verify the data was saved

Inside the MySQL shell, switch to the project's database and inspect the generated `myapp_menu` table to confirm the entries submitted through the form were saved. (A third-party MySQL GUI tool works too, if preferred.)

> Note: the table will be empty if no entries were submitted successfully -- revisit the earlier steps if so.
