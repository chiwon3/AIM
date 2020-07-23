crud 작업

더이상 처음부터 만들지 않고 지난 시간에 사용한 crud 를 그대로 사용했다

static 과 media의 차이
static은 사이트 운영측에서 제공하는 데이터, media는 유저가 가져온 데이터

만든 app 폴더 밑에 static 폴더를 만들고 그 밑에 또 다른 폴더로 css, image, font, js 등을 만들어서 사용

index.html에 가서 <!DOCTYPE html> 위에 {% load static %} 으로 문서가 시작하기 전에 static 폴더부터 불러옴

그리고 CSS를 불러오는 건 head에 <link href="{% static 'css/index.css' %}" rel="stylesheet" type="text/css" />를 추가해줌

이미지도 마찬가지임 <img src="{% static 'image/EPL_ranking1.jpg' %}" class="EPL_Rank"></img> 이렇게 적으면 img 

settings.py에 밑에 STATIC_ROOT = os.path.join(BASE_DIR, 'static')를 추가해주고 명령어 창에 python manage.py collectstatic 침
그러면 STATIC_ROOT에 지정해준 static이라는 폴더로 css, img같은 static 구성된 것들이 자동으로 뽑힘
기본적으로 default static 루트가 static임

STATIC_URL = '/static/'                             #사용자가 static 요소들 요청하는 주소
                                                    #기본적으로 이 세팅만 되어있으면 STATIC_ROOT는 default가 static이기 때문에 따로 설정 안해줘도 됨
                                                    #하지만 이 설정을 바꾸고 싶으면 아래 설정도 static이 아닌 다른 주소로 바꾸어줘야함
STATIC_ROOT = os.path.join(BASE_DIR, 'static')      #개발단계에서 실제로 배포할때는 모아서 배포해야하니까 collectstatic으로 한곳에 모아서 배포

이걸 알았으니 이제 사용자가 사진을 올리는걸 저장해보겠음

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/submedia')

우선 이렇게 아까 배운대로 저장해주는 주소를 만들었음

이러고 모델에 image = models.ImageField("이미지",default="") 를 추가해서 image를 넣을수 있는 칸을 만들었음

views.py 에도 create와 edit의 request.POST뒤에 ,request.FILES 이렇게 넣어줬음

사진을 보내야하니까 Files를 넣어준거고 create.html 에서도 <form method="Post" enctype="multipart/form-data">를 넣어줘야함

그러고 모델을 수정했으니 makemigration을 해줘야하는데 안됐음

그럴때는 pip install pillow --user                  #Cloud 9에서 하다보니 설치 안될때가 있는데 그럴때는 --user 옵션 주면 됨

그러고나서 makemigration 해주고 migrate 했음

이제 썸네일을 만들어줄거임

models.py에 들어가서 아래 명령어를 추가함

from imagekit.models import ImageSpecField          
from imagekit.processors import Thumbnail

    photo_thumbnail = ImageSpecField(
		source = 'image', 		                        # 원본 ImageField 명
		processors = [Thumbnail(100, 100)],             # 처리할 작업목록
		format = 'JPEG',		                        # 최종 저장 포맷
		options = {'quality': 60})                      # 저장 옵션
		
이제 썸네일도 만들어지니까 index.html에 보이도록 해보자

    {% for one_blog in all_post %}
        <a href="{% url 'detail' one_blog.id %}">
밑에 
        {% if one_blog.image%}
            <img src="{{one_blog.photo_thumbnail.url}}" alt = "실패">
        {% endif%}

이렇게 추가해놓으면 썸네일 생김