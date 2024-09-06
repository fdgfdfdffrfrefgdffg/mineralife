from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=150)
    telefon = models.CharField(max_length=30)
    longitute = models.FloatField()
    latitute = models.FloatField()
    