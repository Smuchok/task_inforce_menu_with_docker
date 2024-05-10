
# Inforce Menu Test Task

A company needs internal service for its 'employees which helps them to
make a decision at the lunch place. Each restaurant will be uploading menus
using the system every day over API.

That is my solution

I described step by step how to run my project

### Dependences

| Pip library          | Version  |
| :--------------------| :------- |
|asgiref               | 3.8.1 |
|Django                | 5.0.6 |
|django-rest-framework | 0.1.0 |
|djangorestframework   | 3.15.1 |
|djangorestframework-simplejwt   | 5.3.1 |
|pip                   | 24.0 |
|psycopg2              | 2.9.9 |
|psycopg2-binary       | 2.9.9 |
|PyJWT                 | 2.8.0 |
|sqlparse              | 0.5.0 |
|tzdata                | 2024.1 |


#### pip install
```pip
pip install -r requirements.txt
```
or
```pip
pip install django, djangorestframework, psycopg2, psycopg2-binary, djangorestframework-simplejwt
```

## Run
To skip steps 2-3, you can run `init.bat` file instead:
```bash
init.bat
```


### 1. Git Clone
Project name is `inforce_menus`, app name is `menus`
```bash
git clone https://github.com/Smuchok/task_inforce_menu
```

Structure:
```bash
init.bat
inforce_menus_backup.sql
requirements.txt
README.md
inforce_menus
├───inforce_menus
│   ├───settings.py
│   └───urls.py
│   ...
│
├───menus
│   ├───models.py
│   ├───views.py
│   ├───urls.py
│   └───tests.py
│   ...
│
└───manage.py
```

### 2. Venv

Create venv
```bash
python -m venv venv
```



#### pip install
```pip
pip install -r requirements.txt
```


### Database
PostgreSQL 16
You should restore `inforce_menus_backup.sql` file.
And change `NAME` parameter in `settings.py` in order to name of restored database
```python
# settings.py
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inforce_menus',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
...
```

#### Run Server
```bash
py manage.py runserver
```
## API Reference

### Get all menus

```http
  GET /menus/
```

Show all menus from all restaurans and days

### Get menus by a specific day 

```http
  GET /menus/<day>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `day`     | `int`    | **Required**. Day identificator |

This request returns JSON like a:
```json
[
    ...
    {
        "title": "menu name 1",
        "price": 110.99,
        "restaurant": 1,
        "menu": {
            "menu": "some json staff day 1 r1"
        },
        "day": 1
    },
    {
        "title": "menu name 2",
        "price": 120.99,
        "restaurant": 2,
        "menu": {
            "menu": "some json staff day 1 r2"
        },
        "day": 1
    }
    ...
]
```

Structure
| JSON Parameter | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `title`     | `int` | Title name of new menu |
| `price`     | `float` | Price of menu |
| `restaurant`| `int` | Restaurant id. Foreign key |
| `menu`      | `json` | Some menu staff in JSON format |
| `day`       | `int` | Day identificator |


### Add new menu

```http
  POST /new_menu/
```

POST method include JSON. JSON have to looks like:
```json
{
    "title": "menu name 222",
    "price": 222.22,
    "restaurant": 1,
    "menu": {
        "menu": "some json staff 222"
    },
    "day": 3
}
```

| JSON Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `int` | **Required**. Title name of new menu |
| `price`      | `float` | **Required**. Price of menu |
| `restaurant` | `int` | **Required**. Restaurant id. Foreign key |
| `menu`       | `json` | **Required**. Some menu staff in JSON format |
| `day`        | `int` | **Required**. Day identificator |


### Createa employee
```http
  POST /create_employee/
```
Create new employee.

JSON have to looks like:
```json
{
    "username": "user_222",
    "password": "1234",
    "email": "e222@email.com"
}
```

| Parameter       | Type     | Description                       |
| :--------       | :------- | :-------------------------------- |
| `username`      | `str`   | Username of employee |
| `password`      | `str`   | Password |
| `email`         | `str`   | Email |

### Login user
```http
  POST /login/
```
Login employee. If username and password are valid, send tokens
| Parameter       | Type     | Description                       |
| :--------       | :------- | :-------------------------------- |
| `username`      | `str`   | Username of employee |
| `password`      | `str`   | Password to account |


### Others requests

#### Show all restaurants
```http
  GET /employees/
```
Returns all employees is JSON format
| JSON Parameter  | Type     | Description                       |
| :--------       | :------- | :-------------------------------- |
| `username`      | `str` | Username of employee |
| `password`      | `str` | Password to account |
| `email`         | `str` | Email of employee |


#### Show all employees
```http
  GET /ress/
```
Returns all restaurants is JSON format
| JSON Parameter  | Type     | Description                       |
| :--------       | :------- | :-------------------------------- |
| `username`      | `str` | Username of restaurant's administator |
| `password`      | `str` | Password to account |
| `name`          | `str` | Restaurant's name |
| `addrress`      | `str` | Restaurant's addrress |


## Running Tests

### to run all tests:
```bash
py manage.py test
```

### Tests description
There are 4 tests in `tests.py`

#### test_user_login
Test login user. Check if the response contains the 'refresh' and 'access' tokens
```bash
py manage.py test menus.tests.UserLoginAPITestCase.test_user_login
```

#### test_invalid_password
Test login user by invalid password. Check if the response status code is 400
```bash
py manage.py test menus.tests.UserLoginAPITestCase.test_invalid_password
```

#### test_create_menus
Check if possible add new menu
```bash
py manage.py test menus.tests.MenuTestCase.test_create_menus
```

#### test_get_menus_by_day
Check if the respone have list of menus by a specific day
```bash
py manage.py test menus.tests.MenuTestCase.test_get_menus_by_day
```
