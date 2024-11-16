

class Cart():
    def __init__(self,request):
        self.session = request.session

        # if new user , there is no  session key , let's create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        cart = self.session.get('session_key')

        # make sure cart is available on all pages of the site 


