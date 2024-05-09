from rest_framework import serializers
from .models import Employee, Restaurant, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=(
            'title',
            'price',
            'restaurant',
            'menu',
            'day'
        )


class MenuByDaySerializer(serializers.BaseSerializer):
    class Meta:
        fields = (
            'day'
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=(
            'username',
            'password',
            'email'
        )


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields=(
            'username',
            'password',
            'name',
            'addrress'
        )


#Serializer to Register Employee
class RegisterEmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        # validators=[UniqueValidator(queryset=Employee.objects.all())]
    )
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password = serializers.CharField(write_only=True, required=True)
  
    class Meta:
        model = Employee
        fields = ('username', 'password', 'email')

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})
    #     return attrs
    
    def create(self, validated_data):
        user = Employee.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class LoginSerializers(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
