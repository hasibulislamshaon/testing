from django.urls import path
from . import views
urlpatterns=[
    path('',views.Welcome,name="Welcome Page"),
    #path('', views.registerPerson, name='form')
]