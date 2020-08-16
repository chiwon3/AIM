from django.shortcuts import render,redirect

# Create your views here.

def index(request): 
    return render(request, 'index.html')

def edit_page(request,id):
    context = dict()
    
    if request.method == "POST":
        temp_form = PostForms(request.POST,instance=Post.objects.get(id = request.user.id))
        
        if temp_form.is_valid():
            temp_form.save()
            return redirect('board')
        else:
            context["write_form"] = temp_form
            return render(request,'write.html',context)
    else:
        context["write_form"] = PostForms(instance=Post.objects.get(id = request.user.id))
        return render(request,'write.html', context)