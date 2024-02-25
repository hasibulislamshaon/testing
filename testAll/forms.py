from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import formsData


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    email=forms.EmailField()
    password1 = forms.CharField(max_length=65, widget=forms.PasswordInput)
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=formsData
        fields = ['fullName','phone','password'] 