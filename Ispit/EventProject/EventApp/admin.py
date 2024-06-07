from django.contrib import admin
from .models import Bands, Event, EventBands

# Register your models here.

admin.site.register(Bands)
admin.site.register(Event)
admin.site.register(EventBands)
