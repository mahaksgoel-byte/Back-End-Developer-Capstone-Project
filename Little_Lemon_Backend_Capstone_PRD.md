# PRD --- Little Lemon Web Application (Back-End Developer Capstone)

## 1. Project Overview

**Project name:** Little Lemon Web Application\
**Project type:** Django web application with REST APIs\
**Course:** Meta Back-End Developer Professional Certificate ---
Back-End Developer Capstone

Build a Django application that serves static HTML content, connects to
a MySQL database, exposes menu and table-booking APIs, supports user
registration and authentication, includes unit tests, and can be tested
using Insomnia REST Client.

This is a separate capstone project. Do not merge it with the standalone
Little Lemon Booking System or the Little Lemon API menu/cart/order
peer-graded project.

## 2. Goals

-   Serve the Little Lemon restaurant website through Django.
-   Store application data in MySQL.
-   Implement menu and table-booking REST API endpoints.
-   Support user registration and authentication.
-   Include meaningful unit tests.
-   Make APIs testable through Insomnia.
-   Document API paths in the required README file for peer reviewers.
-   Preserve the existing Git repository and prepare the project for
    Coursera peer review.

## 3. User Roles

### Anonymous visitor

-   Browse the restaurant website and public menu data.
-   Register and authenticate.

### Registered user

-   Authenticate using the project's configured mechanism.
-   Access protected endpoints according to permissions.
-   Create or manage bookings where permitted.

### Peer reviewer

-   Follow README setup instructions.
-   Test documented endpoints in Insomnia.
-   Verify responses, validation, authentication, and database
    persistence.
-   Run the test suite.

## 4. Functional Requirements

### 4.1 Django website and static content

-   Use Django to serve the supplied Little Lemon website and static
    HTML content.
-   Preserve existing templates, pages, and starter structure where
    possible.
-   Configure static files correctly for local development.
-   Ensure main routes load without template or static-file errors.

### 4.2 MySQL database

-   Configure Django to connect to MySQL for the capstone.
-   Use environment variables or an ignored local environment file for
    credentials when practical.
-   Document database setup and migrations.
-   Ensure migrations apply successfully.
-   Do not silently replace MySQL with SQLite if the rubric requires
    MySQL.

### 4.3 Menu API

-   Implement endpoints to read and manage menu items using existing
    route conventions.
-   Support the HTTP methods required by the existing implementation and
    assignment, including GET, POST, PUT/PATCH, and DELETE where
    applicable.
-   Validate input and return appropriate HTTP status codes.
-   Persist changes to the database.
-   Document the actual menu API paths in the README.

### 4.4 Table-booking API

-   Implement endpoints for retrieving and creating table bookings, with
    update/delete operations where required by the project.
-   Store booking records in Django models backed by MySQL.
-   Validate required fields, dates, and time slots.
-   Handle invalid input and nonexistent records with suitable
    responses.
-   Prevent duplicate reservations for the same date/time slot where
    required by the current data model.
-   Document the actual booking API paths.

### 4.5 Registration and authentication

-   Implement user registration and authentication using the mechanism
    expected by the starter project and course.
-   Protect endpoints that require authentication.
-   Return suitable responses to unauthenticated requests.
-   Never expose passwords, password hashes, or secrets in API
    responses.
-   Document how to authenticate in the README.

### 4.6 Unit tests

-   Add or retain tests for models, API endpoints, authentication,
    validation, and database behavior.
-   Include success and failure cases.
-   Document and run the test command.
-   Do not claim tests pass unless they were actually run.

### 4.7 Insomnia compatibility

-   Ensure the documented API endpoints can be tested in Insomnia.
-   Document example HTTP methods, paths, request bodies, and expected
    status codes where useful.
-   Do not rely on frontend-only behavior to satisfy API requirements.

## 5. Data Model Requirements

Inspect the existing starter code first and preserve suitable existing
models and field names.

### Menu item

-   Primary key
-   Name/title
-   Price
-   Category or category reference if supported by the starter project
-   Other fields required by existing course code

### Booking

-   Primary key
-   Guest/customer or user reference where applicable
-   Booking date
-   Booking time/slot
-   Other fields expected by the starter project

### User

-   Use Django's configured user model and authentication approach.
-   Avoid introducing a conflicting custom user model.

Create migrations for required model changes. Do not make unnecessary
schema changes.

## 6. Suggested API Routes

These are examples only. Existing course-provided route names take
precedence.

  ------------------------------------------------------------------------
  Resource                Example route           Purpose
  ----------------------- ----------------------- ------------------------
  Menu                    `/api/menu/` or         Read/manage menu items
                          existing menu route     

  Bookings                `/api/bookings/`        Retrieve/create bookings

  Registration            `/api/registration/`    Register a user if this
                                                  matches the existing
                                                  project

  Authentication          Existing configured     Authenticate users
                          auth/token route        

  Booking detail          `/api/bookings/{id}/`   Retrieve/update/delete a
                                                  booking where
                                                  implemented
  ------------------------------------------------------------------------

Do not create duplicate routes merely to match these examples. Document
the actual routes in the repository.

## 7. Technical Requirements

-   Python and Django.
-   Django REST Framework if required by the existing starter project.
-   MySQL database.
-   Django migrations.
-   Django templates and static files.
-   Django test runner or the project's existing test framework.
-   Insomnia REST Client compatibility.
-   Git repository containing source code and README documentation.

Use the dependency manager already established in the repository. If it
uses Pipenv, preserve its Pipfile/lockfile and document commands such as
`pipenv install`, `pipenv shell`, and Django management commands.

## 8. Quality and Security

-   Follow Django conventions and keep code readable.
-   Use serializers or equivalent validation for API input.
-   Prefer the Django ORM over unsafe raw SQL.
-   Enforce authentication and permissions server-side.
-   Handle missing fields, invalid IDs, malformed requests, and database
    errors appropriately.
-   Do not hard-code credentials or commit secrets.
-   Exclude virtual environments, caches, secret files, and unrelated
    generated artifacts.
-   Keep changes focused on the capstone requirements.

## 9. Acceptance Criteria --- Peer-Grading Rubric

Verify all seven criteria shown in the assignment screenshots:

1.  The web application uses Django to serve static HTML content.
2.  The project has been committed to a Git repository.
3.  The backend connects to a MySQL database.
4.  Menu and table-booking APIs are implemented.
5.  User registration and authentication are implemented.
6.  The application contains unit tests.
7.  The API can be tested using Insomnia REST Client.

Also verify that migrations work, API changes persist in MySQL, and
README documentation lists the API paths reviewers should test.

## 10. Testing Plan

-   Install dependencies in a clean environment.
-   Verify MySQL connectivity.
-   Run `python manage.py check`.
-   Create migrations only when model changes require them, then run
    `python manage.py migrate`.
-   Run `python manage.py test` or the existing test command.
-   Start the server and verify website routes.
-   Test menu APIs in Insomnia.
-   Test booking APIs in Insomnia.
-   Test registration and authentication.
-   Test invalid input and unauthenticated access.
-   Verify database persistence for supported create/update/delete
    operations.

If MySQL is unavailable, state that limitation clearly and do not claim
the MySQL criterion has passed.

## 11. README Requirements

Create or update the README. The assignment specifically mentions
`Readme.txt`; preserve an existing required filename or include that
file if needed.

Include: - Project description and prerequisites. - Dependency
installation instructions. - MySQL setup and environment
configuration. - Migration and server startup commands. - Website
URLs. - Menu API paths. - Booking API paths. -
Registration/authentication paths. - Example requests and expected
responses. - Unit-test command. - Insomnia testing instructions.

## 12. Git and Submission

-   Preserve existing Git history and remote configuration.
-   Check `git status` before staging files.
-   Never commit secrets, `.env` files, virtual environments, caches, or
    local databases containing private data.
-   Do not overwrite or remove an existing remote.
-   Only commit and push when explicitly authorized by the user or
    required by the current task.
-   Ensure the README is committed and pushed with the source when the
    user performs submission.

## 13. Out of Scope

-   The standalone booking-form assignment focused on JavaScript date
    refresh and a JSON reservations page, except where overlapping
    functionality is required here.
-   The separate menu/cart/order API peer-graded assignment.
-   Production hosting, payments, or unrelated features.
-   Unnecessary redesign or replacement of working starter code.

## 14. Definition of Done

The project is ready for peer review when Django serves the website,
MySQL is configured and working, menu and table-booking APIs function,
registration/authentication work, unit tests exist and their actual
results are documented, API paths are listed in the README, and
endpoints can be tested using Insomnia.
