from django.db import models

# Create your models here.
class animalwebsite(models.Model):
    img=models.ImageField(upload_to='')
    description=models.CharField(max_length=50)
    author=models.CharField(max_length=50)