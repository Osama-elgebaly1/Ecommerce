from django.contrib import admin
from .models import ShippingAddress,Order,OrderItem
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

# create an order item inline

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0
    

# extend our order model 
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ['date_ordered']
    inlines = [OrderItemInline]


admin.site.unregister(Order)
admin.site.register(Order,OrderAdmin)