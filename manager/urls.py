from django.urls import path,include
from user.views import login_user
from django.contrib import admin
from .utils import append_excel_data_to_model
from .utils import append_excel_data_to_model_cdc,append_excel_data_to_model_el

from manager.models import department_description
# Trigger the data import process when Django starts
file_path = "FACULTY & PHD LIST"
file_path_courses="CDC & ELECTIVE"
append_excel_data_to_model(file_path)
append_excel_data_to_model_cdc(file_path_courses,'CDC')
append_excel_data_to_model_el(file_path_courses,'ELECTIVES')

urlpatterns = [
    path('', login_user, name="login"),
   
   
]

admin.site.site_header = "BITS Timetable admin"

admin.site.site_title = "BITS Timetable admin"