# The Wall App

The Wall App is a website that allows users to register, login, and write on a wall.

## Features

- Registration / Login: Anonymous users can create a new user and this new user receives a welcome email. New users can then log in. 

- Wall (authed): After logging in, a user can post messages on the site-wide wall, similar to a Facebook wall except there is only one wall for the entire site.

- Wall (guest): Guests as well as authed users can see all of the messages on the wall.


## 	Prerequisites

install pipenv

```json
$ pip install pipenv
```

Activate pipenv

```json
$ pipenv shell| 	
```


## How to run

### Default

You can run the application from the command line with manage.py. Go to the root folder of the application.

Run migrations:

```json
$ python manage.py migrate
```

Run server on port 8000:

```json
$ python manage.py runserver 8000
```

## Docker

It is recommended to run the app using docker:

here you can read more about docker
* Docker Documentation (https://docs.docker.com/)

Build the Docker image:

```json
$ docker-compose up --build
```

