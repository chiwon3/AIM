from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField("제목",max_length=100)
    nick = models.CharField("닉네임",max_length=30)
    create_at = models.DateTimeField(auto_now=True)
    desc = models.TextField("내용",blank=True)
    contact = models.EmailField("E-Mail")
    
    def __str__(self):
        return self.title
        