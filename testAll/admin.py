from django.contrib import admin
from csvexport.actions import  csvexport
from django.http import HttpResponse 
# Register your models here.
from . models import formsData
from import_export.admin import ImportExportModelAdmin

class adminData(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('id','fullName','phone','uuid')
  
admin.site.register(formsData,adminData)


