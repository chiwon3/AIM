from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('제목',max_length=100)
    nickname = models.CharField('닉네임',max_length=20)
    body = models.TextField('내용')
    create_at = models.DateTimeField('작성시간',auto_now=True)
    
