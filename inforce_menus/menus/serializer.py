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
