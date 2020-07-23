from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    context=dict()
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        
        if signup_form.is_valid():
            signup_form.save()
            return redirect("index")
        else :
            context['signup_form'] = signup_form
    
            return render(request, 'registration/signup.html',context)
            
    else : 
        signup_form = UserCreationForm()
            
        context['signup_form'] = signup_form
        
        return render(request, 'registration/signup.html',context)
