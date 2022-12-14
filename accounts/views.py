from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method=='POST':
            username=request.POST.get('Username')
            password=request.POST.get('Password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')

            else:
                messages.info(request,"Username or password is incorrect")  

    return render(request,'login.html')    
        
        
    
def logoutUser(request):
    logout(request)
    return redirect ('loginpage')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Welcome,please sign in Mr/Mrs '+user)
                return redirect('loginpage')
                    
    
    context={'form':form}
    return render(request,'register.html',context)    
