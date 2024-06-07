from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Bands(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.DateField()
    events_held = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to='posters/')
    participants = models.IntegerField(default=0)
    bands = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    INFO_CHOICES = (
        ('отворено', 'отворено'),
        ('не е отворено', 'не еотворено')
    )
    info = models.CharField(max_length=50, choices=INFO_CHOICES)

    def __str__(self):
        return self.name


class EventBands(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    bands = models.ForeignKey(Bands, on_delete=models.CASCADE)
