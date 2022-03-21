from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .validators import validate_email
from .models import *


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(validators = [validate_email])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']




