from django.shortcuts import render
from cart.cart import Cart
from payment.forms import ShippingForm,ShippingAddress
# Create your views here.

def payment_success(request):
    return render(request,'payment/payment_success.html',{})

def checkout(request):
    cart = Cart(request)
    products = cart.get_prods
    quantities = cart.get_quants
    total = cart.total()
    if request.user.is_authenticated:
        current_user  = ShippingAddress.objects.get(user_id = request.user.id)
        shipping_form = ShippingForm(request.POST or None ,instance=current_user)
    else:
        shipping_form = ShippingForm(request.POST or None)

        

    return render(request,'payment/checkout.html',{
                                       'products':products,
                                       'quantities':quantities,
                                       'total':total,
                                       'shipping_form':shipping_form})

