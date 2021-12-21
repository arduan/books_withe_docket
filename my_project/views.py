from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from .models import Post


def test(request):
    data = {'name': 'Эта страница test.html', 'family': 'Иванов'}
    return render(request, 'my_project/test.html', context=data)


def show(request):
    titles = Post.objects.all()
    return render(request, 'my_project/example.html', {
        'titles': titles,
    })


def one_show(request, id_title: int):
    title = Post.objects.get(id=id_title)
    return render(request, 'my_project/test.html', {
        'title': title,
    })
