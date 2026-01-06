from django.db import models
from django.conf import settings

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
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Combo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()
    services = models.ManyToManyField(Service, related_name='combos')

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    barber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='barber_appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.barber} - {self.date} {self.time}"
    
    class Meta:
        ordering = ['-date', '-time']