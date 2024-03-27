from django.db import models
from django.contrib.auth.models import User
import datetime
import os
import pandas as pd

df = pd.read_excel("Departments.xlsx", sheet_name="Codes")
class department_description(models.Model):
     
     AY=()
     for i in range(0,10):
          AY=AY+((str(int(datetime.date.today().year)-1-int(i))+"-"+str(int(datetime.date.today().year)-int(i)),str(int(datetime.date.today().year)-1-int(i))+"-"+str(int(datetime.date.today().year)-int(i))),)
     Department_HOD=models.OneToOneField(User,on_delete=models.CASCADE)
     Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
     Department_name=models.CharField('Department name',choices=Department_Choice,max_length=50)
     Upcoming_Sem=models.CharField('Upcoming Semester',choices=(('Sem 1','Sem 1'),('Sem 2','Sem 2')),max_length=50,null=True)
     Academic_year=models.CharField('Academic Year',choices=AY,max_length=50,null=True)
     Previous_records=models.CharField('Link for the previous data',max_length=400,null=True,blank=True)
     Lock=models.BooleanField('Lock Website',default=False)
   

     def __str__(self):
          return self.Department_name
        
class CDC_FD(models.Model):
        Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
        CDC_ID=models.CharField('CDC_ID',max_length=20)
        CDC_name=models.CharField('CDC_name',max_length=50)
        CDC_Department=models.CharField('Department name',choices=Department_Choice,max_length=50)
        Upcoming_Sem_FD=models.CharField('Upcoming Semester',choices=(('Sem 1','Sem 1'),('Sem 2','Sem 2')),max_length=50,null=True)
        def __str__(self):
             return self.CDC_ID

class CDC_HD(models.Model):
        Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
        CDC_HD_ID=models.CharField('CDC_ID',max_length=20)
        CDC_HD_name=models.CharField('CDC_name',max_length=50)
        CDC_HD_Department=models.CharField('Department name',choices=Department_Choice,max_length=50)
        Upcoming_Sem_HD=models.CharField('Upcoming Semester',choices=(('Sem 1','Sem 1'),('Sem 2','Sem 2')),max_length=50,null=True)
        def __str__(self):
             return self.CDC_HD_ID
        
class Elective_FD(models.Model):
        Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
        Elective_ID=models.CharField('Elective_ID',max_length=20)
        Elective_name=models.CharField('Elective_name',max_length=50)
        Elective_Department=models.CharField('Department name',choices=Department_Choice,max_length=50)
        
        def __str__(self):
             return self.Elective_ID

class Elective_HD(models.Model):
        Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
        Elective_HD_ID=models.CharField('Elective_ID',max_length=20)
        Elective_HD_name=models.CharField('Elective_name',max_length=50)
        Elective_HD_Department=models.CharField('Department name',choices=Department_Choice,max_length=50)
        
        def __str__(self):
             return self.Elective_HD_ID

class WILP(models.Model):
        Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
        WILP_ID=models.CharField('Elective_ID',max_length=20)
        WILP_name=models.CharField('Elective_name',max_length=50)
        WILP_Department=models.CharField('Department name',choices=Department_Choice,max_length=50)
        
        def __str__(self):
             return self.WILP_ID



class anouncement(models.Model):
    title=models.CharField('announcement_title',max_length=120)
    date=models.DateTimeField('announcement_date')
    description=models.TextField(blank=True)
    handler=models.CharField(default='admin',max_length=20)
   

class Faculty_List(models.Model):
     
     first_name=models.CharField(max_length=50)
     ID_No=models.CharField(max_length=50)
     Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
     Department=models.CharField('Department name',choices=Department_Choice,max_length=50)


     def __str__(self):
          return self.first_name

class PHD_List(models.Model):
     
     first_name=models.CharField(max_length=50)
     PSM_No=models.CharField(max_length=50)
     Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
     Department=models.CharField('Department name',choices=Department_Choice,max_length=50)
   

     def __str__(self):
          return self.first_name



     


def dynamic_upload_path(instance, filename):
    return f"{instance.academic_year}\{instance.semester}\{instance.department}\{filename}"

class Files(models.Model):
    Department_Choice = [(code, name) for code, name in zip(df['Department Code'], df['Department name'])]
    AY=()
    for i in range(0,10):
          AY=AY+((str(int(datetime.date.today().year)-1-int(i))+"-"+str(int(datetime.date.today().year)-int(i)),str(int(datetime.date.today().year)-1-int(i))+"-"+str(int(datetime.date.today().year)-int(i))),)
    academic_year = models.CharField('Academic Year',choices=AY,max_length=50,null=True)
    semester = models.CharField('Upcoming Semester',choices=(('Sem 1','Sem 1'),('Sem 2','Sem 2')),max_length=50,null=True)
    department =models.CharField('Department name',choices=Department_Choice,max_length=50)
    file = models.FileField(upload_to=dynamic_upload_path)

    def __str__(self):
        return f"\{self.file}"

    def save(self, *args, **kwargs):
       
        try:
            old_instance = Files.objects.get(pk=self.pk)
            
            if old_instance.file != self.file:
                
                old_instance.delete_file()
        except Files.DoesNotExist:
            pass

        super().save(*args, **kwargs)
  
    def delete(self, *args, **kwargs):
        self.delete_file()
        super().delete(*args, **kwargs)

    def delete_file(self):
     file_path = self.file.path

     try:
        if os.path.exists(file_path):
               os.remove(file_path)
     except OSError:
            # Handle the case where the file doesn't exist gracefully
            pass

def dynamic_upload_path_cache(instance, filename):
    return f"Pickles"

class Cachefile(models.Model):
    file = models.FileField(upload_to=dynamic_upload_path_cache)

    def __str__(self):
        return f"\{self.file}"

    def save(self, *args, **kwargs):


        try:
            old_instance = Files.objects.get(pk=self.pk)
            
            if old_instance.file != self.file:
                
                old_instance.delete_file()
        except Files.DoesNotExist:
            pass

        super().save(*args, **kwargs)
  
    def delete(self, *args, **kwargs):
        self.delete_file()
        super().delete(*args, **kwargs)

    def delete_file(self):
     file_path = self.file.path

     try:
        if os.path.exists(file_path):
               os.remove(file_path)
     except OSError:
            # Handle the case where the file doesn't exist gracefully
            pass