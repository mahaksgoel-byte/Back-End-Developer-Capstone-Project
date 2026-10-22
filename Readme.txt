Little Lemon Web Application — Back-End Developer Capstone
===========================================================

This Django project serves a small restaurant website and provides menu,
table-booking, registration, and token-authentication APIs. MySQL is the
configured database backend. There is deliberately no SQLite fallback.

Prerequisites
-------------
- Python 3.10 or newer
- MySQL 8.x (server running and reachable)
- A MySQL database and user with privileges to create and alter tables

Install
-------
From the project directory, create and activate a virtual environment:

  py -m venv .venv
  .venv\Scripts\activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt

On Linux/macOS use `python3 -m venv .venv` and `source .venv/bin/activate`.
The mysqlclient package may need the platform's MySQL client development
libraries and compiler.

MySQL and secrets
-----------------
Create the database (example):

  CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  CREATE USER 'littlelemon'@'localhost' IDENTIFIED BY 'choose-a-local-password';
  GRANT ALL PRIVILEGES ON littlelemon.* TO 'littlelemon'@'localhost';

Set these environment variables in the shell before running Django:

  MYSQL_DATABASE=littlelemon
  MYSQL_USER=littlelemon
  MYSQL_PASSWORD=your-local-password
  MYSQL_HOST=127.0.0.1
  MYSQL_PORT=3306
  DJANGO_SECRET_KEY=a-long-random-private-value
  DJANGO_DEBUG=true
  DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

PowerShell example (values apply only to the current shell):

  $env:MYSQL_DATABASE='littlelemon'
  $env:MYSQL_USER='littlelemon'
  $env:MYSQL_PASSWORD='your-local-password'
  $env:MYSQL_HOST='127.0.0.1'
  $env:MYSQL_PORT='3306'
  $env:DJANGO_SECRET_KEY='set-a-private-random-value'

Do not commit passwords, tokens, or a local .env file. In deployment, set
DJANGO_DEBUG=false and use a private randomly generated secret key.

Migrations and server
---------------------
  python manage.py check
  python manage.py makemigrations restaurant
  python manage.py migrate
  python manage.py runserver

Website: http://127.0.0.1:8000/
Django admin: http://127.0.0.1:8000/admin/

API routes
----------
Menu (public GET; authenticated writes):
  GET, POST       /api/menu/
  GET, PUT, PATCH, DELETE /api/menu/{id}/

Bookings (all methods require a token; users see only their bookings):
  GET, POST       /api/bookings/
  GET, PUT, PATCH, DELETE /api/bookings/{id}/

Registration and authentication:
  POST            /api/registration/
  POST            /api/token/login/

Insomnia walkthrough
--------------------
1. Send POST http://127.0.0.1:8000/api/registration/ with JSON:
   {"username":"reviewer","password":"A-Strong-Password-42!"}
   Expected: 201 Created and an id/username response; password is omitted.
2. Send POST http://127.0.0.1:8000/api/token/login/ with the same JSON.
   Expected: 200 OK and {"token":"..."}. Invalid credentials return 400.
3. Create an Insomnia Bearer/Token header using `Token <token>` as the
   Authorization value. Menu GET is public; menu writes require this header.
   Example POST /api/menu/ JSON:
   {"title":"Bruschetta","price":"8.50","category":"Starters"}
   Expected: 201 Created with the saved menu item.
4. With the token, POST /api/bookings/ JSON:
   {"name":"Ada","no_of_guests":2,"booking_date":"2030-06-20","booking_time":"18:30:00"}
   Expected: 201 Created. A past date, invalid guest count, or occupied
   date/time returns 400. Unauthenticated booking requests return 401.
5. Use the returned `id` for item/booking detail GET, PUT, PATCH, or DELETE.
   Deletes return 204 No Content; missing IDs return 404. Booking list and
   detail responses are restricted to the authenticated owner.

Tests
-----
  python manage.py test

Tests use Django's configured MySQL database and need a working MySQL
server and credentials. They cover the home page, public/protected menu
operations, registration, token login, booking validation, and persistence.

Git
---
The project source and this documentation belong in the Git repository.
The .gitignore excludes virtual environments, caches, local database files,
and .env secrets. Review `git status` before staging or committing.
