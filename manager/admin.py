from django.contrib import admin
from .models import CDC_FD, CDC_HD, Elective_FD, Elective_HD, WILP, anouncement, Faculty_List, PHD_List, department_description,General
from django.core.exceptions import FieldError
import os
from django.conf import settings
import subprocess
class DepartmentFilter(admin.SimpleListFilter):
  
    title = 'Department'
    
    parameter_name = 'department'

    def lookups(self, request, model_admin):
        try:
            departments = set(model_admin.get_queryset(request).values_list('Department', flat=True))
        except FieldError:
            try:
                departments = set(model_admin.get_queryset(request).values_list('CDC_Department', flat=True))
            except FieldError:
                try:
                    departments = set(model_admin.get_queryset(request).values_list('CDC_HD_Department', flat=True))
                except FieldError:
                    try:
                        departments = set(model_admin.get_queryset(request).values_list('Elective_HD_Department', flat=True))
                    except FieldError:
                        try:
                            departments = set(model_admin.get_queryset(request).values_list('Elective_Department', flat=True))
                        except FieldError:
                                departments = set(model_admin.get_queryset(request).values_list('WILP_Department', flat=True))
                
                

        return [(department, department) for department in departments]

    def queryset(self, request, queryset):
        if self.value():
            try:
                return queryset.filter(CDC_Department=self.value())
            except FieldError:
                try:
                    return queryset.filter(CDC_HD_Department=self.value())
                except FieldError:
                    try:
                        return queryset.filter(Elective_Department=self.value())
                    except FieldError:
                        try:
                            return queryset.filter(Elective_HD_Department=self.value())
                        except FieldError:
                            try:
                                return queryset.filter(WILP_Department=self.value())
                            except FieldError:
                       
                                return queryset.filter(Department=self.value())

class CDC_FDAdmin(admin.ModelAdmin):
    list_display = ['CDC_ID', 'CDC_name']
    list_filter = (DepartmentFilter,)

class CDC_HDAdmin(admin.ModelAdmin):
    list_display = ['CDC_HD_ID', 'CDC_HD_name']
    list_filter = (DepartmentFilter,)

class Elective_FDAdmin(admin.ModelAdmin):
    list_display = ['Elective_ID', 'Elective_name']
    list_filter = (DepartmentFilter,)

class Elective_HDAdmin(admin.ModelAdmin):
    list_display = ['Elective_HD_ID', 'Elective_HD_name']
    list_filter = (DepartmentFilter,)

class WILPAdmin(admin.ModelAdmin):
    list_display = ['WILP_ID', 'WILP_name']
    list_filter = (DepartmentFilter,)

class GeneralAdmin(admin.ModelAdmin):
    list_display = ['General_ID', 'General_name']
    list_filter = (DepartmentFilter,)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
   

class Faculty_ListAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'ID_No']
    list_filter = (DepartmentFilter,)

class PHD_ListAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'PSM_No']
    list_filter = (DepartmentFilter,)

class Department_DescriptionAdmin(admin.ModelAdmin):
    list_display = ['Department_name', 'Department_HOD']




# Register models with respective admin classes
admin.site.register(CDC_FD, CDC_FDAdmin)
admin.site.register(CDC_HD, CDC_HDAdmin)
admin.site.register(Elective_FD, Elective_FDAdmin)
admin.site.register(Elective_HD, Elective_HDAdmin)
admin.site.register(WILP, WILPAdmin)
admin.site.register(anouncement, AnnouncementAdmin)
admin.site.register(Faculty_List, Faculty_ListAdmin)
admin.site.register(PHD_List, PHD_ListAdmin)
admin.site.register(department_description, Department_DescriptionAdmin)
admin.site.register(General)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2'),
        }),
        
    )

from .models import  Files,Cachefile
class UploadAdmin(admin.ModelAdmin):
    list_display = ['academic_year', 'semester', 'department', 'file']
    actions=["delete"]
    def save_model(self, request, obj, form, change):
        
        if obj.file and (not change or obj.file != obj._meta.get_field('file').get_default()):
            if os.path.exists(obj.file.path):
                os.remove(obj.file.path)
            obj.file.save(obj.file.name, obj.file, save=False)

        # Save the model instance
        super().save_model(request, obj, form, change)


    @admin.action(permissions=["delete_locally"] ,description="Delete file from server")
    def delete(self, request, obj):
        
        # Delete the file associated with the model instance
        for instance in obj:
            file_path = str(settings.BASE_DIR)+str(instance)
            print(file_path)
            if os.path.exists(file_path):
                print("exists")
                os.remove(file_path)
            else:
                file_path=str(settings.BASE_DIR)+f"\{instance.academic_year}\{instance.semester}\{instance.department}\{instance}"
                os.remove(file_path)
        
        # Delete the model instance
        super().delete_model(request, obj)
    delete.allowed_permissions=["delete"]

class UploadAdmincache(admin.ModelAdmin):
    list_display = ['file']
    actions=["delete"]
    def save_model(self, request, obj, form, change):
        
        if obj.file and (not change or obj.file != obj._meta.get_field('file').get_default()):
            if os.path.exists(obj.file.path):
                os.remove(obj.file.path)
            obj.file.save(obj.file.name, obj.file, save=False)

        # Save the model instance
        super().save_model(request, obj, form, change)


    @admin.action(permissions=["delete_locally"] ,description="Delete file from server")
    def delete(self, request, obj):
        
        # Delete the file associated with the model instance
        for instance in obj:
            file_path = str(instance.file)
         
            print(instance.file)
            if os.path.exists(file_path):

                os.remove(file_path)
      
                
                
        
        # Delete the model instance
        super().delete_model(request, obj)
    delete.allowed_permissions=["delete"]

admin.site.register(Files, UploadAdmin)
admin.site.register(Cachefile,UploadAdmincache)





admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
