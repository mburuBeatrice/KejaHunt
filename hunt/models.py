from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=30)
    
class House(models.Model):
    Location = models.CharField(max_length=30)
    Image = models.ImageField()
    Description = models.TextField(max_length=250)
    Type = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
