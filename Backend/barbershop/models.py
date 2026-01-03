from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.name
    
class Combo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return self.name