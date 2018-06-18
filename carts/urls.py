from django.urls import path
from django.conf.urls import url


from .views import (
    cart_home,
    cart_update,
    checkout_home,
)

app_name= 'cart_url'
urlpatterns = [
    path('', cart_home, name='home'),
    url('checkout',checkout_home , name='checkout'),
    url('update',cart_update , name='update'),
    ]