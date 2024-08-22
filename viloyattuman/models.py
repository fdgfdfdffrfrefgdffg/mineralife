from django.db import models

# Create your models here.
class ViloyatTuman(models.Model):
    viloyat = models.CharField(max_length=25)
    tuman = models.CharField(max_length=50)
    status = models.BooleanField(default=True)