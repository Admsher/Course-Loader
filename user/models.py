from django.db import models
from django.contrib.auth.models import User





class previewForm(models.Model):
    CDC_name=models.CharField(max_length=100)
    Tut_number=models.CharField(max_length=100)
    Lect_number=models.CharField(max_length=100)
    Lab_number=models.CharField(max_length=100)
    Faculty_List=models.CharField(max_length=100)



class facultyForm(models.Model):
    Faculty_list=[]
    Faculty_name=models.CharField("Faculty name",max_length=120,choices=Faculty_list,blank=True,null=True)




