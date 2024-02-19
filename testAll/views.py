from django.shortcuts import render
from .models import formsData
from .forms import register
# Create your views here.
def Welcome(request):
    if request.method == "POST":
       form=register(request.POST)
       if form.is_valid():
           name=form.cleaned_data['fullName']
           phone=form.cleaned_data['phone']
           data=formsData.objects.create(fullName=name,phone=phone)
           data.save()
       else: 
        form=register()
    context={"form":form}
    return render(request,'index.html',context)

"""
def registerPerson(request):
    #form=register()
    return render(request,'data.html')#{'form': form})


from django.shortcuts import render
from .models import MyModel
from .forms import MyForm

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'cv-form.html', {'form': form})"""