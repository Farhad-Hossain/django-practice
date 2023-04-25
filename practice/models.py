from django.db import models
from datetime import date


class Person (models.Model):
    def __str__(self):
        return self.first_name.title()+' '+self.last_name

    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Long"),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default='M')

    @property
    def full_name(self):
        """Returns the persons full name"""
        return f"{self.first_name} {self.last_name}"
    
    @property
    def reversed_name(self):
        return f"{self.last_name} {self.first_name}"

class Group (models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(default=date(1900, 1,1))
    invite_reason = models.CharField(max_length=128)

class Musician (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album (models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Manufacturer (models.Model):
    name = models.CharField(max_length=50)
    established_year = models.IntegerField()

class Car (models.Model):
    COLORS = [
        ("red", "Red"),
        ("green", "Green"),
        ("blue", "Blue"),
    ]
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, choices=COLORS)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)