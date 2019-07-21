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

- Create a user to access admin panel
```console
python manage.py createsuperuser
```

- Run project's tests.
```console
python manage.py test
```

- Run your project.
```console
python manage.py runserver
```

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


## Admin Pages

Application has a admin panel to manage employee data:

* `/admin/`

## API Routes
Employees' data can be created, retrieved or destroyed at API:

* `/api/employee/`
* `/api/employee/<int:pk>/`

## Thanks of the Author 

Thanks for the oportunity.
I enjoyed a lot and i will be very happy if i can work with you guys.

Att,
