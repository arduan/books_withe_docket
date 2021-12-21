from django.urls import path
from . import views

urlpatterns = [

    path('', views.show),
    path('test/<int:id_title>', views.one_show, name='title-text'),






]