from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Product,Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request,'pages/index.html',{'products':products,
                                              'categories':categories})

def about(request):
    categories = Category.objects.all()
    return render(request,'pages/about.html',{'categories':categories})


def register(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        # fitching data
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # checking if username is unique 
        if User.objects.filter(username=username).exists():
            username_error = 'This username is already taken.'
            return render(request,'pages/register.html',{'error':username_error,
                                                         'username':username,
                                                         'categories':categories})
        else:
            # registering 
            new_user = User.objects.create_user(username=username,
                                                password=password,
                                                email=email)
            new_user.first_name = firstname
            new_user.last_name = lastname
            new_user.save()
            login(request,user=new_user)
            return redirect('home')
    else:
        return render(request,'pages/register.html',{'categories':categories})


def log(request):
    categories = Category.objects.all()
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user=user)
            return redirect('home')
        else:
            error = "User is not exist"
            return render(request,'pages/login.html',{'error':error,
                                                      'categories':categories})
    else:
        return render(request,'pages/login.html',{'categories':categories})



def out(request):
    categories = Category.objects.all()
    logout(request)
    return redirect('home')



def product(request,pk):
    categories = Category.objects.all()
    product = Product.objects.get(id=pk)
    related_products = Product.objects.filter(category=product.category)[:3]
    return render(request,'pages/product.html',{'product':product,
                                                'products':related_products,
                                                'categories':categories})


def category(request,name):
    categories = Category.objects.all()
    category = Category.objects.get(name=name)
    products = Product.objects.filter(category=category)
    return render(request,'pages/index.html',{'products':products,
                                              'categories':categories})