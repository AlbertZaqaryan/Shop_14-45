from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.index_filter, name='index_filter'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('product_details/', views.product_details, name='product_details'),
    path('shop/', views.shop, name='shop'),
    path('error/', views.error, name='error'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('delete_to_cart/', views.delete_to_cart, name='delete_to_cart'),
]
