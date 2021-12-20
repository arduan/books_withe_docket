from django.urls import path

from my_project.views import *
from . import views

urlpatterns = [

    path('', index, name='index'),
    path('about/', about, name='about'),
    path('test/', test, name='test'),
    path('show/', views.show, name='example'),




]