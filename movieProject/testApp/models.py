from django.db import models


# Create your models here.
class Movie(models.Model):
    ReleaseDate = models.DateField()
    moviename = models.CharField(max_length=20)
    hero = models.CharField(max_length=20)
    heroin = models.CharField(max_length=20)
    rating = models.IntegerField()
