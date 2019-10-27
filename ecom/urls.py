from django.urls import path
from . import views
app_name='ecom'
urlpatterns=[
    path('',views.index,name="index"),
    path('category/',views.category,name="category"),
    path('product/',views.product,name="product"),
    path('login/',views.login,name="login"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('confirmation/',views.confirmation,name="confirmation"),
    path('tracking/',views.tracking,name="tracking")
]
