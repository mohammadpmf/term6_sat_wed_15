from django.db import models


class Fridge(models.Model):
    CHOICES = (
        ('A+', 'خیلی عالی'),
        ('A', 'خیلی'),
        ('B', 'خوب'),
    )
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    energy = models.CharField(max_length=4, choices=CHOICES)
    color = models.CharField(max_length=30)
    door_color = models.CharField(max_length=30, default='white')
    old_price = models.IntegerField(null=True, blank=True)
    adad = models.IntegerField()
    string = models.CharField(max_length=30)
    adad_koorosh = models.SmallIntegerField(default=9999999999999999)
    adad_koorosh2 = models.SmallIntegerField(default=999999999999999999999999999999999999999)
