from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Employee, Restaurant, Menu
from .serializer import *

from django.contrib.auth import authenticate, login, logout
from .forms import *


def index(request):
    return HttpResponse("Hello World!")


@api_view(['GET'])
def get_menus(request):
    app = Menu.objects.all()
    serializer = MenuSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_menus_by_day(request, day):
    if request.method == 'POST ':
        print('POSTPOST')
        app = Menu.objects.filter(day=2)
        serializer = MenuByDaySerializer(app, many=True)
        return Response(serializer.data)
    
    app = Menu.objects.filter(day=day)
    serializer = MenuSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['GET'])  # get restaurants
def get_ress(request):
    app = Restaurant.objects.all()
    serializer = RestaurantSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_employees(request):
    app = Employee.objects.all()
    serializer = EmployeeSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_menu(request):
    data = request.data.copy()
    # data['restaurant'] = Restaurant.objects.get(id=data['restaraunt']))
    serializer = MenuSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login_user(request):
    form = LoginEmployeeForm # AuthenticationForm
    # import pdb; pdb.set_trace() #debug

    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    
    print(request)
    serializer.is_valid(raise_exception=True)
    serializer = LoginSerializers(data=request.data)
    return Response(serializer.data)
