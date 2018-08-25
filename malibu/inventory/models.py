from django.db import models


class Lot(models.Model):
    description = models.CharField(max_length=128)
    purchase_date = models.DateField()
    received = models.BooleanField()

    def __str__(self):
        return self.description


class Product(models.Model):
    lot = models.ForeignKey('Lot', on_delete=models.PROTECT)
    categories = models.CharField(max_length=256)
    short_description = models.CharField(max_length=80)
    weight = models.DecimalField(max_digits=8, decimal_places=3)
