from django.urls import path
from . import views

urlpatterns = [
    # Store main page
    path('', views.store, name='store'),

    # Idnividual product
    path('product/<slug:product_slug>', views.product_info, name='product-info'),
    # Idnividual Category
    path('search/<slug:category_slug>',
         views.list_category, name='list-category'),

]
