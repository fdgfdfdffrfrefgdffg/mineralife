from django.db import models

# Create your models here.
class Tolov(models.Model):
    mijoz = models.CharField(max_length=120)
    qolgan_butulkalar = models.SmallIntegerField()
    kol_bo_suv = models.SmallIntegerField()
    maxsulot = models.CharField(max_length=100)
    naqt = models.FloatField()
    plastik = models.FloatField()
    chiqim = models.FloatField()
    sana = models.DateField()
