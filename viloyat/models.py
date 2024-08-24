from django.db import models

# Create your models here.
class Viloyat(models.Model):
    viloyat = models.CharField(max_length=20)
    status = models.BooleanField()
