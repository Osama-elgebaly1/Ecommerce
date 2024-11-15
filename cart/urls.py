from django.urls import path
from . import views
urlpatterns = [
    path('',views.summary,name='cart_summary'),
    path('add/',views.add,name='cart_add'),
    path('update/',views.update,name='cart_update'),
    path('delete/',views.delete,name='cart_delete'),
]

