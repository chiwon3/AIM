from django.db import models

# Create your models here.

class naverwebtoon(models.Model):
    title = models.TextField()
    img = models.TextField()
    link = models.TextField()