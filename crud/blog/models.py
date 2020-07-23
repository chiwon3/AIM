from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.

class Blog(models.Model):
    title = models.CharField("제목",max_length=100)
    nick = models.CharField("닉네임",max_length=30)
    create_at = models.DateTimeField(auto_now=True)
    desc = models.TextField("내용",blank=True)
    image = models.ImageField("이미지",default="")
    contact = models.EmailField("E-Mail", blank=True)
    photo_thumbnail = ImageSpecField(
		source = 'image', 		                        # 원본 ImageField 명
		processors = [Thumbnail(100, 100)],             # 처리할 작업목록
		format = 'JPEG',		                        # 최종 저장 포맷
		options = {'quality': 60})                      # 저장 옵션
		
    
    def __str__(self):
        return self.title
        
