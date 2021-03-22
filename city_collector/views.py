from django.shortcuts import render, redirect
from django import forms

from django.forms import BaseFormSet
from django.forms import formset_factory
from .forms import CityForm
from .models import RandomCity


def post_city(request):
    city = []
    CityFormset = formset_factory(CityForm)
    if request.method == 'GET':
        formset = CityFormset(request.GET or None)
    elif request.method == 'POST':
        formset = CityFormset(request.POST)
        for form in formset:
            if form.is_valid():
                print(form.cleaned_data)
                city.append(form.cleaned_data)
                print(city)
                cleaned_city = form.cleaned_data.get('city')
                print(form.cleaned_data.get('city'))
                if city:
                    RandomCity(city=cleaned_city).save()
                return redirect('/city/')

    return render(request, 'form.html', {'formset': formset})


# class BaseCityFormset(BaseFormSet):
#     def add_fields(self, form, index):
#         super().add_fields(form, index)
#         form.fields['city'] = forms.CharField(label=f'City {index}',
#                                               widget=forms.TextInput(attrs={'placeholder': 'Enter random city here'}),
#                                               max_length=30)


def list_of_cities(request):
    pass
