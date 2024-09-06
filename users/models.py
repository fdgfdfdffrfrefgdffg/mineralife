from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=200)
    telefon = models.CharField(max_length=20)
    manzil = models.CharField(max_length=300)
    lavozimlar = models.CharField(max_length=50)
    eslatma = models.CharField(max_length=300)
    status = models.BooleanField(default=True)
