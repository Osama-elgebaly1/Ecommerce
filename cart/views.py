from django.shortcuts import render , get_object_or_404
from ecommerce.models import Category
from .cart import Cart
from ecommerce.models import Product
from django.http import JsonResponse
# Create your views here.

def summary(request):
    cart = Cart(request)
    products = cart.get_prods
    return render(request,'cart.html',{
                                       'products':products})




def add(request):
    # Get the cart
    cart = Cart(request)
    #  test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product)
        # get cart qty
        cart_quantity = cart.__len__()
        # return response 
        # response = JsonResponse({'product name :':product.name})
        response = JsonResponse({'qty':cart_quantity})
        return response

    



def update(request):
    pass



def delete(request):
    pass


