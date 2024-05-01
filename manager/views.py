from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import datetime

from .models import Files,Cachefile
import os
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
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
    


def populate_files():
    base_directory = settings.BASE_DIR  
    Files.objects.all().delete()
    Cachefile.objects.all().delete()
    cache_dir=str(base_directory)+'/Pickles'
    

    for root, dirs, files in os.walk(base_directory):
       

        if 'Sem' not in str(root):
            continue

        for file_name in files:
           
            file_path = os.path.join(root, file_name)

            
            parts = root.split(os.path.sep)
            if len(parts) >= 3:  
                academic_year = parts[-3]
                semester = parts[-2]
                department = parts[-1]

                file_instance = Files()
                file_instance.academic_year = academic_year
                file_instance.semester = semester
                file_instance.department = department
                file_instance.file = f"{academic_year}/{semester}/{department}/{file_name}"
                file_instance.save()
    if(os.path.exists(cache_dir)):
        files = os.listdir(cache_dir)
        for  file in files:
   
            file_path = os.path.join(cache_dir, file    )

            cache=Cachefile()
            cache.file=file_path
            cache.save()


@receiver(user_logged_in, sender=User)
def on_user_logged_in(sender, user, request, **kwargs):
    if user.is_superuser:
        
        populate_files()