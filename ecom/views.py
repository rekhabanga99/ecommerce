from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

app_name='ecom'
def index(request):
    return render(request,'ecom/index.html')

def category(request):
    return render(request,'ecom/category.html')

def product(request):
    return render(request,'ecom/single-product.html')

def login(request):
    return render(request,'ecom/login.html')

def cart(request):
    return render(request,'ecom/cart.html')

def checkout(request):
    return render(request,'ecom/checkout.html')

def confirmation(request):
    return render(request,'ecom/confirmation.html')

def tracking(request):
    return render(request,'ecom/tracking.html')