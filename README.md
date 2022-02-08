ibanez is a simple app to manage visitors and their bank account numbers.
Management is restricted to administrator who created entry.

to run this app:

create .env file with following credentials:

SOCIAL_AUTH_PROVIDER=google
SOCIAL_AUTH_NAME=<USERNAME>
SOCIAL_AUTH_ID=<SOCIAL_AUTH_ID>
SOCIAL_AUTH__SECRET_KEY=<SOCIAL_AUTH__SECRET_KEY>
DJANGO_SECRET_KEY=<DJANGO_SECRET_KEY>
DJANGO_DEBUG=True
DATABASE_URL=<DATABASE_URL>
SITE_ID=8

  
to build container:
$docker-compose up --build
$docker exec -t -i <CONTAINER ID> bash
in container console:
$python3 manage.py makemigrations
$python3 manage.py migrate
#to create social account, credentials in .env
$python3 manage.py load_social
$python3 manage.py createsuperuser


Currently users permissions are managed bu superuser
