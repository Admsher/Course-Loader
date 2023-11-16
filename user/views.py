from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
import pickle
from manager.models import department_description
from manager.models import anouncement
from manager.models import CDC_FD
from manager.models import CDC_HD
from manager.models import Elective_FD
from manager.models import Elective_HD
from openpyxl import Workbook
from openpyxl import load_workbook
from .forms import classformuser
from .forms import facultyform1user
from .forms import facultyform2user
from .forms import facultyform3user
from .forms import Electiveform_FDuser
from .forms import Electiveform_HDuser
from .forms import Semform
import datetime
from django.forms import formset_factory
from pathlib import Path
import pandas as pd
import numpy as np
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import os
from localStoragePy import localStoragePy
from django.forms.models import model_to_dict




localStorage = localStoragePy('user', 'text')
def login_user(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.success(
                request, "Username or Password might be incorrect.Please try again or contact the administrator.")
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})


def home(request):
   
    announcement_data = anouncement.objects.all()
   

    return render(request, 'homepage/home.html', {'announcement': announcement_data})


def previousrecord(request):
    return render(request, 'homepage/previousrecord.html', {})


def upload(request):
    Department=department_description.objects.get(Department_HOD=request.user)
    academic_year=str(str(datetime.date.today().year)+"/"+str(int(datetime.date.today().year)+1))

    context = {"academic_year":academic_year,"Department":Department}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'homepage/upload.html', context)


def filldata(request):
    return render(request, 'homepage/filldata.html', {})

@csrf_exempt
def choose_new_table(request):
    filecount=0
    academic_year_folder=str(str(datetime.date.today().year)+"-"+str(int(datetime.date.today().year)+1))
    Department_name = department_description.objects.get(Department_HOD=request.user)
    path=str(academic_year_folder)+"/"+str(Department_name)
    
    if not os.path.exists(path):
        os.makedirs(path)

    try:
        for filename in os.listdir(path):
            if filename.endswith('xlsx'): 
                filecount=filecount+1
          
        attempts_remaining=3-filecount
   

        if attempts_remaining==0:
            df=""
            message="Maximum submissions perfomed."
            tablePresent=False

        else:
            df=pd.read_excel("Courses for Course Load Submission "+str(Department_name)+".xlsx",sheet_name=str(Department_name))
            df=df.drop([0])
            df=df.fillna("")
            message=""
            tablePresent=True
            df=df.to_html()
    except FileNotFoundError:
        df=""
        message="Table not created yet."
        tablePresent=False

    if request.GET.get("elective_hd"):
            return Elective_HD_list(request=request)
    if request.GET.get("elective_fd"):
            return Elective_FD_list(request=request)
    if request.method=="POST":

        form=Semform(request.POST or None)
        if form.is_valid():
           
            semester=form.cleaned_data['Sem_choice']
            file=load_workbook("Courses for Course Load Submission "+str(Department_name)+".xlsx")
            sheet=file.get_sheet_by_name(str(Department_name))
            sheet["J2"]=form.cleaned_data["Sidenote"]
            file_path=Path(path+"/Courses for Course Load Submission Sem "+str(semester)+" "+str(Department_name)+".xlsx")
            if file_path.exists():
                file_old=load_workbook(file_path)
                file_old_path=Path(path+"/Courses for Course Load Submission Sem "+str(semester)+" "+str(Department_name)+" Old_1"+".xlsx")
                file_older_path=Path(path+"/Courses for Course Load Submission Sem "+str(semester)+" "+str(Department_name)+" Old_2"+".xlsx")
                if file_old_path.exists():
                    file_older=load_workbook(file_old_path)
                    file_older.save(file_older_path)
                else:
                    file_old.save(file_old_path)
            
            file.save(path+"/Courses for Course Load Submission Sem "+str(semester)+" "+str(Department_name)+".xlsx")
    else:
        form=Semform()
    
    
    return render(request, 'homepage/choose_new_table.html', {"message":message,"table":df,"bool":tablePresent,"form":form,"attempts":attempts_remaining})

 
def CDC_FD_list(request):
    Department_name = department_description.objects.get(Department_HOD=request.user)
    CDC_department = (CDC_FD.objects.filter(CDC_Department=Department_name))
    return render(request, 'homepage/CDC_FD_list.html', {"CDC_List": CDC_department})

def CDC_HD_list(request):
    Department_name = department_description.objects.get()
    CDC_department = (CDC_HD.objects.filter(CDC_HD_Department=Department_name))

   
    return render(request, 'homepage/CDC_HD_list.html', {"CDC_List": CDC_department})


def previewForm(request):
    global cdc_id


    
    if request.method == 'GET':
           cdc_id = request.GET.get('data')
           localStorage.setItem('cdc_id',cdc_id)
          

    academic_year_folder=str(str(datetime.date.today().year-1)+"-"+str(int(datetime.date.today().year)))
    Department_name = department_description.objects.get(Department_HOD=request.user)
    path=str(academic_year_folder)+"/"+str(Department_name)
    
    for filename in os.listdir(path):
        if filename.endswith('xlsx'): 
            filepath=os.path.join(path, filename)
       
    try:
        database=pd.read_excel(filepath,sheet_name=str(department_description.objects.get()))
       
    
    except FileNotFoundError:
        database=pd.read_excel("cache.xlsx")

    
    database=database.drop([0])
    database=database.drop(database.columns[7],axis=1)
    database=database.drop(database.columns[8],axis=1)
    
    try:
        row_number=database[database.eq(cdc_id).any(axis=1)].index.to_numpy()
        row_count=0
        for i in range(row_number[0],len(database[database.columns[1]])-1):
            if database.iloc[i][0] is not np.nan:
                break
            row_count=row_count+1    


        section_list=[]

        for i in range(0,row_count):
            section_list.append(database.iloc[row_number[0]+i][4])
       
        section_list_numpy=np.array(section_list)
        Number_of_Lectures=np.count_nonzero(section_list_numpy=="L")+1
        Number_of_Tutorials=np.count_nonzero(section_list_numpy=="T")
        Number_of_Labs=np.count_nonzero(section_list_numpy=="P")
    except IndexError:
        Number_of_Lectures='No previous data'
        Number_of_Labs='No previous data'
        Number_of_Tutorials='No previous Data'

    Lecture_Faculty=[]
    Tutorial_Faculty=[]
    Labarotary_Faculty=[]
    FIC_preview=str(database.iat[int(row_number-1),6])
    for i in range(0,Number_of_Lectures):
     if str(database.iat[int(i+row_number-1),6])=="nan":
         Lecture_Faculty.append("No Data")
     else:    
        Lecture_Faculty.append(str(database.iat[int(i+row_number-1),6]))
    for i in range(0,Number_of_Labs):
      if str(database.iat[int(i+row_number+Number_of_Tutorials+Number_of_Lectures),6])=="nan":
         Labarotary_Faculty.append("No Data")
      else:   
         Labarotary_Faculty.append(str(database.iat[int(i+row_number+Number_of_Tutorials+Number_of_Lectures),6]))
    for i in range(0,Number_of_Tutorials):
        if str(database.iat[int(i+row_number+Number_of_Lectures),6])=="nan":
         Tutorial_Faculty.append("No Data")
        else: 
         Tutorial_Faculty.append(str(database.iat[int(i+row_number+Number_of_Lectures-1),6]))
     

    
    try:
        cdc_title=CDC_FD.objects.get(CDC_ID=cdc_id).CDC_name   
    except ObjectDoesNotExist:
        print()
    try:
        cdc_title=CDC_HD.objects.get(CDC_HD_ID=cdc_id).CDC_HD_name   
    except ObjectDoesNotExist:
        print()
    try:
        cdc_title=Elective_HD.objects.get(Elective_HD_ID=cdc_id).Elective_HD_name   
    except ObjectDoesNotExist:
        print()
    try:
        cdc_title=Elective_FD.objects.get(Elective_ID=cdc_id).Elective_name   
    except ObjectDoesNotExist:
        print()
        
    if request.method=="POST":
        
        create_file(request=request,FIC_name=FIC_preview,Lecture=Number_of_Lectures,Lab=Number_of_Labs,Tutorial=Number_of_Tutorials,Faculty_Lec=Lecture_Faculty,Faculty_Tut=Tutorial_Faculty,Faculty_Lab=Labarotary_Faculty)
        return choose_new_table(request=request)
    return render(request,'homepage/previewForm.html',{'Lectures':Number_of_Lectures,'Tutorial':Number_of_Tutorials,'Labs':Number_of_Labs,"CDC_name":cdc_title,"Lab_Faculty":Labarotary_Faculty,"Tut_Faculty":Tutorial_Faculty,"Lec_Faculty":Lecture_Faculty})





def form_CDC(request):
    global FIC
    global cdc_title
           
    cdc_title = request.GET.get('data')
    formclass=classformuser(user=request.user)
   
    if request.method == 'POST':
        form = formclass(request.POST) 

        if form.is_valid():
                FIC=form.cleaned_data["FIC"]
                localStorage.setItem('cdc_FIC',FIC)
                request.session['Tuts']=form.cleaned_data["Tutorials"]
                request.session['Lec']=form.cleaned_data["Lectures"]
                request.session['Lab']=form.cleaned_data["Labs"]
                
                
                
        return form_faculty_lec(request=request)
                
       
                           
    
    else:
         
         form = formclass()
    

    return render(request, "homepage/form_CDC.html", context={'form': form,"cdc_name":cdc_title})



def form_faculty_lec(request):
 
 global Lab_number
 global Lecture_Number
 global Tutorial_number
 global Lec_Faculty
 Lec_Faculty=[]
 Lab_number=request.session["Lab"]
 Lecture_Number=request.session["Lec"]
 Tutorial_number=request.session["Tuts"] 

 facultyform1=facultyform1user(user=request.user)
 Lectureformset=formset_factory(facultyform1,extra=Lecture_Number)


    
 if request.method=="POST":
        form_lec=Lectureformset(request.POST or None)
       
        if form_lec.is_valid(): 
            for forms in form_lec:
                Lec_Faculty.append(forms.cleaned_data['Faculty'])
    
           
            return  HttpResponseRedirect('form_Faculty_Tut')
                
            

 return render(request, 'homepage/facultyForm_Lec.html', {'Lectureformset': Lectureformset})

def form_faculty_tut(request):
        
        global Tut_Faculty
        Tut_Faculty=[]
        
        facultyform2=facultyform2user(user=request.user)
        Tutformset=formset_factory(facultyform2,extra=Tutorial_number)
        if request.method=="POST":
            form_tut=Tutformset(request.POST or None)

            if form_tut.is_valid():
                for forms in form_tut:
                    Tut_Faculty.append(forms.cleaned_data['Faculty'])

                return  HttpResponseRedirect('form_Faculty_Lab')
        return render(request, 'homepage/facultyForm_Tut.html', {"Tutformset":Tutformset})



def form_faculty_lab(request):  
      
         submitted=False
         Lab_Faculty=[]
         
         facultyform3=facultyform3user(user=request.user)
         Labformset=formset_factory(facultyform3,extra=Lab_number)
         if request.method=="POST":
            form_lab=Labformset(request.POST or None)
            submitted=True
            if form_lab.is_valid():
                for forms in form_lab:
                    Lab_Faculty.append(forms.cleaned_data['Faculty'])
                try:
                    create_file(FIC_name=FIC,Lecture=Lecture_Number,Tutorial=Tutorial_number,Lab=Lab_number,Faculty_Lab=Lab_Faculty,Faculty_Lec=Lec_Faculty,Faculty_Tut=Tut_Faculty)
                    return choose_new_table(request=request)
                except NameError:
                    FIC=localStorage.getItem('cdc_FIC')
                    create_file(FIC_name=FIC,Lecture=Lecture_Number,Tutorial=Tutorial_number,Lab=Lab_number,Faculty_Lab=Lab_Faculty,Faculty_Lec=Lec_Faculty,Faculty_Tut=Tut_Faculty)
                    return choose_new_table(request=request)
                
         return render(request, 'homepage/facultyForm_Lab.html', {"Labformset":Labformset,"submitted":submitted})



       
def create_file(request,FIC_name,Lecture,Tutorial,Lab,Faculty_Lec,Faculty_Lab,Faculty_Tut):
    try:
        print(cdc_id)
    except NameError:
        cdc_id=localStorage.getItem('cdc_id')
    Department_name = department_description.objects.get(Department_HOD=request.user)
   

    excel_file=Path("Courses for Course Load Submission "+str(Department_name)+".xlsx")

    if excel_file.exists():
       file=load_workbook("Courses for Course Load Submission "+str(Department_name)+".xlsx")
       sheet=file.get_sheet_by_name(str(Department_name))
       row_if_present=""
       next_row_entry=""
         
       for i in range(1,sheet.max_row):
           column = 'A'
           row = i
           cell_value = sheet[f'{column}{row}'].value
           if cell_value==cdc_id:
            row_if_present=row
            break
       if row_if_present!="":
            for i in range(int(row_if_present)+1,sheet.max_row):
                column = 'A'
                row = i
                cell = sheet[f'{column}{row}']
                if cell.value:
                    next_row_entry=row
                    break
            if next_row_entry=="":
                next_row_entry=sheet.max_row
            for i in range(row_if_present,next_row_entry):
                sheet.delete_rows(row_if_present)
           
       last_row=sheet.max_row
       sheet.cell(row=last_row+1,column=6).value=str(FIC_name)
       sheet.cell(row=last_row+1,column=1).value=str(cdc_id)
       try:
         sheet.cell(row=last_row+1,column=2).value=str(cdc_title)
       except UnboundLocalError:
             try:
                cdc_title=CDC_FD.objects.get(CDC_ID=cdc_id).CDC_name   
             except ObjectDoesNotExist:
                print()
             try:
                cdc_title=CDC_HD.objects.get(CDC_HD_ID=cdc_id).CDC_HD_name   
             except ObjectDoesNotExist:
                print()
             try:
                cdc_title=Elective_HD.objects.get(Elective_HD_ID=cdc_id).Elective_HD_name   
             except ObjectDoesNotExist:
                print()
             try:
                cdc_title=Elective_FD.objects.get(Elective_ID=cdc_id).Elective_name   
             except ObjectDoesNotExist:
                 print()
             sheet.cell(row=last_row+1,column=2).value=str(cdc_title)
           
       for i in range(0,Lecture):
           try:
            sheet.cell(row=last_row+i+1, column=5).value="L"
            sheet.cell(row=last_row+i+1, column=7).value=str(Faculty_Lec[i])
           except IndexError:
                break
       for i in range(0,Tutorial):
            try:
                sheet.cell(row=last_row+Lecture+i+1, column=5).value="T"
                sheet.cell(row=last_row+Lecture+i+1, column=7).value=str(Faculty_Tut[i])
            except IndexError:
                break

       for i in range(0,Lab):
         try:
            sheet.cell(row=last_row+Tutorial+Lecture+i+1, column=5).value="P"
            
            sheet.cell(row=last_row+Lecture+Tutorial+i+1, column=7).value=str(Faculty_Lab[i])
         except IndexError:
                break
       file.save("Courses for Course Load Submission "+str(Department_name)+".xlsx")

    else:    
   
        Wb_load=Workbook()
        Sheet=Wb_load.create_sheet(title=str(Department_name))
        Sheet['A3']="COURSE NUMBER"
        Sheet['B3']="COURSE TITLE"
        Sheet["D3"]="Section Number"
        Sheet["E3"]="Section"
        Sheet["F3"]="Instructor In Charge"
        Sheet["G3"]="Instructor"
        Sheet["F4"]=str(FIC_name)
        Sheet['A4']=str(cdc_id)
        try:
            Sheet['B4']=str(cdc_title)
        except NameError:
             try:
                cdc_title=CDC_FD.objects.get(CDC_ID=cdc_id).CDC_name   
             except ObjectDoesNotExist:
                print()
             try:
                cdc_title=CDC_HD.objects.get(CDC_HD_ID=cdc_id).CDC_HD_name   
             except ObjectDoesNotExist:
                print()
             try:
                cdc_title=Elective_HD.objects.get(Elective_HD_ID=cdc_id).Elective_HD_name   
             except ObjectDoesNotExist:
                print()
             try:
                cdc_title=Elective_FD.objects.get(Elective_ID=cdc_id).Elective_name   
             except ObjectDoesNotExist:
                 print()
             Sheet['B4']=str(cdc_title)   
        for i in range(0,Lecture):
           
            Sheet.cell(row=4+i, column=5).value="L"
            Sheet.cell(row=4+i, column=7).value=str(Faculty_Lec[i])
        for i in range(0,Tutorial):
          try: 
            Sheet.cell(row=4+Lecture+i, column=5).value="T"
           
            Sheet.cell(row=4+Lecture+i, column=7).value=str(Faculty_Tut[i])
          except IndexError:
            break
        for i in range(0,Lab):
         try:
            Sheet.cell(row=4+Tutorial+Lecture+i, column=5).value="P"
          
            Sheet.cell(row=4+Tutorial+Lecture+i, column=7).value=str(Faculty_Lab[i])
         except IndexError:
            break
        Wb_load.save("Courses for Course Load Submission "+str(Department_name)+".xlsx")


def Elective_FD_list(request):
    Department_name = department_description.objects.get(Department_HOD=request.user)
    form_Elective=Electiveform_FDuser(user=request.user)
    try: 
        try:
            with open(str(Department_name)+'_FD.pkl', 'rb') as f:
                data = pickle.load(f)
        except FileNotFoundError:
            open(str(Department_name)+'_FD.pkl','a')
            with open(str(Department_name)+'_FD.pkl', 'rb') as f:
                data = pickle.load(f)
        data_dict=model_to_dict(data)
        Elective_list= data
        form=form_Elective(initial=data_dict)
        f.close()

        
    except EOFError:
        Elective_list=[]
        form=form_Elective()

   
    if request.method=="POST":
        form=form_Elective(request.POST or None)
        
        if form.is_valid():
            Elective_list=form.cleaned_data['Elective_ID']
            try:    
                    f=open(str(Department_name)+'_FD.pkl','wb')
            except FileNotFoundError:
                    open(str(Department_name)+'_FD.pkl','a')
                    f=open(str(Department_name)+'_FD.pkl','wb')
            
        


    return render(request,"homepage/Elective_FD_list.html",{"form":form,"elective_list":Elective_list})




def Elective_HD_list(request):
   Department_name = department_description.objects.get(Department_HOD=request.user)
   try: 
    try:
        with open(str(Department_name)+'_HD.pkl', 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
            open(str(Department_name)+'_HD.pkl','a')
            with open(str(Department_name)+'_HD.pkl', 'rb') as f:
                data = pickle.load(f)
    # data_dict=model_to_dict(data)
    
    form_Elective=Electiveform_HDuser(user=request.user)
    Elective_list= data
    form=form_Elective()
    f.close()
   except EOFError:
        Elective_list=[]
        form=form_Elective()

   if request.method=="POST":
        form=form_Elective(request.POST or None)
        
        if form.is_valid():
               
                Elective_list=form.cleaned_data['Elective_ID']

              
                try:    
                    f=open(str(Department_name)+'_HD.pkl','wb')
                except FileNotFoundError:
                    open(str(Department_name)+'_HD.pkl','a')
                    f=open(str(Department_name)+'_HD.pkl','wb')


                (pickle.dump(Elective_list,f))
  
   return render(request,"homepage/Elective_HD_list.html",{"form":form,"elective_list":Elective_list})


