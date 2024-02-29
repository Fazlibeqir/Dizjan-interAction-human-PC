from django.db import models


# Create your models here.

class MyModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'firstApp'
