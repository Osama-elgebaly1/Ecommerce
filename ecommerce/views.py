from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request,'pages/index.html',{'products':products})

def about(request):
    return render(request,'pages/about.html',{})


def register(request):
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
                                                         'username':username})
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
        return render(request,'pages/register.html',{})


def log(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user=user)
            return redirect('home')
        else:
            error = "User is not exist"
            return render(request,'pages/login.html',{'error':error})
    else:
        return render(request,'pages/login.html',{})



def out(request):
    logout(request)
    return redirect('home')
