from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


def index(request):
    """
    :param request: Получат запрос и ...
    :return: Возвращает в базовый шаблон base.html словарь data и отображает в шаблоне по ключу словаря.
    """
    data = {'name': 'Виталий', 'family': 'Иванов'}
    return render(request, 'my_project/base.html', context=data)


def test(request):
    return render(request, 'test.html')


def example(request):
    return render(request, 'example.html')



