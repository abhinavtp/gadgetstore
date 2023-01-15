from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .import views
 
urlpatterns = [

    path('admins',views.admins,name='admins'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('review',views.review,name='revi'),
    path('',views.login,name='login'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('customer_details',views.customer_details,name='customer_details'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),





]


