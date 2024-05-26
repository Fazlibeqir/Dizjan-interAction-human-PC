from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    founded_year = models.PositiveIntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books')
    isbn = models.CharField(max_length=50)
    year_published = models.PositiveIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()
    dimensions = models.CharField(max_length=50)
    cover_type = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=[
        ('Romance', 'Романса'),
        ('Thriller', 'Трилер'),
        ('Biography', 'Биографија'),
        ('Classic', 'Класик'),
        ('Drama', 'Драма'),
        ('History', 'Историја'),
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
