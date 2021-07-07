from django.db import models


class ShoppingList(models.Model):

    item = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    check = models.BooleanField(default=False)

    def __str__(self):
        return self.item
