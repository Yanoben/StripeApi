from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    def return_link(self):
        return reverse('item', args=[self.pk])


# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     currency = models.CharField(max_length=3, default='USD')

# class Order(models.Model):
#     items = models.ManyToManyField(Item)
#     total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     # Добавьте поля для применения скидки и налога

# class Discount(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     # Добавьте соответствующие поля для скидки

# class Tax(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     # Добавьте соответствующие поля для налога
