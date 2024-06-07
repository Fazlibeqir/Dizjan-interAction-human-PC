from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    description = models.TextField()
    year = models.DateField()
    EMPLOYEE_CHOICES = (
        ('хигеничар', 'хигеничар'),
        ('рецепционер', 'рецепционер'),
        ('менаџер', 'менаџер'),
    )

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    bed_number = models.IntegerField()
    balcony = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number} {self.bed_number}"


class EmployeeRoom(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Hotels(models.Model):
    code = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    reserved = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_image = models.ImageField(upload_to='images/')
    approved = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
