# Django Permissions & Postgresql
Author: Sarah Hudaib

# Challenge
- Add JWT Authentication to your API.
Install needed libraries in project configuration and/or site settings.

- Keep any pre-existing authentication so DRF Browsable API still usable.
Install needed libraries in project configuration and/or site settings.

# Architecture
- Python 3.9.5 
- Django 4.0.4
- Docker 20.10.12
- Django REST Framework 3.13.1
- Docker Compose 1.25.0-1
- Django REST Framework-SimpleJWT 5.2.0


# Try it out by installing the requirements. (Works only with python >= 3.8, due to Django 4)
```
# Djang
poetry new example-lab
cd example-lab
rm -r exampl-lab tests
mv README.rst README.md
poetry install
poetry add django djangorestframework djangorestframework-simplejwt
poetry shell

django-admin startproject config .   (OR)
django-admin startproject myproject

code .

python manage.py migrate
python manage.py createsuperuser

# requirements
$ poetry export -f requirements.txt --output requirements.txt

```
install docker
```
poetry add psycopg2-binary

poetry export -f requirements.txt --output requirements.txt

docker-compose up --build

docker-compose --version
docker-compose build ---> to build it up
docker-compose up --> to open db
docker-compose down --> to close the db


docker-compose up -d --> will make the db open even tho its not in terminal

docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser

(docker-compose down) every time i type it it will be deleted and i had to run migration again so to avoide it i need to close it and open it using

docker-compose stop 
docker-compose start
```

# Run the Project
Open Console in Main Project Directory.

```
$ git clone git@github.com:sarahhudaib/Django-JWT-Auth.git
$ cd Django-JWT-Auth
$ python manage.py runserver
on your browser http://127.0.0.1:8000
```
