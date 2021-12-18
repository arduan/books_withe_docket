from django.urls import path
from my_project.views import *

urlpatterns = [

    path('', index, name='index'),
    path('test/', test),
    path('example/', example),


]