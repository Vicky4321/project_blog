from django.db import models

# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=2000)
    photo = models.ImageField()


