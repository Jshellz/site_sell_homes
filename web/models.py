import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

# Lands
class Land(models.Model):
    name_land = models.CharField(max_length=200)
    price_land = models.CharField(max_length=100000)
    pub_date = models.DateTimeField('date_published_land')

    def __str__(self):
        return self.name_land

    def price_land(self):
        return self.price_land

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Flats
class Flat(models.Model):
    name_flat = models.CharField(max_length=2000)
    price_flat = models.CharField(max_length=100000)
    pub_date = models.DateTimeField('date_published_flat')

    def __str__(self):
        return self.name_flat

    def price_flat(self):
        return self.price_flat

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Houses
class House(models.Model):
    name_house = models.CharField(max_length=2000)
    price_house = models.CharField(max_length=100000)
    pub_date = models.DateTimeField('date_published_flat')

    def __str__(self):
        return self.name_house

    def price_house(self):
        return self.price_house

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
