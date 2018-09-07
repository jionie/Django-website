# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# Create your models here.

# Create your models here.

class Img(models.Model):
    img=models.ImageField(upload_to="",null=False,blank=True)
    img_id = models.CharField(max_length=200)
    img_name = models.CharField(max_length=200)






