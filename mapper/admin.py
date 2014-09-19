from django.contrib import admin
from .models import Movie, Location


# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')



admin.register(Movie)
admin.register(Location)
