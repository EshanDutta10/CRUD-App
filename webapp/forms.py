from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #default django form to create users and authenticate while logging in 
from django.contrib.auth.models import User


from django import forms
from django.forms.widgets import PasswordInput, TextInput

# creating a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# log in by user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
