from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('search/', views.ProductsFilterView.as_view(), name="products-search"),
    path('create/', views.CreateProductView.as_view(), name='create_product'),
    path('<int:pk>/image_upload/', views.ProductImageUploadView.as_view(), name='product_image_upload'),
    path('cart/all/', views.GetCartListView.as_view(), name="carts-list"),
    path('cart/create/', views.CreateCartView.as_view(), name="create-cart"),
    path('cart/<int:pk>/', views.CartView.as_view(), name="cart"),
    path('cart/<int:pk>/items/', views.CartItemsView.as_view(), name="cart-items"),


]
