# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
from django.contrib import admin

# Create your models here.

# Create your models here.

class Result_Img(models.Model):
    Result_path = []
    Result_probability = models.CharField(max_length=200)
    Result_name = models.CharField(max_length=200)

