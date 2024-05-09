
# Inforce Menu Test Task

A company needs internal service for its 'employees which helps them to
make a decision at the lunch place. Each restaurant will be uploading menus
using the system every day over API.

That is my solution

### Dependences

| Pip library            | Version     |
| :--------------------| :------- |
|asgiref               | 3.8.1 |
|Django                | 5.0.6 |
|django-rest-framework | 0.1.0 |
|djangorestframework   | 3.15.1 |
|pip                   | 24.0 |
|psycopg2              | 2.9.9 |
|psycopg2-binary       | 2.9.9 | 
|sqlparse              | 0.5.0 |
|tzdata                | 2024.1 |

#### pip install
```pip
pip install django, djangorestframework, psycopg2, psycopg2-binary 
```

## Project structure
Project name is `inforce_menus`, app name is `menus`

```bash
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

How to run
```cmd
py manage.py runserver
```

How to run tests
```cmd
py manage.py test
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
| `day`      | `int` | **Required**. Day identificator |

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
| :-------- | :------- | :-------------------------------- |
| `title`      | `int` | Title name of new menu |
| `price`      | `float` | Price of menu |
| `restaurant`      | `int` | Restaurant id. Foreign key |
| `menu`      | `json` | Some menu staff in JSON format |
| `day`      | `int` | Day identificator |


### Add new menu

```http
  POST /new_menu/
```

POST method include JSON
| JSON Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `int` | **Required**. Title name of new menu |
| `price`      | `float` | **Required**. Price of menu |
| `restaurant`      | `int` | **Required**. Restaurant id. Foreign key |
| `menu`      | `json` | **Required**. Some menu staff in JSON format |
| `day`      | `int` | **Required**. Day identificator |


### Others requests

#### Login user
```http
  POST /login/
```
Login employee. If username and password are valid, do logining
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `str` | Username of employee |
| `password`      | `str` | Password to account |

#### Show all restaurants
```http
  GET /employees/
```
Returns all employees is JSON format
| JSON Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `str` | Username of employee |
| `password`      | `str` | Password to account |
| `email`      | `str` | Email of employee |


#### Show all employees
```http
  GET /ress/
```
Returns all restaurants is JSON format
| JSON Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `str` | Username of restaurant's administator |
| `password`      | `str` | Password to account |
| `name`      | `str` | Restaurant's name |
| `addrress`      | `str` | Restaurant's addrress |


## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

