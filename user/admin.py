from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['f_name','l_name','email']
    list_filter = ['f_name','l_name']
    list_editable = ['l_name',]


admin.register(UserAdmin)