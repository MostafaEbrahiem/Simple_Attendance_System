from datetime import datetime
from os import stat
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from accounts.models import attend ,Leave
from django.urls import reverse


@login_required(login_url='loginpage')
def home(request):
    status= None

    if request.user.is_authenticated:

        try:    
            attended_datatime=str(attend.objects.get(attender=request.user).datetime)[:10]
        except:
            pass

        try:    
            attended_today = attend.objects.filter(attender=request.user,datetime__startswith=attended_datatime)
            status=2
        except:
            status=3

        if status==3:
            attend_obj=attend(attender=request.user)
            attend_obj.save()   
            status=1        
        
    
    context={'status':status}
    return render(request,"home.html",context)


@login_required(login_url='loginpage')
def func_Leave(request):
    status= None
    try:    
        emp_Leave_datatime=str(attend.objects.get(attender=request.user).datetime)[:10]
        
    except:
        status=5
        context={'status':status}
        return render(request,"home.html",context)

    try:    
        Leave_datatime=str(Leave.objects.get(emp_Leave=request.user).datetime)[:10]
        emp_Leave_today = Leave.objects.filter(emp_Leave=request.user,datetime__startswith=Leave_datatime)
        status=2
    except:
        status=3

    if status==3:
        Leave_obj=Leave(emp_Leave=request.user)
        Leave_obj.save()  
        status=1
 
    context={'status':status}
    return render(request,"home.html",context)


@login_required(login_url='loginpage')
def Show(request):
    status= None
    try:    
        res=[]
        temp1=str(attend.objects.get(attender=request.user).datetime)
        temp2=str(Leave.objects.get(emp_Leave=request.user).datetime)[10:19] 

        res.append("At "+temp1[:10] )
        res.append("You Arrived at "+temp1[10:19])
        res.append("Leaved at "+temp2)
        status=7
        context={'Show_res':res,'status':status}
        return render(request,"home.html",context)

        
    except:
        status=6
        context={'status':status}
        return render(request,"home.html",context)

