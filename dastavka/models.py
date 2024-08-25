from django.db import models

# Create your models here.
class Dastavka(models.Model):
    mijoz = models.CharField(max_length=150)
    fio = models.CharField(max_length=100)
    kol_vo_voda = models.IntegerField()
    maxsulot = models.CharField(max_length=150)
    naqt = models.FloatField()
    plastik = models.FloatField()
    sana = models.DateField()
    auto = models.CharField(max_length=50)
    holat = models.BooleanField()
