from rest_framework import serializers
from .models import Employee, Restaurant, Menu
from rest_framework_simplejwt.tokens import RefreshToken


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
            'day',
            'menu'
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


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model=Employee
        fields=(
            'username',
            'password',
        )

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            raise serializers.ValidationError('Username and password are required.')

        user = Employee.objects.filter(username=username).first()
        
        # if there is user
        if user:
            actual_password = user.password
        else:
            raise serializers.ValidationError('Invalid username')

        # if user is None or not user.check_password(password):
        if password != actual_password:
            raise serializers.ValidationError('Invalid password.')

        refresh = RefreshToken.for_user(user)
        data['tokens'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return data
