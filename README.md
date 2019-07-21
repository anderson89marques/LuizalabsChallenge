# Luizalabs challenge

Challenge for hiring at Luizalabs company.

## Tools and main libraries used for this challenge

```
Linux, Notebook samsung i5, VSCode(IDE), python 3.7.3, django, 
django-rest-framework, pylint, isort, autopep8, python-decouple
```

## How Test and Run the project

- Clone repository
```console
git clone https://github.com/anderson89marques/LuizalabsChallenge.git
```
- Change directory into your newly created project.
```console
cd LuizalabsChallenge
```

- Create a Python virtual environment. (I use pyenv, so here 'python' is a link for python 3)
```console
python -m venv .venv
```

- Activate virtual environment.
```console
source .venv/bin/activate
```

- Install project requirements.
```console
pip install -r requirements.txt
```

- Configure the database.
```console
python manage.py makemigrations
python manage.py migrate
```

- Create a user to access admin panel and to get token to acess API
```console
python manage.py createsuperuser
```

- Run project's tests.
```console
python manage.py test
```

- Run collectstatic.
```console
python manage.py collectstatic
```

- Run your project.
```console
python manage.py runserver
```

## Admin Pages

Application has a admin panel to manage employee data:

* `/admin/`

## API Routes
Employees' data can be created, retrieved or destroyed at API:

* `/api/api-token-auth/` - to get token access
* `/api/employee/` - to list and create employees
* `/api/employee/<int:pk>/` - to delete and retrieve a employee

# Authentication and Requests API examples
To Access the API you need create a user and then
make a POST request to ```/api/api-token-auth/```.

Get token example:
```console
curl -d '{"username": "user_name_here", "password":"passwd_here_"}' -v \
-H "Content-Type: application/json" \
-X POST  http://127.0.0.1:8000/api/api-token-auth/
```

The response body is the token associated with this particular user. Use this token to make the future requests.

Get employees example:
```console
curl -v \
-H "Content-Type: application/json" \
-H "Authorization: Token <token_here>" \
-X GET  http://127.0.0.1:8000/api/employee/
```

Create employee example:
```console
curl -d '{"name": "luiza", "email":"luiza@gmail.com","department": "payments","phone": "(11) 99774-5654"}' -v \
-H "Content-Type: application/json" \
-H "Authorization: Token <token_here>" \
-X POST http://127.0.0.1:8000/api/employee/
```

Delete employee example:
```console
curl -v \
-H "Content-Type: application/json" \
-H "Authorization: Token <token_here>" \
-X DELETE  http://127.0.0.1:8000/api/employee/<pk_here>
```

Retrieve employee example:
```console
curl -v \
-H "Content-Type: application/json" \
-H "Authorization: Token <token_here>" \
-X GET http://127.0.0.1:8000/api/employee/<pk_here>


### Optional Configuration
This project use python-decouple. 
To change debug mode, secret_key and database url you can create environment variables or
create a .env file inside the repo like the example below.

Example:
```
SECRET_KEY=<you secret here>
DEBUG=True # default is False
DATABASE_URL=<your-database-url> # default is sqlite3
```

## Thanks of the Author 

Thanks for the oportunity.
I enjoyed a lot and i will be very happy if i can work with you guys.

Att,
