from django.contrib import admin
from csvexport.actions import  csvexport
from django.http import HttpResponse 
# Register your models here.
from . models import formsData
from import_export.formats.base_formats import CSV, XLSX
IMPORT_FORMATS = [CSV, XLSX]

class adminData(admin.ModelAdmin):
    list_display=('id','fullName','phone')
  
admin.site.register(formsData)


