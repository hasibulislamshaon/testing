from django.db import models
import uuid 


# Create your models here.
class formsData(models.Model):
    uuid= models.UUIDField(default=uuid.uuid4,editable=False)
    id=models.AutoField(primary_key=True,default=None)
    fullName=models.CharField(max_length=(200),default=None)
    phone=models.CharField(max_length=(20),default=None)
    password=models.CharField(max_length=(20),default='')

    def __str__(self):
        return str(self.id)
    










#admin register 

    

