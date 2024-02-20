from django.urls import path
from . import views
urlpatterns=[
    path('',views.Welcome,name="Welcome Page"),
    #path('login/', views.sign_in, name='login'),
    #path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
   
]