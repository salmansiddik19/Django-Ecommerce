import json
from .models import *
from user.models import Profile, User
from product.models import Product
from order.models import Order, OrderItem


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    order = {'get_cart_item': 0, 'get_cart_total': 0}
    cart_item = order['get_cart_item']
    for i in cart:
        try:
            cart_item += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.product_price * cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_item'] += cart[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'product_name': product.product_name,
                    'product_price': product.product_price,
                    'product_image': product.product_image,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)
        except:
            pass
    return {'order': order, 'items': items, 'cart_item': cart_item}


def cart_data(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = Profile(
                user=request.user, name=request.user.first_name, email=request.user.email)
            profile.save()
        order, created = Order.objects.get_or_create(
            profile=profile,
            complete=False,
        )
        items = order.orderitem_set.all()
        cart_item = order.get_cart_item
    else:
        cookie_data = cookie_cart(request)
        order = cookie_data['order']
        items = cookie_data['items']
        cart_item = cookie_data['cart_item']
    return {'order': order, 'items': items, 'cart_item': cart_item}


def guest_order(request, data):
    print('User is not authenticated...')
    print('Cookies:', request.COOKIES)
    email = data['form']['email']

    cookie_data = cookie_cart(request)
    items = cookie_data['items']
    profile, create = Profile.objects.get_or_create(
        email=email
    )
    profile.save()
    order, created = Order.objects.get_or_create(
        profile=profile,
        complete=False,
    )
    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        order_item = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'],
        )
    return profile, order
