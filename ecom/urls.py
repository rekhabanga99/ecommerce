from django.urls import path
from . import views
app_name='ecom'
urlpatterns=[
    path('',views.index,name="index"),
    path('category/',views.category,name="category"),
    path('product/',views.product,name="product"),
    path('login/',views.login,name="login")
]