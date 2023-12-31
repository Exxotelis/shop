from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart  # Importing the Cart class
from store.models import Product  # Importing the Product model
# Importing JsonResponse for returning JSON responses
from django.http import JsonResponse


def cart_summary(request):
    cart = Cart(request)
    # This view could display the items in the cart and their quantities
    return render(request, 'cart/cart-summary.html', {'cart': cart})


def cart_add(request):
    # Creating an instance of the Cart object using the request
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        # Getting the product ID from POST data
        product_id = int(request.POST.get('product_id'))
        # Getting the product quantity from POST data
        product_quantity = int(request.POST.get('product_quantity'))
        # Retrieving the product from the database by ID
        product = get_object_or_404(Product, id=product_id)
        # Adding the product to the cart with specified quantity
        cart.add(product=product, product_qty=product_quantity)

        cart_quantity = cart.__len__()

        # Constructing response data for successful addition to the cart
        response = JsonResponse({'qty': cart_quantity})

        # Returning a JSON response with success information
        return response


def cart_delete(request):
    # Creating an instance of the Cart object using the request
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Retrieving the product from the database by ID
        product_id = int(request.POST.get('product_id'))
        # Removing the specified product from the cart
        cart.delete(product=product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        # Returning a JSON response for successful removal
        response = JsonResponse(
            {'qty': cart_quantity, 'total': cart_total, 'message': 'Product removed from cart'})
        return response


def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = request.POST.get('product_quantity')

        cart.update(product=product_id, qty=product_quantity)

        cart_quantity = cart.__len__()
        cart_total = cart.get_total()

        response = JsonResponse(
            {'qty': cart_quantity, 'total': cart_total})
        return response
