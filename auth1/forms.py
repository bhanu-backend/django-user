
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms


class UserCustomForm(UserCreationForm):
    class Meta :
        model = User
        #fields = "__all__"
        fields = ['first_name','last_name','email','username',]

class UserLoginForm(AuthenticationForm):
    pass
