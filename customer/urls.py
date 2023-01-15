from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [

    path ('loginss',views.loginss,name='loginss'),
    path ('index',views.index,name='inte'),
    path('',views.main,name='main'),
    path('iphone_products',views.products_iphone,name="iphone_products"),
    path('mac_products',views.products_mac,name="mac_products"),
    path('ipad_products',views.products_ipad,name="ipad_products"),
    path('watch_products',views.products_watch,name="watch_products"),
    path('loggedin_iphone_products',views.loggedin_products_iphone,name="loggedin_iphone_products"),
    path('loggedin_mac_products',views.loggedin_products_mac,name="loggedin_mac_products"),
    path('loggedin_ipad_products',views.loggedin_products_ipad,name="loggedin_ipad_products"),
    path('loggedin_watch_products',views.loggedin_products_watch,name="loggedin_watch_products"),
    path('cart',views.cart,name="cart"),
    path('add_to_cart',views.add_to_cart,name="add_to_cart"),
    path('home',views.new,name='home'),
    path('phones',views.phones,name='phon'),
    path('logout',views.logout,name='logout'),
    path('remove_product/<int:i>',views.remove_product,name='remove_product'),
    path('checkout',views.checkout,name='checkout'),
    path('my_orders',views.myorders,name='my_orders'),




]













