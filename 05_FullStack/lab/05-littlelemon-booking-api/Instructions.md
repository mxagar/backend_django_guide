# Exercise: Set up a Little Lemon booking API

## Lab Assets

A basic Django project and app are provided (`littlelemon`, with an app called `restaurant`), managed with `uv`, along with an updated template and supporting files.

> Note: this lab uses its own starter code (including extra stylesheets/formatting), not a continuation of the project from part one -- use the provided files rather than the earlier lab's project.

### Objectives

- Create a view to process form data entered in a Django template.
- Convert form data received via POST into a JSON object and return it to a web page.

## Introduction

Part one of the assessment set up a MySQL database, far more secure and scalable than the SQLite used earlier. This is part two: integrating the booking feature into the existing website using plain Django (no JavaScript yet) -- building a model form from the earlier model, populating it with data, then processing that data and sending it to the front end as a JSON object.

### Initial Lab Instructions

This lab requires modifying:

- `views.py`
- `forms.py`
- `urls.py` (app-level)
- `templates/bookings.html`
- `templates/book.html`

Starter code has already been added to:

- `settings.py`
- `models.py`
- `urls.py` (app-level and project-level)
- `views.py` (partially complete)

The project `littlelemon` and the app `restaurant` are already set up.

Follow the steps below and check the output at every step.

> Note: MySQL must already be installed locally, with the `root` user set up. To keep things simple, this lab starts with the `root` user's credentials (password `password` or blank -- press Enter for a blank password; the password won't be visible as it's typed).

## Steps

### Step 1: Sync the project's dependencies

From the directory containing `manage.py`:

```bash
uv sync
```

`uv` reads `pyproject.toml`/`uv.lock`, installs Django and `mysqlclient`, and creates the project's `.venv` automatically -- every command below runs through `uv run`, so there's no separate activation step. (If you run into trouble with the virtual environment, the project can also be run without `uv`, using a system Python with the same dependencies installed.)

### Step 2: Create `forms.py`

In the `restaurant` directory, create `forms.py` and import:

- The `Booking` model from `models.py`.
- The `forms` module from the `django` package.

### Step 3: Define `BookingForm`

In `forms.py`, define a `BookingForm` class based on `forms.ModelForm`, with an inner `Meta` class declaring:

- `model = Booking`
- `fields = "__all__"`

```python
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
```

### Step 4: Run the migrations

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

> Note: make sure the correct MySQL user has been created with the right privileges, and the database is configured to match, before running migrations -- see the previous lab for those steps.

### Step 5: Review `views.py` and enable the `book` view

Open `views.py` and look at the views already defined for the Little Lemon website (added using plain Django). Uncomment the `book()` view function and the `from .forms import BookingForm` import. `book()` accepts the values submitted through the form rendered on `book.html`.

> Note: the necessary imports are already in place.

### Step 6: Add the `bookings()` view

Add a `bookings()` view function, taking `request` as its argument, implementing the following:

- `date = request.GET.get('date', datetime.today().date())`
- `bookings = Booking.objects.all()`
- `booking_json = serializers.serialize('json', bookings)`
- `return render(request, 'bookings.html', {'bookings': booking_json})`

```python
def bookings(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})
```

Save `views.py` and check for errors.

### Step 7: Wire up the URLs

In the app-level `urls.py`, uncomment the URL configuration for the `bookings` and `book` views.

### Step 8: Add a heading to `book.html`

In `templates/book.html`, add an `<h1>` reading "Make a reservation".

### Step 9: Add JavaScript to `book.html`

Inside the `<script>` tags in `book.html`:

- `console.log("Hello")`.
- Get the element with id `id_reservation_date` via `document.getElementById()`, and set its `type` attribute to `"date"`.

```html
<script>
  console.log("Hello");
  document.getElementById("id_reservation_date").type = "date";
</script>
```

### Step 10: Add a heading to `bookings.html`

In `templates/bookings.html`, add an `<h1>` reading "All Reservations".

### Step 11: Add JavaScript to `bookings.html`

Inside the `<script>` tags in `bookings.html`:

- `const bookings = JSON.parse('{{ bookings|safe }}')`.
- `console.log(bookings)`.
- `const pretty_json = JSON.stringify(bookings, null, 2)`.
- Render `pretty_json` into the page (e.g. into the `<pre id="bookings">` element already in the template) so the reservations are actually visible.

```html
<script>
  const bookings = JSON.parse('{{ bookings|safe }}');
  console.log(bookings);
  const pretty_json = JSON.stringify(bookings, null, 2);
  document.getElementById('bookings').textContent = pretty_json;
</script>
```

Save `bookings.html` and check for errors.

### Step 12: Link to the booking page from the home page

In `index.html`, replace `<!-- Add code here for book -->` with:

```html
<a href="{% url 'book' %}">Book your table now</a>
```

### Step 13: Add navigation links

In `templates/partials/_header.html`, replace the two placeholder comments with:

```html
<li><a href="{% url 'book' %}">Book</a></li>
<li><a href="{% url 'bookings' %}">Reservations</a></li>
```

### Step 14: Run the server

```bash
uv run python manage.py runserver
```

Visit the local URL.

### Step 15: Submit some bookings

Go to the Book tab and add three entries via the form.

### Step 16: Verify the reservations

Go to the Reservations tab and confirm the entries appear -- this is the same data now stored in the Little Lemon MySQL database, which can also be verified there directly.

## Conclusion

This completes part two of the final assessment: simple form processing with Django, adding/modifying model data, and converting it into JSON, a more web-friendly format. Part three builds on this with JavaScript for a richer booking experience.
