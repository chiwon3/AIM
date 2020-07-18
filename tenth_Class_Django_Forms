crud 작업

지난시간에 한 CRUD 작업을 특정한 FORM을 짜서 반복적인 사용을 하도록 해줌

Django 에서 사용하는것에 90퍼센트 이상이 FORM을 사용

만들어둔 app 폴더 밑에 forms.py 파일을 만들어주고 아래와 같이 침

from django.forms import ModelForm
from .models import Blog

class BlogForms(ModelForm):
    class Meta :                                        #Meta 라는 건 정의하는것
        model = Blog                                    #form에서 사용할 model을 위에서 선언한 .models의 Blog 를 사용하겠다라는 뜻
        fields = ('title','nick','desc','contact',)     #fields = "__all__" 이렇게 작성해줘도 되긴 하지만 권장되지 않음
        
그리고 views.py에 가서 

from .forms import BlogForms를 추가해주고

def create(request):
    context=dict()
    myform = BlogForms()
    
    context['myform'] = myform
    return render(request,'create.html',context)
    
create를 이렇게 수정해준다

마지막으로 create.html에 가서 body에

    <form method="Post">
        {% csrf_token %}
        {{myform.as_p}}
        <input type='submit'>                           #제출 버튼은 자동으로 생기지 않아서 꼭 생성해줘야함
    </form>
    
이렇게 추가해준다
