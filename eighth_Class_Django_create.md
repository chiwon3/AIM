crproject 작업

TAP 수시로 닫아주기
이름이 다 같은 파일들이 많아서 안닫아주면 헷갈리기 쉬움

django-admin startproject crproject 로 프로젝트 생성

cd crproject로 프로젝트 폴더 안으로 들어옴
수시로 ls 눌러서 파일 list 확인

python manage.py startapp blog 로 APP파일 생성

crproject안에 settings.py 에 들어가서 ALLOWED_HOSTS = ['*'] 호스트 열어주기 #허용되는 호스트 열어주는것
지금은 Cloud9 쓰니까 전체 풀어서 하지만 로컬에서 개발하면 이거 안해도 로컬 접속은 됨

settings.py에서 INSTALLED_APPS = 에 'blog.apps.BlogConfig', 을 추가해서 앱을 연동시킴
'blog', 로 적어도 되지만 이렇게 적는 연습 하기
새로이 추가하는 앱들은 제일 하단에 적고 관련있는 앱끼리 묶어서 주석 달아놓기

crproject안에 urls.py에 from blog.views import index 추가하기
urls.py 에서 urlpatterns에 path('', index, name="index"), 추가하기
하지만 지금 이상황에서 오류 발생할거임 아직 views 안에 index가 없음

blog 폴더 아래에 templates 폴더 만들고 그 안에 index.html 만들기
index.html 파일에 !누르고 탭 해서 기본 html 문서 만들기

views에 하단 인덱스 디파인 명령어 만들기
def index(request): 
    return render(request, 'index.html')
    
이렇게 하면 기본적인 세팅은 끝났음
python manage.py runserver 8080 해서 서버 돌려도 에러 없이 서버 돌아갈거임

서버 정상 확인 후 blog 폴더 밑에 models.py 에 Class 생성
class Post(models.Model): #괄호 안에 첫번째는 위에 from django.db import models 에서 import 뒷부분을 그대로 가져옴
    title = models.CharField("제목",max_length=100) #제목처럼 짧은 글 적을때 CharField 사용
    body = models.TextField("내용") #"내용"으로 적은 부분이 디스플레이 됨, 안적고 괄호만 열어놓으면 앞에 body 부분을 가져옴, TextField는 긴 글 쓸때
    created_at = models.DateTimeField(auto_now=True) #지금 시간을 자동으로 가져옴, DateTimeField는 시간 가져올때

docs.djangoproject.com 에 가면 필드 종류 볼수있음 주로 쓰는건 CharField, TextField, DateTimeField 세개가 제일 많이 씀
그 외에 참고할만한 필드
EmailField(max_length=254,**option) #Email 양식 안맞으면 오류값 리턴
FileField(
numberField
등등 있음 궁금한거 있으면 위에 사이트 들어가서 Field 검색해보기


python manage.py makemigrations 쳐서 마이그레이션 해서 컴퓨터가 알아보게 프로그래밍 언어로 마이그레이션 해줌
python manage.py migrate 해서 마이그레이션 된 파일 적용 가능

제대로 된 것을 확인하고싶을때 admin.py에 들어감
from .models import Post 해서 admin.py랑 같이 있는 models.py 에 있는 Post 라는 클래스를 연동시킴
밑에 admin.site.register(Post) 쳐둠

밑에 bash 창에 python manage.py createsuperuser 쳐서 관리자 계정 만듬
패스워드는 8자 이상

서버 돌리는 주소 뒤에 /admin 추가해서 관리자 페이지로 이동
임시로 admin / adminadmin 으로 만듬
id pw 아까 작성한걸로 들어감


게시판에 게시물 작성했을때 타이틀을 보고싶으면 models.py 에 들어가서
class Post(models.Model): 이 속성 맨 밑에
    def __str__(self):
        return self.title
이렇게 작성
제목이 아니라 다른걸 작성하고 싶으면 위에 self. 뒤에 title 말고 다른거 적어주면 됨
def __str__(self): 이부분은 약속된 부분이라서 언더바 2개씩 꼭 붙여줘야함

이제 이걸 관리자 페이지 아니라 다른데서 보여주고싶으면 views.py에 들어감
우선 파일 연결부터 시켜야하니까 from .models import Post 추가
그러고 나서 원래

def index(request): 
    return render(request, 'index.html')
    
이렇게 되어 있던 문서를

def index(request): 
    context=dict()
    allpost = Post.objects.all()
    
    context['display_post'] = all_post
    return render(request, 'index.html',context)
    
이렇게 바꿔줌

하지만 index.html에서는 보여주는 방식을 설정하지 않았으니 아직 안나옴
index.html 들어가서

<body>
    <h1><게시판></h1>
    {% for one_post in display_post %}
        <h2>[ {{ one_post.id }} ]번째 글</h2>
        <h3>제목 : {{ one_post.title }} - {{ one_post.nickname }}</h3>
        <p>내용 : {{ one_post.body }}</p>
    {% endfor %}
</body>

게시판에서 내용이 다 나오는게 지저분하면 <p>내용 : {{ one_post.body | slice:":100"}}</p> 해서 잘라서 보여줄수 있음

이렇게 수정해놓으면 이제 보여줄수 있음

관리자페이지가 주소가 /admin이면 해킹당하기가 쉬움
/admin 페이지 주소를 바꾸려면 urls.에 들어가서 path('admin/', admin.site.urls), 에서 'admin/' 부분을 수정하면 주소 바꿀수 있음

이제 글을 보여주는 페이지도 만들었고 글을 쓰는 방식을 만들어야 함

우선 글을 작성하는 url을 만들기 위해 urls.py에 들어감
from blog.views import index에 from blog.views import index,create 로 수정해줌
그러고 나서 path('create/', create, name="create"), 를 밑에 추가해줌

우선 create라는 url은 등록되었음 그럼 어떻게 동작할지를 또 만들어줘야함 views.py에 들어감

글 작성 된 것을 전달하는 방법은 두개임
def create(request):
    tmp_post = Post()
    tmp_post.title = request.POST.get('title')
    tmp_post.nickname = request.POST.get('nickname')
    tmp_post.body = request.POST.get('body')
    tmp_post.save()
    return redirect("index")
    

def create(request):
    Post.objects.create(title = request.POST.get('title'),
                        nickname = request.POST.get('nickname'),
                        body = request.POST.get('body') )
    return redirect("index")

이 두개의 차이점
위에 방식은 tmp_post라는 빈 박스에 post에 입력되는 항목을 하나씩 담아서 전달하는 방식
밑에 방식은 정해져있는 양식의 내용을 따로 다른곳에 저장하지 않고 전달하는 방식

request 뒤에 POST와 GET을 하나라도 잘못 넣으면 blog_post. may not be NULL 이라는 ERROR가 뜸
게시판의 경우에는 따로 두번 저장할 필요가 없어서 아래의 경우가 더 직관적으로 표현되고 더 적합함


index.html에 아래 명령어를 입력
    <form method="post" action="{% url 'create' %}">
        {% csrf_token %}
        <input type="text" name="title" placeholder="제목"/>
        <input type="text" name="nickname" placeholder="닉네임"/>
        <textarea name="body" placeholder="내용을 입력하세요"></textarea>
        <input type="submit" name="제출" values="제출"/>
    </form>
글을 입력하는 양식을 만들어줬음
csrf_token은 form의 method를 GET이 아닌 POST로 지정하였기때문에 암호화되어서 글 내용이 전송되는것을 해석해주는 토큰
안넣어주면 이게 해석이 안되어서 CSRF 에러 코드가 발생
