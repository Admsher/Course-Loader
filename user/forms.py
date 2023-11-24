from django import forms

from manager.models import Faculty_List

from manager.models import department_description
from manager.models import Elective_HD
from manager.models import Elective_FD




def classformuser(user):
        Department_name = department_description.objects.get(Department_HOD=user)
        class classForm(forms.Form):
                FIC = forms.ModelChoiceField(queryset=Faculty_List.objects.filter(Department=Department_name),label="Faculty In Charge")
                Tutorials = forms.IntegerField()   
                Lectures = forms.IntegerField()  
                Labs= forms.IntegerField()  
        return classForm
  
        

def facultyform1user(user):
        Department_name = department_description.objects.get(Department_HOD=user)
        class facultyform1(forms.Form):
                Faculty = forms.ModelChoiceField(queryset=Faculty_List.objects.filter(Department=Department_name),required=True)
                
        return facultyform1

def facultyform3user(user):
        Department_name = department_description.objects.get(Department_HOD=user)
        class facultyform3(forms.Form):
                Faculty = forms.ModelChoiceField(queryset=Faculty_List.objects.filter(Department=Department_name),required=True)
        return facultyform3

def facultyform2user(user):
        Department_name = department_description.objects.get(Department_HOD=user)
        class facultyform2(forms.Form):
                Faculty = forms.ModelChoiceField(queryset=Faculty_List.objects.filter(Department=Department_name),required=True)
        return facultyform2


def Electiveform_FDuser(user):
        Department_name = department_description.objects.get(Department_HOD=user)
        class ElectiveForm_FD(forms.Form):
                Elective_ID=forms.ModelMultipleChoiceField(queryset=Elective_FD.objects.filter(Elective_Department=Department_name),widget=forms.CheckboxSelectMultiple,label="",required=False)
        return ElectiveForm_FD

def Electiveform_HDuser(user):
        Department_name = department_description.objects.get(Department_HOD=user)
        class ElectiveForm_HD(forms.Form):
                Elective_ID=forms.ModelMultipleChoiceField(queryset=(Elective_HD.objects.filter(Elective_HD_Department=Department_name)),widget=forms.CheckboxSelectMultiple,label="",required=False)
        return ElectiveForm_HD

class Semform(forms.Form):
      Sidenote=forms.CharField(widget=forms.TextInput(attrs={'size':80}),required=False)

  

