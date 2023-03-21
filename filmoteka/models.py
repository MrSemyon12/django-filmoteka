from django.contrib.auth.models import User
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=45)
    photo_url = models.CharField(max_length=255)


class Actor(models.Model):
    name = models.CharField(max_length=45)
    photo_url = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=45, primary_key=True)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    poster_url = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    country = models.CharField(max_length=45)
    description = models.TextField()
    duration = models.SmallIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


class Mark(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    value = models.SmallIntegerField()


class Favourite(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
