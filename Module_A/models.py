# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=5)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    city = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name
