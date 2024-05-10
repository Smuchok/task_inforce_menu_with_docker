from django.test import TestCase
from .models import Employee, Restaurant, Menu
from rest_framework.test import APIClient

from rest_framework import status
from django.urls import reverse
from .serializer import MenuSerializer, MenuByDaySerializer  # Assuming serializer imports


class MenuTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(username="user_1", password='1234', email='e1@email.com')
        Employee.objects.create(username="user_2", password='1234', email='e2@email.com')
        Employee.objects.create(username="user_3", password='1234', email='e3@email.com')
        Employee.objects.create(username="user_4", password='1234', email='e4@email.com')

        Restaurant.objects.create(username="res_1", password='1234', name='res 1', addrress='address 1')
        Restaurant.objects.create(username="res_2", password='1234', name='res 2', addrress='address 2')

        self.valid_day = '2'          # valid day parameter
        self.invalid_day = '123'    # invalid day parameter


    def test_create_menus(self):
        """
        Test add new menus
        """ 
        r1 = Restaurant.objects.get(username='res_1')
        r2 = Restaurant.objects.get(username='res_2')

        Menu.objects.create(title="menu name 1", price=110.99, restaurant=r1, menu={'menu': 'some json staff day 1 r1'}, day=1)
        Menu.objects.create(title="menu name 2", price=120.99, restaurant=r2, menu={'menu': 'some json staff day 1 r2'}, day=1)
        Menu.objects.create(title="menu name 3", price=210.99, restaurant=r1, menu={'menu': 'some json staff day 2 r1'}, day=2)
        Menu.objects.create(title="menu name 4", price=220.99, restaurant=r2, menu={'menu': 'some json staff day 2 r2'}, day=2)

    def test_get_menus_by_day(self):
        """
        Test get menus list by a specific day
        """
        response = self.client.get('/menus/'+self.valid_day, follow=True)
        self.assertEqual(response.status_code, 200)


class UserLoginAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'user_5'
        self.password = '1234'
        self.user = Employee.objects.create(username=self.username, password=self.password, email='test@test.com')

    def test_user_login(self):
        """
        Test login user
        """
        data = {
            'username': self.username,
            'password': self.password
        }

        # Make a POST request to the login API
        response = self.client.post('/login/', data, format='json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the 'refresh' and 'access' tokens
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)


    def test_invalid_password(self):
        """
        Test login user by invalid password
        """
        data = {
            'username': self.username,
            'password': 'wrong password'
        }

        # Make a POST request to the login API
        response = self.client.post('/login/', data, format='json')

        # Check if the response status code is 400
        self.assertEqual(response.status_code, 400)



# # TESTING IN SHELL
# from menus.models import *
# js = []
# js.append(Employee(username="user_1", password='1234', email='e1@email.com'))
# js.append(Employee(username="user_2", password='1234', email='e2@email.com'))
# js.append(Employee(username="user_3", password='1234', email='e3@email.com'))
# js.append(Employee(username="user_4", password='1234', email='e4@email.com'))

# js.append(Restaurant(username="res_1", password='1234', name='res 1', addrress='address 1'))
# js.append(Restaurant(username="res_2", password='1234', name='res 2', addrress='address 2'))
# [j.save() for j in js]


# r1 = Restaurant.objects.get(username='res_1')
# r2 = Restaurant.objects.get(username='res_2')

# js = []
# js.append(Menu(title="menu name 1", price=110.99, restaurant=r1, menu={'menu': 'some json staff day 1 r1'}, day=1))
# js.append(Menu(title="menu name 2", price=120.99, restaurant=r2, menu={'menu': 'some json staff day 1 r2'}, day=1))
# js.append(Menu(title="menu name 3", price=210.99, restaurant=r1, menu={'menu': 'some json staff day 2 r1'}, day=2))
# js.append(Menu(title="menu name 4", price=220.99, restaurant=r2, menu={'menu': 'some json staff day 2 r2'}, day=2))
# [j.save() for j in js]
