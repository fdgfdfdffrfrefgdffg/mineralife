from django.db import models

# Create your models here.
class Xarita(models.Model):
    order_id = models.IntegerField()
    fio = models.CharField(max_length=150)
    longitute = models.FloatField()
    latitute = models.FloatField()
