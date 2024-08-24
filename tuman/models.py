from django.db import models

# Create your models here.
class Tuman(models.Model):
    viloyat = models.CharField(max_length=20)
    tuman = models.CharField(max_length=50)
    status = models.BooleanField()