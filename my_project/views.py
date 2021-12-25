from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Post
from django.shortcuts import render
from .forms import NameForm, AcauntForm


def test(request):
    data = {'name': 'Эта страница test.html', 'family': 'Иванов'}
    return render(request, 'my_project/test.html', context=data)


def show(request):
    titles = Post.objects.order_by('title')
    return render(request, 'my_project/example.html', {
        'titles': titles,
    })


def one_show(request, id_title: int):
    title = Post.objects.get(id=id_title)
    return render(request, 'my_project/test.html', {
        'title': title,

    })

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'my_form.html', {'form': form,})

def form_for_acaunt(request):
    acaunt_form = AcauntForm(request.POST)
    return render(request, 'my_form.html', {'acaunt_form': acaunt_form,})