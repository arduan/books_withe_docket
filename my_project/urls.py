from django.urls import path
from my_project.views import index

urlpatterns = [

    path('', index),


]