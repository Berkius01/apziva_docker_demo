from django.db import models

# Create your models here.
class Github(models.Model):
    username = models.CharField(max_length=100)
    followers = models.CharField(max_length=100)
    following = models.CharField(max_length=100)
    repos = models.CharField(max_length=100)
    stars = models.CharField(max_length=100)
    contrb = models.CharField(max_length=100)
