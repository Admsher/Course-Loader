from django.urls import path,include
from user.views import login_user
from django.contrib import admin



urlpatterns = [
    path('', login_user, name="login"),
   

]

admin.site.site_header = "BITS Timetable admin"

admin.site.site_title = "BITS Timetable admin"