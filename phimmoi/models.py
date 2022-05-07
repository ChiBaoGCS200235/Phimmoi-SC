from django.db import models

# Create your models here.
class Movie(models.Model):
    movieName = models.CharField(max_length=200, null=False)
    chapter = models.IntegerField(max_length=100, null=False)
    totalChapter = models.IntegerField(max_length=100, null=False)
    views = models.IntegerField(max_length=1000000, null=False)
    description = models.TextField(max_length=1000, null=False)
    openingSong = models.TextField(max_length=100, null=False)
    closingSong = models.TextField(max_length=100, null=False)
    movieLink = models.TextField(max_length=1000, default="")
    picture = models.TextField(max_length=100, default="")
    background = models.TextField(max_length=100, default="")
    type = models.TextField(max_length=100, default="")

    def __str__(self):
        return self.movieName



class episode(models.Model):
    movieName = models.CharField(max_length=200)
    chapter = models.IntegerField(max_length=1000)
    video = models.TextField(max_length=500, default="", null=True, blank=True)

    def __str__(self):
        return self.movieName


class Viewer(models.Model):
    username = models.CharField(max_length=200, default="", null=True, blank=True)
    password = models.CharField(max_length=200, default="", null=True, blank=True)
    repassword = models.CharField(max_length=200, default="", null=True, blank=True)
    email = models.EmailField(max_length=200, default="", null=True, blank=True)
    fullname = models.CharField(max_length=200, default="", null=True, blank=True)
    birthday = models.CharField(max_length=200, default="", null=True, blank=True)
    sex = models.CharField(max_length=5, default="", null=True, blank=True)

    def __str__(self):
        return self.username