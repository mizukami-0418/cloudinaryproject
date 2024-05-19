# models.py

from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title