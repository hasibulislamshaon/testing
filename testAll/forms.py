from django import forms
from . import models


class register(forms.Form):
    fullName=forms.CharField()
    phone=forms.IntegerField()
"""class register(forms.ModelForm):
    class meta:
       myModlel=models.formsData
       fields={'fullName','phone'}
       labels={'fullName':"Name",'phone':"phone"} 
"""