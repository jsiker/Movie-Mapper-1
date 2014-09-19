from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

    # class Meta:
    #     verbose_name_plural = 'Locations'

class Movie(models.Model):
    name = models.CharField(max_length=120)
    year = models.IntegerField(max_length=4, null=True)
    imdbid = models.CharField(max_length=20, null=True)
    location = models.ForeignKey(Location, related_name="locations")

    def __unicode__(self):
        return self.name







