# Kubera Ledger (Django)
Student expense tracker: daily entries, budget plan, savings goal, friends tracker, yearly 3D graph.

    python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Open http://127.0.0.1:8000/ , click "Create an account", and start adding entries.
Optional: `python manage.py createsuperuser` to use /admin/.
Before deploying online: set DEBUG=False, a new SECRET_KEY and ALLOWED_HOSTS in kubera/settings.py.
