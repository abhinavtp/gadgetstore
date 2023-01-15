from django.shortcuts import render

# Create your views here.
from email.mime import image
from urllib import request
from django.shortcuts import render,redirect
from .models import User,Orders
from admin_panel.models import Products
from django.http import JsonResponse
from decorators import login_check,logout_check
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@logout_check
def loginss(request):
    msg=''
    if request.method == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']

        try:
            login_user = User.objects.get(email = email,psw = psw)
            request.session['userId']=login_user.id
            print(request.session['userId'])
            return redirect('home')
        except:
            msg = 'invalid credential'

    return render(request,'customer/loginss.html',{'status':msg})

def logout(request):
    del request.session['userId']
    return redirect('main')

def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        psw = request.POST['re_pass']
        address = request.POST['address']
        phone = request.POST['phone']

        user_login = User(name = name,email = email,psw = psw,address=address,phone=phone)
        user_login.save()

        return redirect('loginss')
    return render(request,'customer/index.html')    
@logout_check
def main(request):
    return render (request,'customer/main.html')

def products_iphone(request):
    productObj = Products.objects.filter(category="iPhone")

    return render (request,'customer/iphone_products.html',{'data':productObj})


def products_mac(request):
    productObj = Products.objects.filter(category="Mac")

    return render (request,'customer/mac_products.html',{'data':productObj})


def products_ipad(request):
    productObj = Products.objects.filter(category="iPad")

    return render (request,'customer/ipad_products.html',{'data':productObj})



def products_watch(request):
    productObj = Products.objects.filter(category="Watch")

    return render (request,'customer/watch_products.html',{'data':productObj})

def loggedin_products_iphone(request):
    productObj = Products.objects.filter(category="iPhone")

    return render (request,'customer/loggedin_iphone_products.html',{'data':productObj})

@login_check
def loggedin_products_mac(request):
    productObj = Products.objects.filter(category="Mac")

    return render (request,'customer/loggedin_mac_products.html',{'data':productObj})

@login_check
def loggedin_products_ipad(request):
    productObj = Products.objects.filter(category="iPad")

    return render (request,'customer/loggedin_ipad_products.html',{'data':productObj})


@login_check
def loggedin_products_watch(request):
    productObj = Products.objects.filter(category="Watch")

    return render (request,'customer/loggedin_watch_products.html',{'data':productObj})

@login_check
def cart(request):
    orderObj = Orders.objects.filter(user_id = request.session['userId'],status='Not Paid')
    return render (request,'customer/cart.html',{'data':orderObj})

@login_check
def add_to_cart(request,id=0):
    if (request.session.get("userId")):
        print("Hellooo")
        id = request.POST.get('id')
        print(id)
        user_id = request.session.get("userId")
        orderObj = Orders(user_id=user_id, product_id=id,quantity=1,status='Not Paid')
        orderObj.save()
        return JsonResponse({'message':'Added To Cart'})

    else:
        print("Wokkeyyy")



    return render (request,'customer/cart.html')
@login_check
def new(request):
    return render(request,'customer/new.html')
@login_check   
def phones(request):

    return render(request,'customer/phones.html')    

def remove_product(request,i=0):
    Orders.objects.get(id=i).delete()
    return redirect('cart')

@login_check
def checkout(request):
    Orders.objects.filter(status='Not Paid',user_id = request.session['userId']).update(status='Paid')
    return redirect('home')

@login_check
def myorders(request):
    orderObj = Orders.objects.filter(user_id = request.session['userId'],status='Paid')
    return render (request,'customer/myorders.html',{'data':orderObj})


