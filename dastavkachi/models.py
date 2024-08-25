from django.db import models

# Create your models here.
class Dastavkachi(models.Model):
    fio = models.CharField(max_length=120)
    kol_bo = models.IntegerField()
    longitute = models.FloatField()
    latitute = models.FloatField()
    sana = models.DateField()
    holat = models.BooleanField()
