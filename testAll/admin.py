from django.contrib import admin
from csvexport.actions import  csvexport
# Register your models here.
from . models import formsData
class adminData(admin.ModelAdmin):
    list_display=('id','fullName','phone')
    actions = [csvexport]
admin.site.register(formsData,adminData)

