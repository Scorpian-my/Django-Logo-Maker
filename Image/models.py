# image_app/models.py
from django.db import models

class ImageRequest(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
