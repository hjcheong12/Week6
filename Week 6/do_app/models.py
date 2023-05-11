from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length = 100)
    r_rate = models.FloatField()
    status = models.BooleanField(default=False)
    review = models.TextField()

def __str__(self):
    return self.title