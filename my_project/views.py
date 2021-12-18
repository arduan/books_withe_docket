from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.


def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


def example(request):
    return render(request, 'example.html')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, world')
