from django.db import models

# Create your models here.
class Autolar(models.Model):
    login = models.CharField(max_length=120)
    parol = models.CharField(max_length=50)