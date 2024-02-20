from django.db import models


# Create your models here.
class formsData(models.Model):
    fullName=models.CharField(max_length=(200),default=None)
    phone=models.CharField(max_length=(20),default=None)

    def __str__(self):
        return str(self.id)
    










#admin register 

    

