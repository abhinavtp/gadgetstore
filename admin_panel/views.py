from django.shortcuts import render

# Create your views here.
from email.mime import image
from urllib import request
from django.shortcuts import render,redirect
from admin_panel.models import Products
from customer.models import Orders,User
from .models import admin


# Create your views here.
def admins(request):
    if request.method=="POST":
        brand = request.POST['brand']
        model = request.POST['model']
        price = request.POST['price']
        description = request.POST['description']
        quantity = request.POST['quantity']
        category = request.POST['category']
        prd_img = request.FILES['prd_img']
        productObj = Products(brand=brand, model=model, price=price, description=description, quantity=quantity, category=category,img=prd_img)
        productObj.save()
    return render(request,'admin_panel/admins.html')

def adminpage(request):
    return render(request,'admin_panel/adminpage.html')    
    
def viewproduct(request):
    productObj = Products.objects.all()
    return render (request,'admin_panel/viewproduct.html',{'data':productObj})   

def review(request):
    productObj = Orders.objects.all()
    return render(request,'admin_panel/review.html',{'data':productObj}) 

def login(request):
    msg=''
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']

        try:
            if uname=='abhinav' and upass=='1234':
                request.session['admin_id'] = 1

                return redirect('adminpage')
        except Exception as e:
            print(e)
            msg = 'invalid  credentials'


    return render (request,'admin_panel/login.html',{'error':msg})



def delete_product(request,id=0):
    Products.objects.get(id=id).delete()
    return redirect('viewproduct')


def customer_details(request):
    userObj=User.objects.all()
    return render(request,'admin_panel/customer_details.html',{'data':userObj})


def delete_user(request,id=0):
    User.objects.get(id=id).delete()
    return redirect('customer_details')