from django.shortcuts import render, redirect
from .forms import BlogForms
from .models import Blog

# Create your views here.

def index(request):
    context=dict()
    all_post = Blog.objects.all()
    context["all_post"] = all_post
    return render(request,'index.html',context)
    
def create(request):
    context=dict()
    
    if request.method == "POST":
        saveform = BlogForms(request.POST)
        
        if saveform.is_valid():
            saveform.save()
            return redirect('index')
        else :
            context['myform'] = saveform
            return render(request,'create.html',context)
            
    else :
        myform = BlogForms()
        context['myform'] = myform
        
        return render(request,'create.html',context)
        
def detail (request,blog_id):
    context = dict()
    context['one_blog'] = Blog.objects.get(id = blog_id)
    return render(request,'detail.html',context)
    
def edit(request,edit_blog_id):
    context=dict()
    
    if request.method == "POST":
        saveform = BlogForms(request.POST, instance=Blog.objects.get(id = edit_blog_id))
        
        if saveform.is_valid():
            saveform.save()
            return redirect('index')
        else :
            context['myform'] = saveform
            return render(request,'create.html',context)
            
    else :
        myform = BlogForms(instance=Blog.objects.get(id = edit_blog_id))
        context['myform'] = myform
        
        return render(request,'create.html',context)

def delete(request,blog_id):
    del_post = Blog.objects.get(id = blog_id)               #del_post에 삭제할 post_id를 붙여줌
    del_post.delete()                                       #이렇게만 적어도 가능한것은 django에서 이미 약속되어있기 때문
    return redirect('index')                                #삭제하고 다시 메인페이지로 돌아감
