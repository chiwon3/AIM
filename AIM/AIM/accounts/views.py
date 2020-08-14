from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractUser 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import auth

# Create your views here.

def signup(request):
    context=dict()
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        
        if signup_form.is_valid():
            signup_form.save()
            user = authenticate(username=signup_form.cleaned_data['username'],
                                password=signup_form.cleaned_data['password1'])
            return redirect("index")
        else :
            context['signup_form'] = signup_form
    
            return render(request, 'signup.html',context)
            
    else : 
        signup_form = UserCreationForm()
            
        context['signup_form'] = signup_form
        
        return render(request, 'signup.html',context)


# def signup(request):
#     if request.method == "POST":
#         if request.POST["password"] == request.POST["repassword"]:
#             user = User.objects.create_user(
#                 username=request.POST["username"], password=request.POST["password"])
#             auth.login(request,user)
#             return redirect('index')
#         return render(request, 'registration/signup.html')
#     return render(request, 'registration/signup.html')

def login(request):
    if request.method == "Post":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else :
            return render(request, 'registration/login.html', {'error': 'ID 혹은 비밀번호를 확인하세요.'})

    else :
        return render(request, 'registration/login.html')

    return render(requset, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')