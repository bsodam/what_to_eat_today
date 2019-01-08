from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    info = models.CharField(max_length=300)

    def __str__(self):
        return self.restaurant_name
