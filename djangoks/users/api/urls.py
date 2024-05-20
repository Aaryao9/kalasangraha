from .views import *
from django.urls import path

urlpatterns = [
    path('signup/', signupView.as_view(), name='signup'),
    path('login/', loginView.as_view(), name='login'),
    path('profile/', profileView.as_view(), name='profile'),
    path('logout/', logoutView.as_view(), name='logout'),
    
    
    path('product/', productView.as_view(), name='product'),
    path('cart/', cartView.as_view(), name='cart'),
    
    
    path('category/', categoryView.as_view(), name='category'),
   
    path('order/', orderView.as_view(), name='order'),
    path('bestseller/', bestsellerView.as_view(), name='bestseller'),   

]
