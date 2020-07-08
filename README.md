![Django CI](https://github.com/CodeAndCoffee55/hollow-website/workflows/Django%20CI/badge.svg?branch=develop)
# Hollow's website (created by Code & Coffee 55)

GitHub repository for Hollow's website. This repository contains all files needed to see and integrate the original website with the functions discussed during the initial phase of the project. 
The project is currently in development.

## Getting Started

### Prerequisites 


1. [`Django 3.0.8`](https://docs.djangoproject.com/en/3.0/releases/2.2.10/)
2. [`Python 3.8.3`](https://www.python.org/downloads/release/python-374/)
3. (Not fixed yet) [`PostgreSQL 12`](https://www.postgresql.org/download/)
3. For others requirements, see `requirements.txt`

## Run the project

Clone  the project on your machine and change the directory : 
```bash
$ git clone git@github.com:CodeAndCoffee55/hollow-website.git
$ cd intranet/
```
[Create](https://www.guru99.com/postgresql-create-database.html) the database:
- Open the SQL Shell (psql)
- Press enter five times to connect to the DB

```bash
$ CREATE DATABASE hollow;
```

Migrate the database: 

```bash
$ python manage.py makemigrations website 

$ python manage.py migrate --noinput
```

Create an admin user (for tests, we recommend ``admin@admin.com`` with password ``admin``) 

```bash
$ python manage.py createsuperuser
```

Run the app in a Django server: 

```bash
$ python manage.py runserver
```

Now you should see the app by taping http://127.0.0.1:8000 in your web browser (we will use ``Chrome``). 


When you're done, don't forget to exit the server by : 

```bash
Quit the server with CTRL-BREAK
(In Windows) Ctrl + C
```

## Functions
See the GitHub project for the features included in the version 1.0 of the website.

## To go further
To go further into the project, consult the [project documentation](https://github.com/CodeAndCoffee55/hollow-docs) (in Portuguese).

## Authors
- Matheus Elyasha LOPES
