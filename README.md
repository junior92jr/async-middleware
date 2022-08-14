# Django Rest Framework Project Tier
Async Middleware

# Urls Api

## Installation
This is a Simple Django project, it Only requires to have virtualenv and pip installed.

## Configure packages

### Database
Install Postgresql

## Configure the project
### Create a virtualenv

```
$ python3 -m venv tier
```

This command will create a new folder with the name `tier`

### Clone the project
The repository is public. You can use the ssh or http link to clone the repository
```
$ git clone git@github.com:junior92jr/tier-challenge.git
```

### Activate your enviroment
Inside the `tier` folder run the following command

```
$ source bin/activate
```

After this you will see the virtualenv name in your prompt. i.e.:

```
(tier) $
```

### Install requirements
```
(tier)$ cd tier

(tier)$ pip install -r requirements.txt
```

### Setting up environment variables for project

```
(tier)$ mkidr .env
```
you can use this as an example for your .env file

```
DATABASE_URL=postgres://postgres:postgres@localhost:5432/tier_db
DEBUG=true
SECRET_KEY=secret_key
ALLOWED_HOSTS=*
```

### Run the project

Once you have everything ok, you can run the project.

```
(tier) $ ./manage.py check

(tier) $ ./manage.py migrate

(tier) $ ./manage.py runserver
```

In localhost just go to:

```
(GET) http://127.0.0.1:8000/urls/

(POST) http://127.0.0.1:8000/urls/ 

BODY: {
    "original_url": "www.google.com"
}
```
### Run tests


```
(tier) $ ./manage.py test
```

# Future Improvements

Because time isues I couldn't focus on the Bonus part. But I do have some ideas.

1) A better Error Handling.
2) More Unit Test cases with more Mocks to cover every possible case and error.
