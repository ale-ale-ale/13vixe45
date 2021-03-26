from django import forms
from django.forms import formset_factory


class CityForm(forms.Form):
    city = forms.CharField(label='City',
                           widget=forms.TextInput(attrs={'placeholder': 'Enter random city here'}), max_length=30)


CityFormset = formset_factory(CityForm, validate_min=1, min_num=1, extra=0)
