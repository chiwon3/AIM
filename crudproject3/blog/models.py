from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField('제목',max_length=100)
    desc = models.TextField('내용',blank=True)
    contact = models.EmailField('이메일')
    
    created_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title