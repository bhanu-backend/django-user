from django.shortcuts import render
from .forms import UserCustomForm
from django.contrib.auth.forms import UserCreationForm



def sign_up(request):
    if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
    else:
       form = UserCreationForm()
    return render(request, "auth1/sign_up.html",{'form':form})
