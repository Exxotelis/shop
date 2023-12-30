from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart  # Importing the Cart class
from store.models import Product  # Importing the Product model
# Importing JsonResponse for returning JSON responses
from django.http import JsonResponse


def cart_summary(request):
    # This view could display the items in the cart and their quantities
    return render(request, 'cart/cart-summary.html')


def cart_add(request):
    # Creating an instance of the Cart object using the request
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            # Getting the product ID from POST data
            product_id = int(request.POST.get('product_id'))
            # Getting the product quantity from POST data
            product_quantity = int(request.POST.get('product_quantity'))
            # Retrieving the product from the database by ID
            product = get_object_or_404(Product, id=product_id)
            # Adding the product to the cart with specified quantity
            cart.add(product=product, product_qty=product_quantity)

            # Constructing response data for successful addition to the cart
            response_data = {
                'message': 'Product added to cart successfully',
                'product_title': product.title,
                'product_quantity': product_quantity
            }

            # Returning a JSON response with success information
            return JsonResponse(response_data)
        except (ValueError, Product.DoesNotExist) as e:
            # Handling exceptions like ValueError or Product.DoesNotExist and returning error response
            response_data = {'error': str(e)}
            # Returning a JSON error response with status code 400
            return JsonResponse(response_data, status=400)
    else:
        # Handling cases where the request method is not POST or 'action' is not 'post'
        response_data = {'error': 'Invalid request'}
        # Returning a JSON error response with status code 400
        return JsonResponse(response_data, status=400)


def cart_delete(request, product_id):
    # Creating an instance of the Cart object using the request
    cart = Cart(request)
    # Retrieving the product from the database by ID
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)  # Removing the specified product from the cart
    # Returning a JSON response for successful removal
    return JsonResponse({'message': 'Product removed from cart'})


def cart_update(request):
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            # Getting the product ID from POST data
            product_id = int(request.POST.get('product_id'))
            # Getting the new quantity from POST data
            new_quantity = int(request.POST.get('new_quantity'))
            # Creating an instance of the Cart object using the request
            cart = Cart(request)
            # Retrieving the product from the database by ID
            product = get_object_or_404(Product, id=product_id)
            # Updating the product quantity in the cart
            cart.update(product=product, quantity=new_quantity)

            # Constructing response data for successful cart update
            response_data = {
                'message': 'Cart updated successfully',
                'product_title': product.title,
                'new_quantity': new_quantity
            }

            # Returning a JSON response with success information
            return JsonResponse(response_data)
        except (ValueError, Product.DoesNotExist) as e:
            # Handling exceptions like ValueError or Product.DoesNotExist and returning error response
            response_data = {'error': str(e)}
            # Returning a JSON error response with status code 400
            return JsonResponse(response_data, status=400)
    else:
        # Handling cases where the request method is not POST or 'action' is not 'post'
        response_data = {'error': 'Invalid request'}
        # Returning a JSON error response with status code 400
        return JsonResponse(response_data, status=400)
