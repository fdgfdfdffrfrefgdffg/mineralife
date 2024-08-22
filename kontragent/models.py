from django.db import models

# Create your models here.
class Kontragent(models.Model):
    fio = models.CharField(max_length=200)
    telefon = models.CharField(max_length=30)
    telefon2 = models.CharField(max_length=30)
    dokon_nomer= models.CharField(max_length=50)
    manzil = models.CharField(max_length=300)
    status = models.BooleanField(default=True)