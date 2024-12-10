from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import ShippingForm,ShippingAddress,PaymentForm
from django.contrib import messages
from .models import Order , OrderItem
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
            request.session['shipping_info'] = shipping_form
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


def order_success(request):
     if request.POST:
        #   importing cart to get total 
          cart = Cart(request)
          products = cart.get_prods
          quantities = cart.get_quants
          total = cart.total()
        
          

          shipping_info = request.session.get('shipping_info')
          full_name = shipping_info.get('shipping_full_name')
          email = shipping_info.get('shipping_email')

          if request.user.is_authenticated:
               user = request.user
          else:
               user = None
               

        ############## address ########

          address1 = shipping_info.get('shipping_address1')
          address2 = shipping_info.get('shipping_address2')
          city = shipping_info.get('shipping_city')
          state = shipping_info.get('shipping_state')
          country = shipping_info.get('shipping_country')
          full_address = f"{address1} \n {address2} \n {city} \n {state} \n {country} "
        
        #   amount_paid = total
          amount_paid = total

        # creating Order 
          order = Order(user = user ,
                        full_name=full_name,
                        email = email,
                        shipping_address = full_address,
                        amount_paid=amount_paid,
                        )
          order.save()

          # creating order items
          order_id  = order.pk
          for product in products():
              product_id = product.id
              user= user
              if product.price != product.price_after_dis and product.price_after_dis > 0:
                    price = product.price_after_dis
              else:
                    price = product.price

              for key,value in quantities().items():
                   if product.id == int(key):
                        quantity = value
                        order_item = OrderItem(
                                          order_id = order_id,
                                          product_id=product_id,
                                          user=user,
                                          price=price,
                                          quantity=quantity)
                        order_item.save()










          messages.success(request,'Order Placed...')
          return redirect('home')
     else:
          messages.success(request,'Access Denied ')
          return redirect('home')