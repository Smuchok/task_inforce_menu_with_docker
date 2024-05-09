from django.test import TestCase
from .models import Employee, Restaurant, Menu

# Create your tests here.
# class EmployeeTestCase(TestCase):
#     def setUp(self):
#         e1 = Employee.objects.create(username="user_1", password='1234', email='e1@email.com')
#         e2 = Employee.objects.create(username="user_2", password='1234', email='e2@email.com')
#         e3 = Employee.objects.create(username="user_3", password='1234', email='e3@email.com')
#         e4 = Employee.objects.create(username="user_4", password='1234', email='e4@email.com')


# class RestaurantTestCase(TestCase):
#     def setUp(self):
#         r1 = Restaurant.objects.create(username="res_1", password='1234', email='r1@email.com')
#         r2 = Restaurant.objects.create(username="res_2", password='1234', email='r2@email.com')
#         r3 = Restaurant.objects.create(username="res_3", password='1234', email='r3@email.com')


class MenuTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(username="user_1", password='1234', email='e1@email.com')
        Employee.objects.create(username="user_2", password='1234', email='e2@email.com')
        Employee.objects.create(username="user_3", password='1234', email='e3@email.com')
        Employee.objects.create(username="user_4", password='1234', email='e4@email.com')

        Restaurant.objects.create(username="res_1", password='1234', name='res 1', addrress='address 1')
        Restaurant.objects.create(username="res_2", password='1234', name='res 2', addrress='address 2')

    def test_create_menus(self):
        r1 = Restaurant.objects.get(username='res_1')
        r2 = Restaurant.objects.get(username='res_2')

        Menu.objects.create(title="menu name 1", price=110.99, restaurant=r1, menu={'menu': 'some json staff day 1 r1'}, day=1)
        Menu.objects.create(title="menu name 2", price=120.99, restaurant=r2, menu={'menu': 'some json staff day 1 r2'}, day=1)
        Menu.objects.create(title="menu name 3", price=210.99, restaurant=r1, menu={'menu': 'some json staff day 2 r1'}, day=2)
        Menu.objects.create(title="menu name 4", price=220.99, restaurant=r2, menu={'menu': 'some json staff day 2 r2'}, day=2)


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

