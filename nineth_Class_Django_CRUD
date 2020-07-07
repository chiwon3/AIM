crudproject 작업

C,R,U,D가 중요한 이유 - 가장 기본적인 개발로 주니어개발자들을 볼때 제일 먼저 보는 부분
create, read, update, delete

create에서는 없는 글을 생성하기 때문에특정 ID가 필요없음
read, update, delete는 기존에 작성되어있는 특정된 글에 대해서 행위가 이루어져야하기 때문에 나머지 항목에서는 ID 라는게 중요

!!!!!!!!!!!  create  !!!!!!!!!!!

지난시간 복습
우선 기본 설정을 마친 뒤 a tag로 글쓰기 페이지 연결

    <a href="{% url 'create_page' %}">글쓰기</a>
    
create_page html 문서 만듬

views에 기능 추가

    
def create_page(request) :
    return render(request, 'create_page.html')              #render는 그 페이지를 그려서 보여주는것
    
def create(request) :
    if request.method == "POST":                            # method를 POST로 지정할것이기 때문에 정상적인 글쓰기 버튼을 통한 요청일때만 글이 써짐 
        Post.objects.create(title = request.POST.get('title'),
                            nickname = request.POST.get('nickname'),
                            body = request.POST.get('body'))
        return redirect("index")                            # 글이 써 지고 다시 메인페이지로 돌아감
    else :
        return redirect("index")                            # 사용자가 다른 방식으로 접근을 시도할때 메인화면만 보여줌


url에 path 아까 views에 추가한 두개 마찬가지로 추가

    from blog.views import index,create_page,create

    path('create_page/',create_page, name = "create_page"), #create_page로 이동하는 기능
    path('create/', create, name="create"),                 #실제로 글을 쓰는 기능

그 뒤에 create_page html 문서에서 create 기능 구현
post 쓸때는 csrf_token 잊지말기

    <form action= "{% url 'create' %}" method="post">
        {% csrf_token %}
        <input type="text" name="title" class="title" placeholder="제목"/>
        <input type="text" name="nickname" class="nickname" placeholder="닉네임"/><hr>
        <textarea name="body" class="body" placeholder="내용을 입력하세요"></textarea><br>
        <input type="submit" value="글쓰기"/>               #여기에서 value는 버튼에 나오는 글자일 뿐 특별한 의미 없음
    </form>


!!!!!!!!!!!  read  !!!!!!!!!!!

이제 글이 써 지지만 읽어지지는 않음

글을 읽을수 있도록 우선 보여지는 페이지인 detail html 문서 만듬

하지만 여기서부터는 전체 글을 다 보는게 아니라 내가 클릭한 글을 보여줘야함

그래서 views에서 request뒤에 post_id를 함께 넘겨줌
context 빈 dictionary에 one_post라는 이름으로 글 번호 넣어서 담아줌
그리고 detail html 문서로 넘어갈때 글번호가 담긴 context 같이 넘겨줘서 그 글을 보여주도록 함

def detail(request,post_id):
    context = dict()
    one_post = Post.objects.get(id = post_id)
    context['one_post'] = one_post
    return render(request,'detail.html',context)
    
url에서도 <int: 과 고유의 post_id 를 써서 숫자를 detail 뒤에 붙도록 만듬

    path('detail/<int:post_id>', detail, name = "detail"),

이렇게 하고 나서 detail html 문서로 와서는 아래처럼 작성

    <h1>제목 :    {{one_post.title}}</h1>                   # {{ }}으로 감싸주는것은 그냥 가져와서 보여주는것 {% %}으로 감싸주는것은 함수
    <strong>닉네임 :     {{one_post.nickname}}<br></strong><hr>                 #strong은 닉네임 Bold처리 해서 강조하려고 쓴것, hr은 가로줄 긋기
    <h3>내용</h3><br> 
    <p>{{one_post.body}}</p><br>


!!!!!!!!!!!  delete  !!!!!!!!!!!

삭제는 쉬움
views에 가서 아까와 같이 post_id와 함께 넘겨줌

def delete(request,post_id):
    del_post = Post.objects.get(id = post_id)               #del_post에 삭제할 post_id를 붙여줌
    del_post.delete()                                       #이렇게만 적어도 가능한것은 django에서 이미 약속되어있기 때문
    return redirect('index')                                #삭제하고 다시 메인페이지로 돌아감

url에 path와 import를 추가함

    from blog.views import index,create_page,create,detail,delete
    
    path('delete/<int:post_id>', delete, name = "delete"),

이제 detail html 페이지에 연결시켜주면 끝

    <a href="{% url 'delete' one_post.id %}"><h6> 삭제하기 </h6></a>

!!!!!!!!!!!  update  !!!!!!!!!!!

개인적으로는 제일 어려웠음

우선 views에 가서 아까 create와 같이 버튼으로 작동해야하니 if를 써서 사용자의 다른 동작을 방지함
여기에서는 else로 다른 동작으로 들어오면 수정한 내용은 저장되지않은 채 계속 create_page로 돌아가도록 되어 있음

def update(request,post_id):
    if request.method == "POST":
        update_post = Post.objects.get(id = post_id)
        update_post.title = request.POST.get('title')
        update_post.nickname = request.POST.get('nickname')
        update_post.body = request.POST.get('body')
        update_post.save()                                      #이것또한 마찬가지로 django에서 save를 약속해두었기 때문에 쉬움
        return redirect('index')
    else :
        context = dict()
        one_post = Post.objects.get(id = post_id)
        context['one_post'] = one_post
        return render(request,'create_page.html',context)
        
이제 urls로 가서 path랑 import 추가해줌        

from blog.views import index,create_page,create,detail,delete,update    #참고로 crudproject 가보면 이 순서가 아닌데 내가 update 어려워서 순서 바꾼거임

    path('update/<int:post_id>', update, name = "update"),

수정의 경우 글쓰기 창으로 돌아가는데 대신 내용이 담긴 채로 있어야함

그래서 create_page를 수정해줌
one_post를 가지고 있을때 즉 이미 있는 글을 수정할때는 if문과 같이 update action을 하게 됨
value에 넣어준 글들이 이미 입력되어서 나옴
사실 else에도 똑같이 넣어주더라도 신규 작성의 경우 아직 one_post id가 생성되어있지 않기 때문에 보이지않지만 혹시모를 오류에 대비함

    {% if one_post %}
    <form action= "{% url 'update' one_post.id %}" method="post">
        {% csrf_token %}
        <input type="text" name="title" class="title" placeholder="제목" value="{{one_post.title}}"/>
        <input type="text" name="nickname" class="nickname" placeholder="닉네임" value="{{one_post.nickname}}"/><hr>
        <textarea name="body" class="body" placeholder="내용을 입력하세요">{{one_post.body}}</textarea><br>
        <input type="submit" value="수정하기"/>
    </form>
    {% else %}
        <form action= "{% url 'create' %}" method="post">
        {% csrf_token %}
        <input type="text" name="title" class="title" placeholder="제목"/>
        <input type="text" name="nickname" class="nickname" placeholder="닉네임"/><hr>
        <textarea name="body" class="body" placeholder="내용을 입력하세요"></textarea><br>
        <input type="submit" value="글쓰기"/>
    </form>
    {% endif %}
    


수업후기
create_page가 기존에 있는 것을 수정하는 것이어서 정리하기가 어려웠고 순간 놓치고 나니 이미 있는것이 바뀌어있어 어디서부터 따라해야할지 멘붕왔음
create_page에서 url을 거는 부분에서 one_post.id가 아닌 one_post만 적어서 계속 오류가 났었음

이렇게 오류가 발생했을때는 에러페이지에 밑에 노란색으로 표시된 부분을 찾거나 오류난 페이지쪽에서 오타를 보는것이 좋음