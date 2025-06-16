
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCustomForm(UserCreationForm):
    class Meta :
        model = User
        #fields = "__all__"
        fields = ['first_name','last_name','email','username',]
