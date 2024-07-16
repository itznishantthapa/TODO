from django.db import models

# Create your models here.
class Note(models.Model):
    heading=models.CharField(max_length=20)
    description=models.TextField(max_length=100)