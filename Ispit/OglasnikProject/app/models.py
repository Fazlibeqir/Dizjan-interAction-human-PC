from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Oglas(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    STATUS_CHOICE = (
        ('цената е фиксна', 'цената е фиксна'),
        ('прифаќам предлози', 'прифаќам предлози'),
        ('цената не е фиксна', 'цената не е фиксна'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)
    INFO_CHOICE = (
        ('Нов', 'Нов'),
        ('Стар', 'Стар'),
    )
    info = models.CharField(max_length=50, choices=INFO_CHOICE)

    def __str__(self):
        return self.title
