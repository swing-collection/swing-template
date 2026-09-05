# Demo Project

This is a demo Django project designed to exercise reusable Django apps
built from this template. The project provides a simple environment to
experiment with the app you build under `src/`.

---

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/swing-collection/swing-template.git
cd swing-template
cd demo
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If you are using poetry, install the dependencies using:

```bash
poetry install
```

## Usage

### 1. Apply Migrations

Run the following command to set up the database:

```bash
python manage.py migrate
```

### 2. Create a Superuser (Optional)

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

### 3. Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

Access the project in your web browser at `http://127.0.0.1:8000/`.

## Project Structure

```bash
demo/
├── demo/
│   ├── __init__.py        # Project package initialization
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL configuration
│   ├── wsgi.py            # WSGI entry point
├── manage.py              # Django CLI entry point
├── db.sqlite3             # SQLite database file
├── README.md              # This README file
└── requirements.txt       # Python dependencies
```

## Features

- Django Admin: Access the admin interface at /admin/.
- Add routes for the reusable app you build under `src/` in `demo/urls.py`.
