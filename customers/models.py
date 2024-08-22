from django.db import models

# Create your models here.
class Customer(models.Model):
    fio = models.CharField(max_length=150)
    telefon = models.CharField(max_length=30)
    manzil = models.CharField(max_length=300)
