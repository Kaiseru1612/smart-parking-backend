release: python3 manage.py migrate
web: python website/manage.py runserver 0.0.0.0:8080
web: gunicorn parking_project.wsgi --log-file