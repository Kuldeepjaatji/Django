from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name