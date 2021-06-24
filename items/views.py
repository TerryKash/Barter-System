from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.order_by('-pub_date')
    # n = len(products)
    params = {'product': products}
    return render(request, 'items/index.html', params)

def about(request):
    return render(request, 'items/about.html')
