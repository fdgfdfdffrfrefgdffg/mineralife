from django.db import models

# Create your models here.
class Ega(models.Model):
    login = models.CharField(max_length=50)
    parol = models.CharField(max_length=50)
