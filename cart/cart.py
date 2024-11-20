from ecommerce.models import Product

class Cart():
    def __init__(self,request):
        self.session = request.session

        # if new user , there is no  session key , let's create one
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}

        cart = self.session.get('session_key')

        self.cart = cart

    def add(self,product):
        product_id = str(product.id)

        if product.id in self.cart:
            pass

        else:
            self.cart[product_id] = {'price':str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get ids from cart 
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids) 
        return products

        


