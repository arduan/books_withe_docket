from django.urls import path
from my_project.views import *

urlpatterns = [

    path('', index),
    path('test/', test),


]