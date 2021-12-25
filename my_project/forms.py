from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    age = forms.CharField(label='Возраст', max_length=4)
    text = forms.CharField(label='Текст', max_length=200)
