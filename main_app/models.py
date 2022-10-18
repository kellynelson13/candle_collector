from django.db import models

# Create your models here.
class Candle(models.Model):
    scent = models.CharField(max_length=75)
    color = models.CharField(max_length=75)
    ounces = models.IntegerField()
    burn_time = models.IntegerField()

    def __str__(self):
        return self.scent