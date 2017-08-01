# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=5)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    city = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("byname",kwargs={"name":self.name})

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()