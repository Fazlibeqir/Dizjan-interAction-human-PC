from django.db import models


# Create your models here.


class Gotvac(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    bio = models.CharField(max_length=30)
    borndate = models.CharField(max_length=30)
    profileImage = models.ImageField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Recept(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sheff = models.ForeignKey(Gotvac, on_delete=models.CASCADE)
    opis = models.TextField()
    ingridians = models.TextField()
    instructions = models.TextField()
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    grade = models.IntegerField()
    comment = models.TextField()
    inputDate = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    chef = models.ForeignKey(Gotvac, on_delete=models.CASCADE)
    MEAL_CHOICES = (
        ("IT", "Italian"),
        ("CH", "Chinese"),
        ("JA", "Japanese"),
        ("ME", "Mexican"),
    )
    meal_type = models.CharField(max_length=255, choices=MEAL_CHOICES)
    recept = models.ManyToManyField(Recept)

    def __str__(self):
        return self.title


class Slika(models.Model):
    slika_url = models.URLField(unique=True, null=True)
    gotvac = models.ForeignKey(Gotvac, on_delete=models.CASCADE)
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)


class Nagrada(models.Model):
    chef = models.ForeignKey(Gotvac, on_delete=models.CASCADE)
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
