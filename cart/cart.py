

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


        


