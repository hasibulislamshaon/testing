from django.contrib import admin
from csvexport.actions import  csvexport
from django.http import HttpResponse 
# Register your models here.
from . models import formsData
def export_as_csv(modeladmin, request, queryset):
    data = queryset.values()
    csv_export = csvexport()
    csv_content = csv_export.export(data)
    response = HttpResponse(csv_content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mydata.csv"'
    return response
export_as_csv.short_description = "Export Selected as CSV"
@admin.register(formsData)
class adminData(admin.ModelAdmin):
    list_display=('id','fullName','phone')
    actions = [export_as_csv]


