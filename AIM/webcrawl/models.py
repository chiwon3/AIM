from django.db import models

# Create your models here.

class NaverWebtoon(models.Model):
    title = models.TextField()
    img = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title