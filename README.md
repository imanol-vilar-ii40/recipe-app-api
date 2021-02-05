# recipe-app-api

Recipe app api source code

- docker build .
- docker-compose build
- docker-compose run app sh -c "django-admin.py startproject app ."
- docker-compose run app sh -c "python manage.py createsuperuser"
- docker-compose run --rm app sh -c "python manage.py startapp user"
- docker-compose run --rm app sh -c "python manage.py test && flake8"
