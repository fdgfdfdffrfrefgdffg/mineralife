from django.db import models

# Create your models here.
class UsersImg(models.Model):
    user_id = models.SmallIntegerField()
    img = models.ImageField(upload_to="/media")
