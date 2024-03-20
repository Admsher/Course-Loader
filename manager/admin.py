from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import CDC_FD
from .models import Faculty_List
from . models import anouncement
from . models import department_description
from .models import CDC_HD
from .models import Elective_FD
from .models import Elective_HD
from .models import PHD_List
from .models import WILP



# Register your models here.
admin.site.unregister(Group)
class CDC_FD_names(admin.StackedInline):
    model=CDC_FD

class Department_Desc_Inline(admin.StackedInline):
    model=department_description

    inlines=[CDC_FD_names]

class UserAdmin(admin.ModelAdmin):

    model= User

    fields=["username","password"]
    
  
    inlines=[Department_Desc_Inline]
    
    
    


 



class Faculties(admin.ModelAdmin):
    model=Faculty_List







admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(CDC_FD)
admin.site.register(CDC_HD)
admin.site.register(PHD_List)
admin.site.register(Faculty_List)
admin.site.register(department_description)
admin.site.register(anouncement)
admin.site.register(Elective_HD)
admin.site.register(Elective_FD)
admin.site.register(WILP)

# admin.site.register(classform)

