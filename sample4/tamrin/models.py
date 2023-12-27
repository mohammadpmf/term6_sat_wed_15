from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
