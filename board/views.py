from django.shortcuts import render,redirect
from .forms import PostForms,CommentForms
from .models import Post,Comment
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

# Create your views here.

def board(request):
    context=dict()
    all_post = Post.objects.all()
    context['all_post'] = all_post
    return render(request,'board.html',context)
    
    
def create(request):
    context = dict()
    
    if request.method == "POST":
        temp_form = PostForms(request.POST)
        if temp_form.is_valid():
            success_form = temp_form.save(commit=False)
            
            success_form.author = User.objects.get(id = request.user.id)
            success_form.save()
            return redirect('board')
        else:
            context["write_form"] = temp_form
            return render(request,'write.html',context)
    else:
        context["write_form"] = PostForms()
        return render(request,'write.html', context)
        
def detail(request,post_id):
    context = dict()
    detail_post = Post.objects.get(id = post_id)
    context['detail_post'] = detail_post
    context['comment_form'] = CommentForms()
    context['comment_all'] = Comment.objects.filter(post = Post.objects.get(id=post_id))
    return render(request,'detail.html',context)
        
def update(request,post_id):
    context = dict()
    
    if request.method == "POST":
        temp_form = PostForms(request.POST,instance=Post.objects.get(id = post_id))
        
        if temp_form.is_valid():
            temp_form.save()
            return redirect('board')
        else:
            context["write_form"] = temp_form
            return render(request,'write.html',context)
    else:
        context["write_form"] = PostForms(instance=Post.objects.get(id = post_id))
        return render(request,'write.html', context)
        
        
def delete(request,post_id):
    detail_post = Post.objects.get(id = post_id)
    if detail_post.author == request.user :
        detail_post.delete()
    return redirect('board')
    
    
    
def comment_create(request,post_id):
    if request.method == "POST":
        temp_form = CommentForms(request.POST)
        if temp_form.is_valid():
            clean_form = temp_form.save(commit=False)
            
            clean_form.author = User.objects.get(id = request.user.id)
            clean_form.post = Post.objects.get(id=post_id)
            clean_form.save()
    return redirect('detail', post_id)
    
    
def comment_delete(request,post_id, com_id):
    del_com = Comment.objects.get(id = com_id)
    del_com.delete()
    
    return redirect('detail', post_id)