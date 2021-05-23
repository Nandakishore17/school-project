
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('index',views.testfun1,name='index'),
    path('calc',views.testfun2,name='calc'),
    path('form',views.testfun3,name='form'),
    
    


]