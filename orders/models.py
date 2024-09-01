from django.db import models
# Create your models here.

class Order(models.Model):
    customer_id = models.IntegerField()
    fio = models.CharField(max_length=100)
    product = models.CharField(max_length=200)
    suv_miqdori = models.CharField(max_length=20)
    viloyat = models.CharField(max_length=70)
    tuman = models.CharField(max_length=120)
    longitute = models.FloatField()
    latitute = models.FloatField()
    sana = models.DateField()
    vaqt = models.TimeField()
    dastavka = models.BooleanField()
    eslatma = models.CharField(max_length=300)
    auto = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
