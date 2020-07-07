from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def index(request): 
    context=dict()
    allpost = Post.objects.all()
    
    context['display_post'] = allpost
    return render(request, 'index.html',context)
    
def second(request):
    return render(request, 'create.html')
     
def create(request):
    Post.objects.create(title = request.POST.get('title'),
                        nickname = request.POST.get('nickname'),
                        body = request.POST.get('body'))
    return redirect("index")
    
def delete(request, memo_id):
		memo = get_object_or_404(Memo, pk=memo_id)
		memo.delete()
    return redirect("index")