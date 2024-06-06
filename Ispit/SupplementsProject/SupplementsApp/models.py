from django.db import models


# Create your models here.

class Supplements(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='upload_to/')
    code = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    CATEGORY_CHOICES = (
        ('proteins', 'proteins'),
        ('vitamins', 'vitamins'),
        ('amino acids', 'amino acids'),
        ('pre-workout', 'pre-workout'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
