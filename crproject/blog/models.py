from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목",max_length=100)
    body = models.TextField("내용")
    nickname = models.CharField("닉네임", max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title