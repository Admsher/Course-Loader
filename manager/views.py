from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect

# Create your views here.
def base(request):
    current_year=datetime.date.today()
    
    return render(request,'base.html',{"current_year":current_year})





def login_user(request):
    if request.method == "POST" :
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    
        else:
            messages.success(request,"Username or Password might be incorrect.Please try again or contact the administrator.")
            return redirect('login')

    else:
        return render(request,'authentication/login.html',{})    