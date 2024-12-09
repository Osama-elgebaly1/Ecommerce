from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import ShippingForm,ShippingAddress,PaymentForm
from django.contrib import messages
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




def billing_info(request):
        if request.POST:
            cart = Cart(request)
            products = cart.get_prods
            quantities = cart.get_quants
            total = cart.total()
            
            shipping_form = request.POST
            if request.user.is_authenticated:
                billing_form = PaymentForm()


                return render(request,'payment/billing_info.html',{
                                                'products':products,
                                                'quantities':quantities,
                                                'total':total,
                                                'shipping_info':shipping_form,
                                                'billing_form':billing_form
                                                })
            

            else:
                billing_form = PaymentForm()
                return render(request,'payment/billing_info.html',{
                                                'products':products,
                                                'quantities':quantities,
                                                'total':total,
                                                'shipping_info':shipping_form,
                                                'billing_form':billing_form

                                                })
                 
            
                 
        else:
             messages.success(request,'Access Denied ')
             return redirect('home')


