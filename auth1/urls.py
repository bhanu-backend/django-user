

from django.urls import path
from . import views
urlpatterns = [

    path('signup',views.sign_up,name='sign_up'),
    path('login/',views.log_in,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.log_out,name='logout'),
  #  path('home/',views.add_to_cart,name='home'),
    path('chosen/<int:num>/',views.category_chosen,name='chosen'),
     path('',views.select_category,name='category'),
    path('addproduct/<int:id>/',views.addproduct,name='addproduct'),
    path('deleteproduct/<int:id>/',views.deleteproduct,name='deleteproduct'),
    path('add2cart',views.mycart,name='add2cart'),
  
]



   #  path('cart/',views.add_cart,name='cart'),