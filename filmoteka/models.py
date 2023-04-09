from django.contrib.auth.models import User
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=45)
    photo_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=45)
    photo_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    poster_url = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    country = models.CharField(max_length=45)
    description = models.TextField()
    duration = models.SmallIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()


class Mark(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.SmallIntegerField()


class Favourite(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
