from django import forms
from django.db.models import Q
from manager.models import Faculty_List
from itertools import chain
from manager.models import PHD_List
from manager.models import department_description
from manager.models import Elective_HD
from manager.models import Elective_FD

class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, queryset, *args, **kwargs):
        super().__init__(queryset, *args, **kwargs)
        self.widget.attrs['class'] = 'searchable-select'  # Add a class to the widget for styling purposes

    def clean(self, value):
        cleaned_data = super().clean(value)
        # Perform custom validation or cleaning logic here if needed
        return cleaned_data





def classformuser(user,initial_val):
        Department_name = department_description.objects.get(Department_HOD=user)
        class classForm(forms.Form):
                FIC = forms.ModelChoiceField(queryset=Faculty_List.objects.filter(Department=Department_name),label="Instructor In Charge",)
                Tutorials = forms.IntegerField(initial=initial_val['Tutorial'])   
                Lectures = forms.IntegerField(initial=initial_val['Lectures'])  
                Labs= forms.IntegerField(initial=initial_val['Labs'])  
        return classForm
  
        

def facultyform1user(user):
  
    department_instance = department_description.objects.get(Department_HOD=user)
    department_name = department_instance.Department_name

    faculties = Faculty_List.objects.filter(Department=department_name)

    class facultyform1(forms.Form):
                faculty_queryset = Faculty_List.objects.filter(Department=department_name)
                phd_queryset = PHD_List.objects.filter(Department=department_name)

      

                Faculty = CustomModelMultipleChoiceField(queryset=faculty_queryset, required=True)
                PHD=forms.ModelMultipleChoiceField(queryset=phd_queryset, required=False)
    
    return facultyform1



def facultyform3user(user):
        department_name = department_description.objects.get(Department_HOD=user)
        class facultyform3(forms.Form):
                faculty_queryset = Faculty_List.objects.filter(Department=department_name)
                phd_queryset = PHD_List.objects.filter(Department=department_name)

      
                Faculty = CustomModelMultipleChoiceField(queryset=faculty_queryset, required=True)
                PHD=forms.ModelMultipleChoiceField(queryset=phd_queryset, required=False)
        return facultyform3

def facultyform2user(user):
        department_name = department_description.objects.get(Department_HOD=user)
        class facultyform2(forms.Form):
                        
                faculty_queryset = Faculty_List.objects.filter(Department=department_name)
                phd_queryset = PHD_List.objects.filter(Department=department_name)

               

                Faculty = CustomModelMultipleChoiceField(queryset=faculty_queryset, required=True)
                PHD=forms.ModelMultipleChoiceField(queryset=phd_queryset, required=False)
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

  

