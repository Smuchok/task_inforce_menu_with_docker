from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from django.core.serializers import serialize
import json

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
    app = Menu.objects.filter(day=day)
    serializer = MenuSerializer(app, many=True)
    return Response(serializer.data)


class CreateEmployeeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class PostMenuAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        # data['restaurant'] = Restaurant.objects.get(id=data['restaraunt']))
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data['tokens'], status=status.HTTP_200_OK)


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
