from django.db import models
from django.contrib.auth.models import User


        
class CDC_FD(models.Model):
        Department_Choice=(("CHE",'Chemical'),("MECH","Mechanical"),("EEE-INSTR","Electrical"),("Computer Science","Computer Science"),("PHY","Physics"),("BIO","Biology"),("CHEM","Chemistry"),("MATHS","Mathematics"),('ECON & MGMT',"Economics"),("HUM","Humanities"))
        CDC_ID=models.CharField('CDC_ID',max_length=20)
        CDC_name=models.CharField('CDC_name',max_length=50)
        CDC_Department=models.CharField('CDC_Department',max_length=100,choices=Department_Choice)

        def __str__(self):
             return self.CDC_ID

class CDC_HD(models.Model):
        Department_Choice=(("CHE",'Chemical'),("MECH","Mechanical"),("EEE-INSTR","Electrical"),("Computer Science","Computer Science"),("PHY","Physics"),("BIO","Biology"),("CHEM","Chemistry"),("MATHS","Mathematics"),('ECON & MGMT',"Economics"),("HUM","Humanities"))
        CDC_HD_ID=models.CharField('CDC_ID',max_length=20)
        CDC_HD_name=models.CharField('CDC_name',max_length=50)
        CDC_HD_Department=models.CharField('CDC_Department',max_length=100,choices=Department_Choice)

        def __str__(self):
             return self.CDC_HD_ID
        
class Elective_FD(models.Model):
        Department_Choice=(("CHE",'Chemical'),("MECH","Mechanical"),("EEE-INSTR","Electrical"),("Computer Science","Computer Science"),("PHY","Physics"),("BIO","Biology"),("CHEM","Chemistry"),("MATHS","Mathematics"),('ECON & MGMT',"Economics"),("HUM","Humanities"))
        Elective_ID=models.CharField('Elective_ID',max_length=20)
        Elective_name=models.CharField('Elective_name',max_length=50)
        Elective_Department=models.CharField('Elective_Department',max_length=100,choices=Department_Choice)

        def __str__(self):
             return self.Elective_ID

class Elective_HD(models.Model):
        Department_Choice=(("CHE",'Chemical'),("MECH","Mechanical"),("EEE-INSTR","Electrical"),("Computer Science","Computer Science"),("PHY","Physics"),("BIO","Biology"),("CHEM","Chemistry"),("MATHS","Mathematics"),('ECON & MGMT',"Economics"),("HUM","Humanities"))
        Elective_HD_ID=models.CharField('Elective_ID',max_length=20)
        Elective_HD_name=models.CharField('Elective_name',max_length=50)
        Elective_HD_Department=models.CharField('Elective_Department',max_length=100,choices=Department_Choice)

        def __str__(self):
             return self.Elective_HD_ID

class anouncement(models.Model):
    title=models.CharField('announcement_title',max_length=120)
    date=models.DateTimeField('announcement_date')
    description=models.TextField(blank=True)
    handler=models.CharField(default='admin',max_length=20)
   

class Faculty_List(models.Model):
     Faculty_List_CHOICES=(("CHE",'Chemical'),("MECH","Mechanical"),("EEE-INSTR","Electrical"),("Computer Science","Computer Science"),("PHY","Physics"),("BIO","Biology"),("CHEM","Chemistry"),("MATHS","Mathematics"),('ECON & MGMT',"Economics"),("HUM","Humanities"))
     first_name=models.CharField(max_length=50)
     last_name=models.CharField(max_length=50)
     Department=models.CharField(max_length=20,choices=Faculty_List_CHOICES,null=True,blank=True)

     def __str__(self):
          return self.first_name+ " " + self.last_name


class department_description(models.Model):
     Department_HOD=models.OneToOneField(User,on_delete=models.CASCADE)
     Department_Choice=(("CHE",'Chemical'),("MECH","Mechanical"),("EEE-INSTR","Electrical"),("Computer Science","Computer Science"),("PHY","Physics"),("BIO","Biology"),("CHEM","Chemistry"),("MATHS","Mathematics"),('ECON & MGMT',"Economics"),("HUM","Humanities"))
     Department_name=models.CharField('Department name',choices=Department_Choice,max_length=50)
     Upcoming_Sem=models.CharField('Upcoming Semester',choices=(('Sem 1','Sem 1'),('Sem 2','Sem 2')),max_length=50,null=True)
     Previous_records=models.CharField('Link for the previous data',max_length=400,null=True,blank=True)
     Lock=models.BooleanField('Lock Website',default=False)
   

     def __str__(self):
          return self.Department_name
     

  
