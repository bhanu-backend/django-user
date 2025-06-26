from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserCustomForm,UserLoginForm
from django.contrib.auth import login,logout,authenticate
from .models import Product

# 'cart': {'ref1':22 }
def select_category(request):
     return render(request,"auth1/category.html")

def category_chosen(request,num=None):
     if request.session.get('cart') == None :
              request.session['cart'] = {}
     if num== 1:
          data = Product.objects.filter(category ='Refrigerator')
     elif num==2:
          data = Product.objects.filter(category ='AC')
     return render(request,"auth1/add.html",{'data':data})



# def add_to_cart(request):
#      if request.session.get('cart') == None :
#               request.session['cart'] = {}
#      data = Product.objects.all() 
#      return render(request,"auth1/add.html",{'data':data})

def addproduct(request,id,category):
     if request.method == "POST":
               quantity = int(request.POST.get('quantity'))
               cart = request.session.get('cart')
               if  cart.get(id) :
                     cart[id] = cart[id] + quantity
               else:
                     cart[id] = quantity #updated value
               request.session['cart']=cart # reassign in session
     data = Product.objects.get(pk=id) 
     return render(request,"auth1/add_product.html",{'data':data})

def mycart(request):
      cart = request.session.get('cart')
      #{'cart': {'1': 5, '5': 4}
      lis= []
      for i in cart :
            lis.append(Product.objects.get(pk=int(i)))
      return render(request,"auth1/add_to_cart.html",{'data':lis})





def sign_up(request):
    request.session['cart'] = ""
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







# def add_cart(req):
#      if req.method=="POST":
#           n=req.POST.get('name')
#           q=req.POST.get('quantity')
#           cart=req.session.get('cart','')
#           cart[n]=q
#           req.session['cart'] = cart
#      return redirect('sig')



