from django.urls import path

import forms

from . import views

urlpatterns = [

    path('', views.show),
    path('test/<int:id_title>', views.one_show, name='title-text'),
    path('my_form/', views.get_name, name='form'),
    path('my_form/', views.form_for_acaunt, name='acaunt_form'),






]