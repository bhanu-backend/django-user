

from django.urls import path
from . import views
urlpatterns = [

    path('signup',views.sign_up,name='sign_up'),
    path('login/',views.log_in,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.log_out,name='logout'),
    path('',views.add_to_cart,name='home'),
    path('addproduct/<int:id>/<str:category>/',views.addproduct,name='addproduct'),

]



   #  path('cart/',views.add_cart,name='cart'),