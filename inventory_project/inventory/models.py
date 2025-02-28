from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('purchased', 'Purchased'),
        ('sold', 'Sold'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    product_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
