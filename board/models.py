from django.db import models
from django.utils import timezone
from django.conf import settings
from django.conf.urls.static import static


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    title = models.CharField("제목", max_length=50)
    desc = models.TextField("내용")
    create_at = models.DateTimeField('작성시간', default = timezone.now)
    
    
    def __str__(self):
        return self.title
        
        
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.CharField("내용", max_length=250)
    create_at = models.DateTimeField('작성시간', default = timezone.now)

    def __str__(self):
        return self.body

