from django.db import models

# Create your models here.
class Product(models.Model):
    fio = models.CharField(max_length=100)
    pul = models.CharField(max_length=100)
    kod = models.CharField(max_length=50)
    asosiy_mahsulot = models.BooleanField()
    eslatma = models.CharField(max_length=300)