from django.db import models

# Create your models here.
class formsData(models.Model):
    fullName=models.CharField(max_length=(200),default=None)
    phone=models.BigIntegerField(default=None)
    

