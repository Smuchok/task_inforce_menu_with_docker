from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterEmployeeForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RegisterEmployeeForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    name = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    addrress = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'addrress')


class LoginEmployeeForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())
