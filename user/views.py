from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def register(request):

    form=RegisterForm(request.POST or None)
    if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            newUser=User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request, 'Succesfully registered.')
            return redirect("index")
    context={
        "form":form
    }
    return render(request,"register.html",context)

def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                messages.success(request, 'Succesfully login.')
                if("next" in request.POST):
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('article:dashboard')
            else:
                messages.info(request, 'Username and password does not match')
                return render(request,"login.html",context)    
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request, 'Succesfully log out.')
    return redirect("index")