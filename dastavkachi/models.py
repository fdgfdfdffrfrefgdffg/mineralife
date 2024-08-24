from django.db import models

# Create your models here.
class Dastavkachi(models.Model):
    fio = models.CharField(max_length=120)
    kol_bo = models.IntegerField()
    manzil = models.CharField(max_length=300)
    sana = models.DateField()
    holat = models.BooleanField()
