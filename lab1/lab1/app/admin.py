from django.contrib import admin
from .models import Gotvac, Category, Recept, Review, Book, Slika, Nagrada

# Register your models here.

admin.site.register(Gotvac)
admin.site.register(Category)
admin.site.register(Recept)
admin.site.register(Review)
admin.site.register(Book)
admin.site.register(Slika)
admin.site.register(Nagrada)
