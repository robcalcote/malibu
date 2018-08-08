from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.order_by('descriptionShort_text')
    context = {'products': products}
    return render(request, 'inventory/index.html', context)

def detail(request, sku_number):
    item = get_object_or_404(Product, pk=sku_number)
    return render(request, 'inventory/detail.html', {'item': item})




# details view page (click the line item link to see more details on the item)