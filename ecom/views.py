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