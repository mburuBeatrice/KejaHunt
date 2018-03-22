from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=30)


    def __str__(self):
        return self.category

class House(models.Model):
    Location = models.CharField(max_length=30)
    Image = models.ImageField()
    Description = models.TextField(max_length=250)
    Type = models.CharField(max_length=30)
    contact_email = models.EmailField(default=1)
    contact_number = models.IntegerField(default=1)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User,default=1)

    def __str__(self):
        return self.Location
    
    def create_house(self):
        self.create()
    def delete_house(self):
        self.delete()
    @classmethod
    def search_by_category(cls,search_term):
        house_search = cls.objects.filter(category__category__icontains=search_term)

        return house_search
class Contacts(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    email_address = models.EmailField()

    def __str__(self):
        return self.name

class About(models.Model):
    description = models.TextField(max_length=250)

  
