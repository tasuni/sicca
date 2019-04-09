from django.db import models


# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=50)
    coin_img = models.ImageField(upload_to='images/')