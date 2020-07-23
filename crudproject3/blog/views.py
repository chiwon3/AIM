from django.shortcuts import render,redirect
from .forms import BlogForms
from .models import Blog
# Create your views here.
def index(request):
    context=dict()
    all_post = Blog.objects.all()
    context['all_post'] = all_post
    return render(request,'index.html',context)

def create(request):
    context=dict()
    
    if request.method =="POST":
        saveform = BlogForms(request.POST)
        
        if saveform.is_valid():
            saveform.save()
            return redirect('index')
        else:
            context['myform'] = saveform
            return render(request, 'create.html',context)
    else:
        myform = BlogForms()
        context['myform'] = myform
        #context['myform'] = BlogForms()
        return render(request,'create.html',context)
        
def detail(request,blog_id):
    context = dict()
    context["one_blog"] = Blog.objects.get(id = blog_id)
    return render(request, 'detail.html', context)
    
    
def edit(request, edit_blog_id):
    context=dict()
    
    if request.method =="POST":
        saveform = BlogForms(request.POST, instance=Blog.objects.get(id = edit_blog_id) )
        
        if saveform.is_valid():
            saveform.save()
            return redirect('index')
        else:
            context['myform'] = saveform
            return render(request, 'create.html',context)
    else:
        myform = BlogForms( instance=Blog.objects.get(id = edit_blog_id) )
        context['myform'] = myform
        #context['myform'] = BlogForms()
        return render(request,'create.html',context)

def delete(request,post_id):
    target_blog = Blog.objects.get(id = post_id)
    target_blog.delete()
    
    return redirect('index')