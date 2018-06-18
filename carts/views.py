from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart
from accounts.models import GuestEmail
from billing.models import BillingProfile
from accounts.form import LoginForm, GuestForm
from orders.models import Order

# Create your views here.

'''to create cart but it is good practise if done in cart model Manager'''
# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print('New cart created')
#     return cart_obj

def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    return render(request, 'cart/home.html', {'cart':cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, Product is gone!")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.product.all():
            cart_obj.product.remove(product_obj)
        else:
            cart_obj.product.add(product_obj)
        request.session['cart_items'] = cart_obj.product.count()

    return redirect("cart:home")

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.product.count() == 0:
        return redirect("cart:home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    user = request.user
    billing_profile =None
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')

    if user.is_authenticated:
        billing_profile, billing_profile_create = BillingProfile.objects.get_or_create(
                                                           user=user, email=user.email)
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_create = BillingProfile.objects.get_or_create(
                                                  email=guest_email_obj.email)
    else:
        pass
    context = {
        'object': order_obj,
        'billing_profile': billing_profile,
        'login_form': login_form,
        'guest_form': guest_form
    }
    return render(request, 'cart/checkout.html', context)
