from django.shortcuts import render
from ecommerce.models import Category
# Create your views here.

def summary(request):
    categories = Category.objects.all()
    return render(request,'cart.html',{'categories':categories})



def add(request):
    pass



def update(request):
    pass



def delete(request):
    pass


