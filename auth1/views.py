from django.shortcuts import render,redirect
from .forms import UserCustomForm,UserLoginForm
from django.contrib.auth import login,logout,authenticate


def sign_up(request):
    if request.method == "POST":
          form = UserCustomForm(request.POST)
          if form.is_valid():
               form.save()
    else:
       form = UserCustomForm()
    return render(request, "auth1/sign_up.html",{'form':form})

def log_in(request):
      if request.method == "POST":
           form = UserLoginForm(request=request,data = request.POST)
           if form.is_valid():
                un= form.cleaned_data.get('username')
                ps= form.cleaned_data.get('password')
                user =authenticate(username = un , password = ps)
                if user is not None :
                     login(request,user)
                     return redirect("profile")
              
           
      else:
           form = UserLoginForm()
      return render(request, "auth1/log_in.html",{'form':form})


def profile(request):
     if request.user.is_authenticated :
         username = request.user
         print(username)
         return render(request, "auth1/profile.html",{'username':username})
     return redirect("login")
     
def log_out(request):
     logout(request)
     return redirect('login')


