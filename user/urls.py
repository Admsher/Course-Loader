
from django.urls import path
from . import views

urlpatterns = [
    path('home_page', views.home, name="home"),
    path('previousrecord', views.previousrecord, name="previousrecord"),
    path('login_user',views.login_user,name='login'),
    path('upload_page',views.upload,name='upload'),
    path('filldata_page',views.filldata,name='filldata'),
    path('form_CDC',views.form_CDC,name='form_CDC'),
    path('choose_new_table',views.choose_new_table,name='choose_new_table'),
    path('CDC_FD_list',views.CDC_FD_list,name='CDC_FD_list'),
    path('CDC_HD_list',views.CDC_HD_list,name='CDC_HD_list'),
    path('Elective_FD_list',views.Elective_FD_list,name='Elective_FD_list'),
    path('Elective_HD_list',views.Elective_HD_list,name='Elective_HD_list'),
    path(r'form_Faculty_Lec',views.form_faculty_lec,name='form_Faculty_Lec'),
    path(r'form_Faculty_Tut',views.form_faculty_tut,name='form_Faculty_Tut'),
    path(r'form_Faculty_Lab',views.form_faculty_lab,name='form_Faculty_Lab'),
    path('previewForm',views.previewForm,name='previewForm')
]