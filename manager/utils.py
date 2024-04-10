import pandas as pd
from .models import PHD_List, Faculty_List
from .models import CDC_FD,CDC_HD,Elective_FD,Elective_HD,WILP,General
from django.contrib import admin
import os


def remove_duplicate_entries(model):
    # Get all instances of the specified model
    instances = model.objects.all()

    # Initialize a set to keep track of unique values
    unique_values = set()

    # Initialize a list to store duplicate instances
    duplicate_instances = []

    # Iterate through instances
    for instance in instances:
        # Define criteria for identifying duplicate entries
        unique_identifier = (instance.first_name, instance.Department)  # Adjust as needed

        # Check if the unique identifier is already present
        if unique_identifier in unique_values:
            duplicate_instances.append(instance)
        else:
            # Add the unique identifier to the set
            unique_values.add(unique_identifier)

    # Delete duplicate instances
    for duplicate_instance in duplicate_instances:
        duplicate_instance.delete()


def append_excel_data_to_model(file_path):
    for filename in os.listdir(file_path):
        if filename.endswith('xlsx'): 
            filepath=os.path.join(file_path, filename)
    try:
        df = pd.read_excel(filepath)
    except FileNotFoundError:
        return
    for index, row in df.iterrows():
  
        if row['stat'] == 'Faculty':
            existing_faculty = Faculty_List.objects.filter(first_name=row['full name'], Department=row['dept']).exists()
            if not existing_faculty:
                instance = Faculty_List(
                    ID_No=row['psrn/ idno'],
                    first_name=row['full name'],
                    Department=row['dept'],
                   
                )
               
                instance.save()
                
        elif row['stat'] == 'PHD':
            existing_phd = PHD_List.objects.filter(first_name=row['full name'], Department=row['dept']).exists()
            if not existing_phd:
                instance = PHD_List(
                    PSM_No=row['psrn/ idno'],
                    first_name=row['full name'],
                    Department=row['dept'],
              
                )
                instance.save()
                class Meta:
                     ordering = ['first_name']
   

def append_excel_data_to_model_cdc(file_path,file_sheet):
    for filename in os.listdir(file_path):
        if filename.endswith('xlsx'): 
            filepath=os.path.join(file_path, filename)
    try:
        df = pd.read_excel(filepath)
        
    except FileNotFoundError:
        return
    CDC_FD.objects.all().delete()
    df = pd.read_excel(filepath,sheet_name=file_sheet)
        
    for index, row in df.iterrows():
            if str(row["DEGREE"])[:4]=="B.E.":
        
                existing_CDC_FD = CDC_FD.objects.filter(CDC_name=row['COURSE TITLE'], CDC_Department=row['DEPT']).exists()
                if not existing_CDC_FD:
                    instance = CDC_FD(
                        CDC_ID=row['COURSE NO'],
                        CDC_name=row['COURSE TITLE'],
                        CDC_Department=row['DEPT'],
                        Upcoming_Sem_FD=row['SEM']
                   
                )
                
                instance.save()
            else:
                   existing_CDC_HD = CDC_HD.objects.filter(CDC_HD_name=row['COURSE TITLE'], CDC_HD_Department=row['DEPT']).exists()
                   if not existing_CDC_HD:
                    instance = CDC_FD(
                        CDC_ID=row['COURSE NO'],
                        CDC_name=row['COURSE TITLE'],
                        CDC_Department=row['DEPT'],
                        Upcoming_Sem_FD=row['SEM']
                   
                )
                
                    instance.save()

def append_excel_data_to_model_el(file_path,file_sheet):
    for filename in os.listdir(file_path):
        if filename.endswith('xlsx'): 
            filepath=os.path.join(file_path, filename)
    try:
        df = pd.read_excel(filepath)
       
    except FileNotFoundError:
        return
    Elective_FD.objects.all().delete()
    Elective_HD.objects.all().delete()
    WILP.objects.all().delete()
    df = pd.read_excel(filepath,sheet_name=file_sheet)
        
    for index, row in df.iterrows():
            
            if str(row["DISCIPLINE ELECTIVE"])[:4]=="M.E.":
          
                existing_Elective_HD = Elective_HD.objects.filter(Elective_HD_name=row['COURSE TITLE'], Elective_HD_Department=row['DEPT']).exists()
                if not existing_Elective_HD:
                   
                    instance = Elective_HD(
                        Elective_HD_ID=row['COURSE NO'],
                        Elective_HD_name=row['COURSE TITLE'],
                        Elective_HD_Department=row['DEPT'],
                       
                   
                )
                instance.save()
            elif str(row["DISCIPLINE ELECTIVE"])[:4]=="WILP":
                existing_WILP = WILP.objects.filter(WILP_name=row['COURSE TITLE'], WILP_Department=row['DEPT']).exists()
                if not existing_WILP:
                    instance = WILP(
                        WILP_ID=row['COURSE NO'],
                        WILP_name=row['COURSE TITLE'],
                        WILP_Department=row['DEPT'],
                       
                   
                )
                instance.save()
            elif str(row["DISCIPLINE ELECTIVE"])=="GENERAL":
                existing_General = General.objects.filter(General_name=row['COURSE TITLE']).exists()
                if not existing_General:
                   
                    instance = General(
                        General_ID=row['COURSE NO'],
                        General_name=row['COURSE TITLE'],
                       
                   
                )
                instance.save()


            else:
                existing_Elective_FD = Elective_FD.objects.filter(Elective_name=row['COURSE TITLE'], Elective_Department=row['DEPT']).exists()
                if not existing_Elective_FD:
                    instance = Elective_FD( 
                        Elective_ID=row['COURSE NO'],
                        Elective_name=row['COURSE TITLE'],
                        Elective_Department=row['DEPT'],          
                   
                )
                instance.save()

