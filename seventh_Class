Aaa 라는 앱 안에서 Data 라는 데이터 생성시 models.py 에서 Class Data(Aaa.aaa) : 하고 한줄 띄우고 만들어주면 됨


python manage.py makemigrations #명령어 치면 Class 만든걸 프로그래밍 언어로 마이그레이션을 함
python manage.py migrate #명령어 치면 마이그레이션 된걸 동기화를 함

admin.py에서 models.py 수정한걸 연동해줘야함
admin.py에서 from .models import Data 하면 이제 서로 연동 됨


Class 예제

Class Blog(models.Model):
    title = models.CharField(Max_length=100) #CharField는 TextField랑 다르게 한줄로 적도록 나옴
    body = models.TextField('내용') #내용이라고 적으면 텍스트 치는곳 위 라벨에 내용 이라고 나옴 위에 타이틀 처럼 안적으면 title: 이렇게 나옴
    Date = models.DateTimeField(auto_now=True) #auto_now 하면 지금 시간 찍힘
    
    def __str__(self) #따로 선언하지 않아도 django에서 미리 세팅되어있어서 괜춘
        return self.title #블로그 게시판에서 제목을 보여줌


admin 계정으로 관리자 페이지 접속방법
원래 주소에서 /admin 추가하면 Django에서 제공하는 페이지가 원래는 접속 되어야 함
근데 우리는 아이디 패스워드 만들어 준적 없음
python manage.py createsuperuser 치면 username, Email, password 세개를 입력 하라고 함
Email은 필수요소 아님, password는 8자 이상(로컬에서는 8자 안되도 괜춘)

models.py 에서 index.html로 바로 못가기때문에 views.py를 거쳐야함

예제
views.py 설정

all_blog = Blog.objects.all()
context['all_blog'] = all_blog

first_blog = Blog.objects.get(id=1) #글 하나만 보기 위한 설정, 이렇게 설정하면 blog에 여러개의 글 중 id 1번만 가져와서 보여줌
context['first_blog'] = first_blog

index.html 설정

블로그 글 리스트 보는 법

{{all_blog}} #블로그 글 딕셔너리에 담겨서 리스트화 되어서 제목만 안예쁘게 나옴, 밑에 적은 방법들이 예쁘게 보임

블로그 전체 글 보는 법

{% for one_blog in all_blog $}
    <h1>제목 : {{one_blog.title}}</h1>
    <p>내용 : {{one_blog.body}}</p>
    <p>날짜 : {{one_blog.date}}</p>

글 하나만 보는 법

    <h1>제목 : {{first_blog.title}}</h1>
    <p>내용 : {{first_blog.body}}</p>
    <p>날짜 : {{first_blog.date}}</p>

이렇게 하면 블로그 글 긁어옴

근데 시간 제대로 안나올거임
settings.py 들어가서 time을 UTC 되어있는거 한국 표준시간으로 맞추면 됨

