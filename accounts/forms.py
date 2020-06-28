from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Locations
from .models import Users



class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields =  '__all__'


class LocationsForm(ModelForm):
    class Meta:
        model = Locations
        fields =  '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
