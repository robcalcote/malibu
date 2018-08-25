from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.order_by('short_description')
    context = {'products': products}
    return render(request, 'inventory/index.html', context)


def detail(request, id):
    item = get_object_or_404(Product, pk=id)
    return render(request, 'inventory/detail.html', {'item': item})
