from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=60)
    price1 = models.IntegerField()
    price2 = models.DecimalField(max_digits=6,decimal_places=2)