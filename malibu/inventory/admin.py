from django.contrib import admin
from .models import Product, Lot


class ProductAdmin(admin.ModelAdmin):
    fields = ['lot', 'short_description', 'categories', 'weight']
    list_display = ('short_description', 'lot', 'weight', 'categories')
    list_filter = ['categories']


class LotAdmin(admin.ModelAdmin):
    fields = ['description', 'purchase_date', 'received']
    list_display = ('description', 'purchase_date', 'received')


admin.site.register(Product, ProductAdmin)
admin.site.register(Lot, LotAdmin)
