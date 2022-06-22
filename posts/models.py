from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=10000)
    body = models.CharField(max_length=100000)
    created_at= models.DateTimeField(default= datetime.now, blank= True)

class   Paintings(models.Model):
    image= models.ImageField()    