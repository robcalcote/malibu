from django.db import models

# Create your models here.

class Lot(models.Model):
    lot_number = models.IntegerField(default=0, primary_key=True)
    description_text = models.CharField(max_length=128)
    purchaseDate_date = models.DateField()
    received_boolean = models.BooleanField()

class Product(models.Model):
    sku_number = models.IntegerField(default=0, primary_key=True)
    lot_number = models.ForeignKey('Lot', on_delete=models.PROTECT)
    categories_text = models.CharField(max_length=256)
    descriptionShort_text = models.CharField(max_length=80)
    weight_number = models.DecimalField(max_digits=8, decimal_places=3)


