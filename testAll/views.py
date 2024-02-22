from django.shortcuts import render
from .models import formsData
from . forms import RegisterForm

# Create your views here.
def Welcome(request):
    data=formsData.objects.all()
    print('output:',data)
    return render(request,'data.html',{'data':data})
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', { 'form': form})
    
   