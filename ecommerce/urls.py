from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    # auth system
    path('register/',views.register,name='register'),
    path('login/',views.log,name='login'),
    path('logout/',views.out,name='logout'),
]
